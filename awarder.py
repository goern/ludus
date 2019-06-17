import ssl
import faust
from configs import config
from configs.badge_configuration import badges as badge_config
from configs.config import awarder_configuration
from configs.config import datastore_configuration
from events.ludus_event import LudusEvent
from events.ludus_badge import LudusBadge
from ludus.datastore import Datastore
import json

#Setting up Faust app
ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=config.kafka_configuration['cacert_file'])
app = faust.App(awarder_configuration['faust_app_name'], broker='kafka://'+config.kafka_configuration['bootstrap_server'], broker_credentials=ssl_context)

#Setting Kafka topic for stream processors
events = app.topic(config.kafka_configuration['topic'], value_type=LudusEvent)
badges = app.topic(config.kafka_configuration['topic'], value_type=LudusBadge)

#Initializing faust tables
aggregated_event_data = app.Table(awarder_configuration['events_table_name'], default=dict, partitions=2)
awarded_badges = app.Table(awarder_configuration['badges_table_name'], default=None, partitions=2)

#Initializing datastore
datastore = Datastore.get_datastore(datastore_configuration['type'])

#Processes ludus event stream
@app.agent(events)
async def aggregate_events(events):

    async for event in events:
        if event.type is None:
            if event.username not in aggregated_event_data:
                aggregated_user_data = {event.event_type : 1}
                aggregated_event_data[event.username] = aggregated_user_data
            else:
                aggregated_user_data = aggregated_event_data[event.username]

                if event.event_type not in aggregated_user_data:
                    aggregated_user_data[event.event_type] = 1
                else:
                    aggregated_user_data[event.event_type] += 1

                aggregated_event_data[event.username] = aggregated_user_data

#Task to award badges
@app.timer(30.0)
async def award_badges():

    if aggregated_event_data is not None:
        for username in aggregated_event_data.keys():
            events = aggregated_event_data[username]
            print(username)
            print(events)
            for event_type in events.keys():
                award_badge(username,event_type,events[event_type])

#Stores badges in Faust table so that are not reawareded to a User
@app.agent(badges)
async def store_badges(badges):

    async for badge in badges:
        if badge.type == 'badge':
            if badge.username not in awarded_badges:
                awarded_badges[badge.username] = set()

            awarded_badges_to_current_user = set(awarded_badges[badge.username])
            awarded_badges_to_current_user.add(badge.badge)
            awarded_badges[badge.username] = awarded_badges_to_current_user


#Creates a badge
def award_badge(username, event_type, count):
    for badge_name in badge_config.keys():
        badge_detail = badge_config[badge_name]

        if badge_detail['event_type'] == event_type and \
                 count >= badge_detail['criteria'] and \
                (username not in awarded_badges or \
                 badge_name not in awarded_badges[username]):
            new_badge = {
                'type': 'badge',
                'username': username,
                'badge': badge_name,
                'description': badge_detail['description'],
                'event_type': event_type,
                'criteria': badge_detail['criteria']
            }
            new_badge_json = json.dumps(new_badge)
            datastore.insert(new_badge_json.encode('utf-8'))


if __name__ == "__main__":
    app.main()