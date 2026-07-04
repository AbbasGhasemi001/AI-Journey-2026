import json
from datetime import date
#-------------------------------
class HabitTracker:
    def __init__(self):
        self.file_name="habits.json"
    def show_main(self):
        print("\n===== Habit Tracker =====")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Exit")
    def load_habits(self):
        try:
            with open (self.file_name,"r")as file:
                habits = json.load(file)
                return habits
        except(FileNotFoundError,json.JSONDecodeError):
            return []
    def save_habits(self,habits):
        with open(self.file_name,"w")as file:
            json.dump(habits,file,indent=4)
    def add_habit(self):
        habit_name=input("Enter your habit :").strip()
        if habit_name=="":
            print("habit cannot be empty !")
            return
        habit={
                "name":habit_name,
                "created_at":date.today().strftime('%Y-%m-%d'),
                "history":[] }
        habits=self.load_habits()
        habits.append(habit)
        self.save_habits(habits)
        print("Habit added successfully!")
    def view_habits(self):
        habits=self.load_habits()
        if len(habits)==0:
            print("no data found !")
        else :
            print ("\n---------Habits-------------")
            for index , habit in enumerate(habits,start=1):
                print("\n--------------------------")
                print(f"{index}.{habit['name']}")
                print(f"created at: {habit['created_at']}")
                print(f"Done days : {len(habit['history'])}")
    def run(self):
        while True:
            self.show_main()
            choice=input("enter your number :").strip()
            if choice=="1":
                self.add_habit()
            elif choice=="2":
                self.view_habits()
            elif choice=="3":
                print("Goodbye 👋")
                break
            else:
                print("invalid choice??!")





app = HabitTracker()
app.run()