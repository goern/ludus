import datetime
import re

class GithubEventFormatter:
    def get_formatter(event_type):
        if event_type == "issue":
            return IssueEventFormatter()
        elif event_type == "issue_closed":
            return IssueClosedEventFormatter()
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

class IssueClosedEventFormatter:
    def format(self, event, event_type):
        formatted_event = dict()
        formatted_event['username'] = event['issue']['user']['login']
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
        formatted_event['issue_closes'] = self.parse_issue_number(event)
        formatted_event['raw_github'] = event

        return formatted_event

    def parse_issue_number(self, event):
        body = event['pull_request']['body']
        issue_number = None

        match_found = re.search('closes #[0-9]+', body)
        if match_found:
            print(match_found)
            issue_closes = match_found.group(0)
            issue_number = re.search('[0-9]+', issue_closes).group(0)

        return issue_number


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
