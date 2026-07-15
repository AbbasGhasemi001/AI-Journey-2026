import json
from datetime import date
from habit import Habit


class HabitTracker:
    def __init__(self):
        self.file_name = "habits.json"

    def show_main(self):
        print("\n===== Habit Tracker =====")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Mark Habit as Done")
        print("4. View Habit History")
        print("5. Delete Habit")
        print("6. Analyze Habits")
        print("7. Exit")

    def load_habits(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                habit_data = json.load(file)

            habit_objects = []

            for data in habit_data:
                habit = Habit.from_dict(data)
                habit_objects.append(habit)

            return habit_objects

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_habits(self, habits):
        habit_data = []

        for habit in habits:
            habit_data.append(habit.to_dict())

        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(habit_data, file, indent=4, ensure_ascii=False)

    def select_habit(self):
        habits = self.load_habits()

        if len(habits) == 0:
            print("No habits found!")
            return None, None

        self.view_habits(habits)

        try:
            number = int(input("Enter habit number: "))
        except ValueError:
            print("Please enter a valid number!")
            return None, None

        index = number - 1

        if index < 0 or index >= len(habits):
            print("Invalid habit number!")
            return None, None

        return habits, index

    def add_habit(self):
        habit_name = input("Enter your habit: ").strip()

        if habit_name == "":
            print("Habit cannot be empty!")
            return

        habits = self.load_habits()

        new_habit = Habit(habit_name)
        habits.append(new_habit)

        self.save_habits(habits)
        print("Habit added successfully!")

    def view_habits(self, habits=None):
        if habits is None:
            habits = self.load_habits()

        if len(habits) == 0:
            print("No habits found!")
            return

        print("\n===== Habits =====")

        for index, habit in enumerate(habits, start=1):
            print("\n--------------------------")
            print(f"{index}. {habit.name}")
            print(f"Created at: {habit.created_at}")
            print(f"Done days: {len(habit.history)}")

    def mark_done_today(self):
        habits, index = self.select_habit()

        if habits is None:
            return

        today = date.today().strftime("%Y-%m-%d")
        selected_habit = habits[index]

        if today in selected_habit.history:
            print("This habit is already marked as done today!")
            return

        selected_habit.history.append(today)

        self.save_habits(habits)
        print(f"{selected_habit.name} marked as done for today!")

    def view_habit_history(self):
        habits, index = self.select_habit()

        if habits is None:
            return

        selected_habit = habits[index]

        if len(selected_habit.history) == 0:
            print(f"No history found for {selected_habit.name}!")
            return

        print(f"\nHistory for {selected_habit.name}:")

        for history_index, day in enumerate(
            selected_habit.history,
            start=1,
        ):
            print(f"{history_index}. {day}")

    def delete_habit(self):
        habits, index = self.select_habit()

        if habits is None:
            return

        deleted_habit = habits.pop(index)

        self.save_habits(habits)
        print(f"{deleted_habit.name} has been deleted!")

    def analyze_habits(self):
        habits = self.load_habits()

        if len(habits) == 0:
            print("No habits found!")
            return

        total_habits = len(habits)
        total_done_days = 0

        for habit in habits:
            total_done_days += len(habit.history)

        most_consistent_habit = habits[0]
        max_done_days = len(habits[0].history)

        for habit in habits:
            done_days = len(habit.history)

            if done_days > max_done_days:
                max_done_days = done_days
                most_consistent_habit = habit

        average_done_days = total_done_days / total_habits

        print("\n===== Habit Analysis =====")
        print(f"Total Habits: {total_habits}")
        print(f"Total Done Days: {total_done_days}")
        print(f"Average Done Days per Habit: {average_done_days:.1f}")
        print(
            f"Most Consistent Habit: "
            f"{most_consistent_habit.name} - {max_done_days} days"
        )

    def run(self):
        while True:
            self.show_main()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_habit()

            elif choice == "2":
                self.view_habits()

            elif choice == "3":
                self.mark_done_today()

            elif choice == "4":
                self.view_habit_history()

            elif choice == "5":
                self.delete_habit()

            elif choice == "6":
                self.analyze_habits()

            elif choice == "7":
                print("Goodbye 👋")
                break

            else:
                print("Invalid choice!")
