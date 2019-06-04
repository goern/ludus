from ludus.github_event_formatter import GithubEventFormatter
from ludus.trello_event_formatter import TrelloEventFormatter

class DataFormatter:

    def get_formatter(event_source, event_type):
        if event_source == "github":
            return GithubEventFormatter.get_formatter(event_type)
        elif event_source == "trello":
            return TrelloEventFormatter.get_formatter(event_type)


