from datetime import date
class Habit:
    def __init__(self, name):
        self.name = name
        self.created_at = date.today().strftime("%Y-%m-%d")
        self.history = []

    def to_dict(self):
        return {
            "name": self.name,
            "created_at": self.created_at,
            "history": self.history,
        }

    @staticmethod
    def from_dict(data):
        habit = Habit(data["name"])
        habit.created_at = data["created_at"]
        habit.history = data["history"]
        return habit