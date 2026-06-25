import json
from datetime import datetime


# ===== User =====

try:
    with open("user.json", "r") as file:
        user = json.load(file)

    name = user["name"]

except (FileNotFoundError, json.JSONDecodeError):

    name = input("Enter your name: ")

    user = {
        "name": name
    }

    with open("user.json", "w") as file:
        json.dump(user, file, indent=4)


# ===== Main Program =====

while True:

    print(f"\n===== AI Study Assistant | {name} =====")

    print("1. Add Study Session")
    print("2. View Study Sessions")
    print("3. Add Goal")
    print("4. View Goals")
    print("5. Analyze Progress")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # =====================
    # Add Study Session
    # =====================

    if choice == "1":

        subject = input("Subject: ")
        hours = float(input("Study Hours: "))
        mood = input("Mood: ")

        date = datetime.now().strftime(
            "%Y-%m-%d"
        )

        session = {
            "subject": subject,
            "hours": hours,
            "date": date,
            "mood": mood
        }

        try:

            with open(
                "session.json",
                "r"
            ) as file:

                data = json.load(file)

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            data = []

        data.append(session)

        with open(
            "session.json",
            "w"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print("Study session saved!")


    # =====================
    # View Sessions
    # =====================

    elif choice == "2":

        try:

            with open(
                "session.json",
                "r"
            ) as file:

                data = json.load(file)

            print(
                "\n===== Study History ====="
            )

            for session in data:

                print(
                    "\n----------------"
                )

                print(
                    f"Subject: {session['subject']}"
                )

                print(
                    f"Hours: {session['hours']}"
                )

                print(
                    f"Date: {session['date']}"
                )

                print(
                    f"Mood: {session['mood']}"
                )

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            print(
                "No study sessions found!"
            )


    # =====================
    # Add Goal
    # =====================

    elif choice == "3":

        goal_name = input(
            "Enter Goal: "
        )

        deadline = input(
            "Deadline: "
        )

        goal = {
            "goal": goal_name,
            "deadline": deadline
        }

        try:

            with open(
                "goal.json",
                "r"
            ) as file:

                goals = json.load(
                    file
                )

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            goals = []

        goals.append(goal)

        with open(
            "goal.json",
            "w"
        ) as file:

            json.dump(
                goals,
                file,
                indent=4
            )

        print("Goal saved!")


    # =====================
    # View Goals
    # =====================

    elif choice == "4":

        try:

            with open(
                "goal.json",
                "r"
            ) as file:

                goals = json.load(
                    file
                )

            print(
                "\n===== Goals ====="
            )

            for goal in goals:

                print(
                    "\n----------------"
                )

                print(
                    f"Goal: {goal['goal']}"
                )

                print(
                    f"Deadline: {goal['deadline']}"
                )

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            print(
                "No goals found!"
            )


    # =====================
    # Analyze Progress
    # =====================

    elif choice == "5":

        try:

            with open(
                "session.json",
                "r"
            ) as file:

                data = json.load(
                    file
                )

            total_hours = 0
            subjects = {}

            for session in data:

                total_hours += (
                    session["hours"]
                )

                subject = (
                    session["subject"]
                )

                if subject not in subjects:

                    subjects[
                        subject
                    ] = 0

                subjects[
                    subject
                ] += session[
                    "hours"
                ]

            average = (
                total_hours /
                len(data)
            )

            most_subject = max(
                subjects,
                key=subjects.get
            )

            # ===== Streak =====

            dates = []

            for session in data:

                dates.append(
                    session["date"]
                )

            dates = [

                datetime.strptime(
                    date,
                    "%Y-%m-%d"
                )

                for date in dates
            ]

            dates.sort()

            streak = 1
            max_streak = 1

            for i in range(
                1,
                len(dates)
            ):

                difference = (
                    dates[i]
                    - dates[i-1]
                )

                if difference.days == 1:

                    streak += 1

                else:

                    streak = 1

                if streak > max_streak:

                    max_streak = streak


            print(
                "\n===== Analysis ====="
            )

            print(
                f"Total Hours: {total_hours}"
            )

            print(
                f"Average Hours: {average:.1f}"
            )

            print(
                f"Most Studied Subject: {most_subject}"
            )

            print(
                f"Study Streak: {max_streak} days 🔥"
            )

        except (
            FileNotFoundError,
            json.JSONDecodeError
        ):

            print(
                "No study data found!"
            )


    elif choice == "6":

        print(
            f"\nGoodbye {name} 👋"
        )

        break

    else:

        print("Invalid choice!")