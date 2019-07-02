import json

class Validator:

    def get_validator(event_source):
        if event_source == "github":
            return GithubEventValidator()
        elif event_source == "trello":
            return TrelloEventValidator()


class GithubEventValidator:
    def is_valid(self, event):



        if 'action' in event and event['action'] == "opened" and 'issue' in event:
            return True, 'issue'
        elif 'action' in event and event['action'] == "closed" and 'issue' in event:
            return True, 'issue_closed'
        elif 'action' in event and event['action'] == "closed" and 'pull_request' in event and \
                event['pull_request']['merged'] == True:
            print(json.dumps(event))
            return True, 'pull_request'
        elif 'comment' in event:
            return True, 'comment'

        return False, None


class TrelloEventValidator:
    def is_valid(self, event):

        #print(json.dumps(event))

        if 'action' in event and 'type' in event['action'] and event['action']['type'] == 'createCard' and \
                event['action']['data']['list']['name'] == 'New':
            return True, 'new_idea'

        elif 'action' in event and 'type' in event['action'] and event['action']['type'] == 'updateCard' \
                and 'listAfter' in event['action']['data'] and ( event['action']['data']['listAfter']['name'] == 'Completed'\
                or event['action']['data']['listAfter']['name'] == 'Done') :
            return True, 'task_completed'

        return False, None

