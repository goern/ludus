class TrelloEventFormatter:
    def get_formatter(event_type):
        if event_type == "new_idea":
            return NewIdeaEventFormatter()
        elif event_type == "task_completed":
            return TaskCompletedEventFormatter()

class NewIdeaEventFormatter:
    def format(self, data):
        return


class TaskCompletedEventFormatter:
    def format(self, data):
        return
