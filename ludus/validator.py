import json

class Validator:

    def get_validator(event_source):
        if event_source == "github":
            return GithubEventValidator()
        elif event_source == "trello":
            return TrelloEventValidator()


class GithubEventValidator:
    def is_valid(self, data):

        #print(json.dumps(data))

        if 'action' in data and data['action'] == "opened" and 'issue' in data:
            return True, 'issue'
        elif 'action' in data and data['action'] == "closed" and 'pull_request' in data:
            return True, 'pull_request'
        elif 'comment' in data:
            return True, 'comment'

        return False, None


class TrelloEventValidator:
    def is_valid(self, data):

        #print(json.dumps(data))

        if 'action' in data and 'type' in data['action'] and data['action']['type'] == 'createCard':
            return True, 'new_idea'
        elif 'action' in data and 'type' in data['action'] and data['action']['type'] == 'updateCard' \
                and 'listAfter' in data['action']['data'] and ( data['action']['data']['listAfter']['name'] == 'Completed'\
                or data['action']['data']['listAfter']['name'] == 'Done') :

            return True, 'task_completed'

        return False, None

