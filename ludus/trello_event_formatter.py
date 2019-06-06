import datetime

class TrelloEventFormatter:
    def get_formatter(event_type):
        if event_type == "new_idea":
            return NewIdeaEventFormatter()
        elif event_type == "task_completed":
            return TaskCompletedEventFormatter()

class NewIdeaEventFormatter:
    def format(self, event, event_type):
        formatted_event = dict()
        formatted_event['username'] = event['action']['memberCreator']['username']
        formatted_event['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_event['event_source'] = 'trello'
        formatted_event['event_url'] = event['model']['url']
        formatted_event['event_type'] = event_type
        formatted_event['raw_trello'] = event

        return formatted_event


class TaskCompletedEventFormatter:
    def format(self, event, event_type):
        formatted_event = dict()
        formatted_event['username'] = event['action']['memberCreator']['username']
        formatted_event['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_event['event_source'] = 'trello'
        formatted_event['event_url'] = event['model']['url']
        formatted_event['event_type'] = event_type
        formatted_event['raw_trello'] = event

        return formatted_event
