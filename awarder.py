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
import re

#Setting up Faust app
ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=config.kafka_configuration['cacert_file'])
app = faust.App(awarder_configuration['faust_app_name'], broker='kafka://'+config.kafka_configuration['bootstrap_server'], broker_credentials=ssl_context)

#Setting Kafka topic for stream processors
events = app.topic(config.kafka_configuration['topic'], value_type=LudusEvent)
badges = app.topic(config.kafka_configuration['topic'], value_type=LudusBadge)

#Initializing faust tables
event_data = app.Table(awarder_configuration['events_table_name'], default=None, partitions=8)
awarded_badges = app.Table(awarder_configuration['badges_table_name'], default=None, partitions=8)


#Initializing datastore
datastore = Datastore.get_datastore(datastore_configuration['type'])

#Processes ludus event stream
@app.agent(events)
async def aggregate_events(events):
    async for event in events.group_by(LudusEvent.username):
        if event.type is None:
            if event.username not in event_data:
                event_list = list()
                event_list.append(event.to_representation())
                event_data[event.username] = event_list
            else:
                event_list = event_data[event.username]
                event_list.append(event.to_representation())
                event_data[event.username] = event_list

@app.timer(120.0)
async def evaluate_user_data_for_badges():
    if event_data is not None:
        for username in event_data.keys():
            for badge_name in badge_config.keys():
                if is_badge_awarded(username, badge_name) == False:
                    award_badge(username,badge_name,  badge_config[badge_name])


def award_badge(username, badge_name, badge_details):
    criteria_type = badge_details['criteria']['type']

    if criteria_type == 'count':
        award_badge_for_type_count(username, badge_name, badge_details)
    elif criteria_type == 'match':
        award_badge_for_type_match(username, badge_name, badge_details)


def is_badge_awarded(username, badge_name):
    if (username not in awarded_badges) or (awarded_badges[username] is None):
        return False
    elif badge_name in awarded_badges[username]:
        return True
    return False

def award_badge_for_type_count(username, badge_name, badge_details):
    count = 0
    events = event_data[username]

    for event in events:
        if event['event_type']== badge_details['event_type']:
            count+=1

    if count >= badge_details['criteria']['value']:
        store_badge(username,badge_name,badge_details, badge_name)

def award_badge_for_type_match(username, badge_name, badge_details):
    events = event_data[username]

    for event in events:
        if event['event_type']== badge_details['event_type']:
            match_value = get_match_value(badge_details['criteria']['field'], event)

            equality = event['event_type'] + str(match_value)
            if is_badge_awarded(username, equality):
                continue

            status = dict()
            for matching_event in badge_details['criteria']['matching_events']:
                status[matching_event['event_type']] = False

            for event in events:
                check_for_matching_events(event, match_value, badge_details['criteria']['matching_events'], status)

                if check_status(status):
                    store_badge(username, badge_name, badge_details, equality)
                    break


def check_for_matching_events(event, match_value, matching_events, status):
    for matching_event in matching_events:
        match_value_current_event = None

        if event['event_type'] == matching_event['event_type']:
            match_value_current_event = get_match_value(matching_event['field'], event)

        if str(match_value) == str(match_value_current_event):
            status[matching_event['event_type']] = True

def check_status(status):
    match = True

    for matching_event in status.keys():
        if status[matching_event]  == False:
            match = False
            break

    return match

def get_match_value(match_field, event):
    is_json = re.search('[.]+', match_field)

    if is_json:
        fields = match_field.split('.')
        match_value = event[fields[0]]

        for i in range(1,len(fields)):
            match_value = match_value[fields[i]]

    else:
        match_value = event[match_field]

    return match_value

#Stores badges in Faust table so that are not reawareded to a User
@app.agent(badges)
async def store_badges(badges):
    async for badge in badges.group_by(LudusBadge.username):
        if badge.type == 'badge':
            if (badge.username not in awarded_badges) or awarded_badges[badge.username] is None:
                awarded_badges[badge.username] = set()

            awarded_badges_to_current_user = set(awarded_badges[badge.username])
            awarded_badges_to_current_user.add(badge.equality)
            awarded_badges[badge.username] = awarded_badges_to_current_user


#Creates a badge
def store_badge(username, badge_name, badge_details,equality):
    new_badge = {
        'type': 'badge',
        'username': username,
        'badge': badge_name,
        'description': badge_details['description'],
        'event_type': badge_details['event_type'],
        'criteria': badge_details['criteria'],
        'equality': equality
    }
    new_badge_json = json.dumps(new_badge)
    datastore.insert(new_badge_json.encode('utf-8'))

if __name__ == "__main__":
    app.main()