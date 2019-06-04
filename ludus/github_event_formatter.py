class GithubEventFormatter:
    def get_formatter(event_type):
        if event_type == "issue":
            return IssueEventFormatter()
        elif event_type == "pull_request":
            return PullRequestEventFormatter()
        elif event_type == "comment":
            return CommentEventFormatter()


class IssueEventFormatter:
    def format(self, data):
        return

class PullRequestEventFormatter:
    def format(self, data):
        return

class CommentEventFormatter:
    def format(self, data):
        return