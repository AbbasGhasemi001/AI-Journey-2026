import json
import calendar
from datetime import datetime, date

try:
    import matplotlib.pyplot as plt
except ImportError:
    plt = None


# =====================
# File Names
# =====================

USER_FILE = "user.json"
SESSION_FILE = "session.json"
GOAL_FILE = "goal.json"


# =====================
# User
# =====================

try:
    with open(USER_FILE, "r") as file:
        user = json.load(file)

    name = user["name"]

except (FileNotFoundError, json.JSONDecodeError, KeyError):

    name = input("Enter your name: ")

    user = {
        "name": name
    }

    with open(USER_FILE, "w") as file:
        json.dump(user, file, indent=4)


# =====================
# Main Menu
# =====================

def show_main():

    print("1. Add Study Session")
    print("2. View Study Sessions")
    print("3. Add Goal")
    print("4. View Goals")
    print("5. Edit Goal")
    print("6. View Goal Progress")
    print("7. Analyze Progress")
    print("8. Show Daily Sessions Chart")
    print("9. Search Session")
    print("10. Edit Session")
    print("11. Delete Session")
    print("12. Exit")


# =====================
# Helper Functions
# =====================

def is_valid_date(date_text):

    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True

    except ValueError:
        return False


# =====================
# Sessions: Load / Save
# =====================

def load_sessions():

    try:
        with open(SESSION_FILE, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_sessions(data):

    with open(SESSION_FILE, "w") as file:
        json.dump(data, file, indent=4)


# =====================
# Add Study Session
# =====================

def add_study_session():

    subject = input("Subject: ").strip()

    if subject == "":
        print("Subject cannot be empty!")
        return

    try:
        hours = float(input("Study Hours: "))

    except ValueError:
        print("Enter a valid number for hours!")
        return

    mood = input("Mood: ").strip()

    session_date = date.today().strftime("%Y-%m-%d")

    session = {
        "subject": subject,
        "hours": hours,
        "date": session_date,
        "mood": mood
    }

    data = load_sessions()
    data.append(session)
    save_sessions(data)

    print("Study session saved!")


# =====================
# View Study Sessions
# =====================

def view_study_sessions():

    data = load_sessions()

    if len(data) == 0:

        print("No study sessions found!")

    else:

        print("\n===== Study History =====")

        for session in data:

            print("\n----------------")
            print(f"Subject: {session.get('subject', 'Unknown')}")
            print(f"Hours: {session.get('hours', 0)}")
            print(f"Date: {session.get('date', 'No date')}")
            print(f"Mood: {session.get('mood', 'No mood')}")


# =====================
# Goals: Load / Save
# =====================

def load_goals():

    try:
        with open(GOAL_FILE, "r") as file:
            goals = json.load(file)

        if isinstance(goals, list):
            return goals

        return []

    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_goals(goals):

    with open(GOAL_FILE, "w") as file:
        json.dump(goals, file, indent=4)


# =====================
# Add Goal
# =====================

def add_goal():

    goal_name = input("Enter Goal: ").strip()

    if goal_name == "":
        print("Goal cannot be empty!")
        return

    start_date = input("Start Date (YYYY-MM-DD): ").strip()

    if not is_valid_date(start_date):
        print("Invalid start date format! Use YYYY-MM-DD.")
        return

    deadline = input("Deadline (YYYY-MM-DD): ").strip()

    if not is_valid_date(deadline):
        print("Invalid deadline format! Use YYYY-MM-DD.")
        return

    start_date_value = datetime.strptime(start_date, "%Y-%m-%d").date()
    deadline_value = datetime.strptime(deadline, "%Y-%m-%d").date()

    if deadline_value < start_date_value:
        print("Deadline cannot be before start date!")
        return

    status = input("Status (not started / in progress / done): ").strip().lower()

    try:
        target_hours = float(input("Target Hours: "))

    except ValueError:
        print("Enter a valid number for target hours!")
        return

    goal = {
        "goal": goal_name,
        "start_date": start_date,
        "deadline": deadline,
        "status": status,
        "target_hours": target_hours
    }

    goals = load_goals()
    goals.append(goal)
    save_goals(goals)

    print("Goal saved!")


# =====================
# View Goals
# =====================

def view_goals():

    goals = load_goals()

    if len(goals) == 0:

        print("No goals found!")

    else:

        print("\n===== Goals =====")

        for goal in goals:

            print("\n----------------")
            print(f"Goal: {goal.get('goal', 'No goal')}")
            print(f"Start Date: {goal.get('start_date', 'No start date')}")
            print(f"Deadline: {goal.get('deadline', 'No deadline')}")
            print(f"Status: {goal.get('status', 'No status')}")
            print(f"Target Hours: {goal.get('target_hours', 'No target hours')}")


# =====================
# Edit Goal
# =====================

def edit_goal():

    goals = load_goals()

    if len(goals) == 0:

        print("No goals found!")
        return

    print("\n===== Edit Goal =====")

    for i, goal in enumerate(goals, start=1):

        print(
            f"{i}. {goal.get('goal', 'No goal')} | "
            f"Deadline: {goal.get('deadline', 'No deadline')} | "
            f"Status: {goal.get('status', 'No status')}"
        )

    try:
        number = int(input("Enter goal number to edit: "))

    except ValueError:
        print("Please enter a valid number!")
        return

    index = number - 1

    if index < 0 or index >= len(goals):

        print("Invalid goal number!")
        return

    selected_goal = goals[index]

    print("\nSelected Goal:")
    print(f"Goal: {selected_goal.get('goal', 'No goal')}")
    print(f"Start Date: {selected_goal.get('start_date', 'No start date')}")
    print(f"Deadline: {selected_goal.get('deadline', 'No deadline')}")
    print(f"Status: {selected_goal.get('status', 'No status')}")
    print(f"Target Hours: {selected_goal.get('target_hours', 'No target hours')}")

    print("\nLeave empty if you do not want to change a field.")

    new_goal = input("Enter new goal: ").strip()
    new_start_date = input("Enter new start date (YYYY-MM-DD): ").strip()
    new_deadline = input("Enter new deadline (YYYY-MM-DD): ").strip()
    new_status = input("Enter new status (not started / in progress / done): ").strip().lower()
    new_target_hours_text = input("Enter new target hours: ").strip()

    if new_goal != "":
        selected_goal["goal"] = new_goal

    if new_start_date != "":

        if not is_valid_date(new_start_date):
            print("Invalid start date format! Use YYYY-MM-DD.")
            return

        selected_goal["start_date"] = new_start_date

    if new_deadline != "":

        if not is_valid_date(new_deadline):
            print("Invalid deadline format! Use YYYY-MM-DD.")
            return

        selected_goal["deadline"] = new_deadline

    if new_status != "":
        selected_goal["status"] = new_status

    if new_target_hours_text != "":

        try:
            selected_goal["target_hours"] = float(new_target_hours_text)

        except ValueError:
            print("Please enter a valid number for target hours!")
            return

    start_date_text = selected_goal.get("start_date", "")
    deadline_text = selected_goal.get("deadline", "")

    if is_valid_date(start_date_text) and is_valid_date(deadline_text):

        start_date_value = datetime.strptime(start_date_text, "%Y-%m-%d").date()
        deadline_value = datetime.strptime(deadline_text, "%Y-%m-%d").date()

        if deadline_value < start_date_value:
            print("Deadline cannot be before start date!")
            return

    save_goals(goals)

    print("Goal updated successfully! ✅")


# =====================
# View Goal Progress
# =====================

def view_goal_progress():

    goals = load_goals()

    if len(goals) == 0:

        print("No goals found!")
        return

    print("\n===== Goal Progress =====")

    today = date.today()

    for goal in goals:

        start_date_text = goal.get("start_date", "")
        deadline_text = goal.get("deadline", "")

        try:
            start_date_value = datetime.strptime(start_date_text, "%Y-%m-%d").date()
            deadline_value = datetime.strptime(deadline_text, "%Y-%m-%d").date()

        except ValueError:
            print("\n----------------")
            print(f"Goal: {goal.get('goal', 'No goal')}")
            print("Status: Invalid date format!")
            continue

        days_passed = (today - start_date_value).days
        days_left = (deadline_value - today).days
        total_days = (deadline_value - start_date_value).days

        if days_left > 0:
            time_status = "In Progress ✅"

        elif days_left == 0:
            time_status = "Due Today 🔥"

        else:
            time_status = "Overdue ⚠️"

        if total_days > 0:
            progress_percent = (days_passed / total_days) * 100
            progress_percent = max(0, min(progress_percent, 100))
        else:
            progress_percent = 100

        print("\n----------------")
        print(f"Goal: {goal.get('goal', 'No goal')}")
        print(f"Start Date: {goal.get('start_date', 'No start date')}")
        print(f"Deadline: {goal.get('deadline', 'No deadline')}")
        print(f"Days Passed: {max(days_passed, 0)}")
        print(f"Days Left: {days_left}")
        print(f"Total Days: {total_days}")
        print(f"Time Progress: {progress_percent:.1f}%")
        print(f"Time Status: {time_status}")
        print(f"Your Status: {goal.get('status', 'No status')}")
        print(f"Target Hours: {goal.get('target_hours', 'No target hours')}")


# =====================
# Analyze Progress
# =====================

def analyze_progress():

    data = load_sessions()

    if len(data) == 0:

        print("No data found!")
        return

    total_hours = 0
    subjects = {}

    for session in data:

        try:
            hours = float(session.get("hours", 0))

        except (ValueError, TypeError):
            hours = 0

        total_hours += hours

        subject = session.get("subject", "Unknown")

        if subject not in subjects:
            subjects[subject] = 0

        subjects[subject] += hours

    average = total_hours / len(data)

    most_subject = max(
        subjects,
        key=subjects.get
    )

    unique_dates = set()

    for session in data:

        try:
            session_date = datetime.strptime(session.get("date", ""), "%Y-%m-%d").date()
            unique_dates.add(session_date)

        except ValueError:
            continue

    if len(unique_dates) == 0:

        max_streak = 0

    else:

        sorted_dates = sorted(unique_dates)

        streak = 1
        max_streak = 1

        for i in range(1, len(sorted_dates)):

            difference = sorted_dates[i] - sorted_dates[i - 1]

            if difference.days == 1:
                streak += 1

            else:
                streak = 1

            if streak > max_streak:
                max_streak = streak

    study_score = (total_hours * 2) + (max_streak * 5) + len(data)

    print("\n===== Analyze Progress =====")
    print(f"Total Hours: {total_hours}")
    print(f"Average Hours: {average:.1f}")
    print(f"Most Studied Subject: {most_subject}")
    print(f"Study Streak: {max_streak} days 🔥")
    print(f"Study Score: {study_score:.1f} points 🏆")


# =====================
# Search Sessions
# =====================

def search_sessions():

    search = input("Enter subject to search: ").strip()

    data = load_sessions()

    found = False

    print("\n===== Search Results =====")

    for session in data:

        if search.lower() in session.get("subject", "").lower():

            print("\n----------------")
            print(f"Subject: {session.get('subject', 'Unknown')}")
            print(f"Hours: {session.get('hours', 0)}")
            print(f"Date: {session.get('date', 'No date')}")
            print(f"Mood: {session.get('mood', 'No mood')}")

            found = True

    if not found:

        print("No session found.")


# =====================
# Edit Session
# =====================

def edit_session():

    data = load_sessions()

    if len(data) == 0:

        print("No study sessions found!")
        return

    print("\n===== Edit Session =====")

    for i, session in enumerate(data, start=1):

        print(
            f"{i}. {session.get('subject', 'Unknown')} | "
            f"{session.get('hours', 0)} hours | "
            f"{session.get('date', 'No date')} | "
            f"{session.get('mood', 'No mood')}"
        )

    try:
        number = int(input("Enter session number to edit: "))

    except ValueError:
        print("Please enter a valid number!")
        return

    index = number - 1

    if index < 0 or index >= len(data):

        print("Invalid number!")
        return

    selected_session = data[index]

    print("\nSelected Session:")
    print(f"Subject: {selected_session.get('subject', 'Unknown')}")
    print(f"Hours: {selected_session.get('hours', 0)}")
    print(f"Date: {selected_session.get('date', 'No date')}")
    print(f"Mood: {selected_session.get('mood', 'No mood')}")

    print("\nLeave empty if you do not want to change a field.")

    new_subject = input("Enter new subject: ").strip()
    new_hours_text = input("Enter new hours: ").strip()
    new_mood = input("Enter new mood: ").strip()

    if new_subject != "":
        selected_session["subject"] = new_subject

    if new_hours_text != "":

        try:
            selected_session["hours"] = float(new_hours_text)

        except ValueError:
            print("Please enter a valid number for hours!")
            return

    if new_mood != "":
        selected_session["mood"] = new_mood

    save_sessions(data)

    print("Session updated successfully! ✅")


# =====================
# Delete Session
# =====================

def delete_session():

    data = load_sessions()

    if len(data) == 0:

        print("No study sessions found!")
        return

    print("\n===== Delete Session =====")

    for i, session in enumerate(data, start=1):

        print(
            f"{i}. {session.get('subject', 'Unknown')} | "
            f"{session.get('hours', 0)} hours | "
            f"{session.get('date', 'No date')}"
        )

    try:
        number = int(input("Enter session number: "))

    except ValueError:
        print("Please enter a valid number!")
        return

    index = number - 1

    if index >= 0 and index < len(data):

        deleted_session = data.pop(index)

        save_sessions(data)

        print(
            f"Deleted: {deleted_session.get('subject', 'Unknown')} | "
            f"{deleted_session.get('hours', 0)} hours | "
            f"{deleted_session.get('date', 'No date')}"
        )

    else:

        print("Invalid number!")


# =====================
# Daily Sessions Chart
# =====================

def show_daily_sessions_chart():

    if plt is None:

        print("matplotlib is not installed!")
        print("Run this command in terminal:")
        print("python -m pip install matplotlib")
        return

    data = load_sessions()

    if len(data) == 0:

        print("No study sessions found!")
        return

    current_year = date.today().year
    current_month = date.today().month

    last_day = calendar.monthrange(current_year, current_month)[1]

    daily_counts = {}

    for day in range(1, last_day + 1):

        chart_date = f"{current_year}-{current_month:02d}-{day:02d}"

        daily_counts[chart_date] = 0

    for session in data:

        session_date = session.get("date", "")

        if session_date in daily_counts:

            daily_counts[session_date] += 1

    dates = list(daily_counts.keys())
    counts = list(daily_counts.values())

    plt.figure(figsize=(12, 5))

    plt.plot(dates, counts, marker="o")

    plt.title("Daily Study Sessions - Current Month")
    plt.xlabel("Date")
    plt.ylabel("Number of Sessions")

    plt.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.show()


# =====================
# Main Program
# =====================

while True:

    print(f"\n===== AI Study Assistant | {name} =====")
    show_main()

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        add_study_session()

    elif choice == "2":

        view_study_sessions()

    elif choice == "3":

        add_goal()

    elif choice == "4":

        view_goals()

    elif choice == "5":

        edit_goal()

    elif choice == "6":

        view_goal_progress()

    elif choice == "7":

        analyze_progress()

    elif choice == "8":

        show_daily_sessions_chart()

    elif choice == "9":

        search_sessions()

    elif choice == "10":

        edit_session()

    elif choice == "11":

        delete_session()

    elif choice == "12":

        print(f"\nGoodbye {name} 👋")
        break

    else:

        print("Invalid choice!")