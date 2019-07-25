#Utilty functions for formatters
import re


class Processor:
    def get_processor(event_type):
        if event_type == 'pull_request':
            return PullRequestEventProcessor()
        else:
            return DefaultEventProcessor()


class DefaultEventProcessor:
    def get_variables(self, event_type, event):
        variables = dict()
        return variables


class PullRequestEventProcessor:
    def get_variables(self, event_type, event):
        print(event_type)
        variables = dict()

        if event_type != 'pull_request':
            raise Exception

        body = event['pull_request']['body']
        issue_number = None

        match_found = re.search('(closes|closed|fix|fixes|fixed|resolve|resolves|resolved)\s*#[0-9]+', body,
                                flags=re.IGNORECASE)
        if match_found:
            issue_closes = match_found.group(0)
            issue_number = re.search('[0-9]+', issue_closes).group(0)

        variables['issue_number'] = issue_number
        return variables


