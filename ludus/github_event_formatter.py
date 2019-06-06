import datetime

class GithubEventFormatter:
    def get_formatter(event_type):
        if event_type == "issue":
            return IssueEventFormatter()
        elif event_type == "pull_request":
            return PullRequestEventFormatter()
        elif event_type == "comment":
            return CommentEventFormatter()


class IssueEventFormatter:
    def format(self, event, event_type):
        formatted_event = dict()
        formatted_event['username'] = event['sender']['login']
        formatted_event['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_event['event_source'] = 'github'
        formatted_event['event_url'] = event['issue']['html_url']
        formatted_event['event_type'] = event_type
        formatted_event['raw_github'] = event

        return formatted_event

class PullRequestEventFormatter:
    def format(self, event, event_type):
        formatted_event = dict()
        formatted_event['username'] = event['sender']['login']
        formatted_event['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_event['event_source'] = 'github'
        formatted_event['event_url'] = event['pull_request']['html_url']
        formatted_event['event_type'] = event_type
        formatted_event['raw_github'] = event

        return formatted_event


class CommentEventFormatter:
    def format(self, event, event_type):
        formatted_event = dict()
        formatted_event['username'] = event['sender']['login']
        formatted_event['timestamp'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_event['event_source'] = 'github'
        formatted_event['event_url'] = event['comment']['html_url']
        formatted_event['event_type'] = event_type
        formatted_event['raw_github'] = event

        return formatted_event
