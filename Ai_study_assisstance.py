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
def show_main ():

    
    print("1. Add Study Session")
    print("2. View Study Sessions")
    print("3. Add Goal")
    print("4. View Goals")
    print("5. Analyze Progress")
    print("6. Search Sesion")
    print("7. Delete Session")
    print("8. Exit")
def load_sessions():
    try:
        with open("session.json", "r") as file:
            data = json.load(file)

        return data

    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_sessions(data):
    with open("session.json", "w") as file:
        json.dump(data, file, indent=4)
def add_study_session():
        
    
        subject = input("Subject: ")
        hours = float(input("Study Hours: "))
        mood = input("Mood: ")

        date = datetime.now().strftime("%Y-%m-%d")

        session = {
        "subject": subject,
        "hours": hours,
        "date": date,
        "mood": mood
        }

        data = load_sessions()
        data.append(session)
        save_sessions(data)

        print("Study session saved!")
def view_study_sessions():

    data = load_sessions()

    if len(data) == 0:

        print("No study sessions found!")

    else:

        print("\n===== Study History =====")

        for session in data:

            print("\n----------------")

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
def load_goals():
    

    try:
        with open("goal.json","r")as file:
            goals =json.load(file)
        return goals
    except (FileNotFoundError,json.JSONDecodeError):
        return []
def save_goals(goals):
    with open ("goal.json","w")as file :
        json.dump(goals,file,indent=4)
def add_goal():

    goal_name = input("Enter Goal: ")
    deadline = input("Deadline: ")

    goal = {
        "goal": goal_name,
        "deadline": deadline
    }

    goals = load_goals()
    goals.append(goal)
    save_goals(goals)

    print("Goal saved!")
def view_goals():
    goals=load_goals()
    if len(goals)==0:
        print("No goals found !")
    else:
        print("\n=================goals====================")
        for goal in goals:
            print ("\n---------------------")
            print(
                f"Goal :{goal['goal']}"
            )
            print (f"Deadline:{goal['deadline']}")
def analyze_progress():

    data = load_sessions()

    if len(data) == 0:

        print("No data found!")

    else:

        total_hours = 0
        subjects = {}

        for session in data:

            total_hours += session["hours"]

            subject = session["subject"]

            if subject not in subjects:

                subjects[subject] = 0

            subjects[subject] += session["hours"]

        average = total_hours / len(data)

        most_subject = max(
            subjects,
            key=subjects.get
        )

        dates = []

        for session in data:

            dates.append(session["date"])

        dates = [
            datetime.strptime(date, "%Y-%m-%d")
            for date in dates
        ]

        dates.sort()

        streak = 1
        max_streak = 1

        for i in range(1, len(dates)):

            difference = dates[i] - dates[i - 1]

            if difference.days == 1:

                streak += 1

            elif difference.days == 0:

                continue

            else:

                streak = 1

            if streak > max_streak:

                max_streak = streak

        print("\n============== Analyze ===================")
        print(f"Total Hours: {total_hours}")
        print(f"Average Hours: {average:.1f}")
        print(f"Most Studied Subject: {most_subject}")
        print(f"Study Streak: {max_streak} days 🔥")
def search_sessions():

    search = input("Enter subject to search: ")

    data = load_sessions()

    found = False

    print("\n===== Search Results =====")

    for session in data:

        if search.lower() in session.get("subject", "").lower():

            print("\n----------------")
            print(f"Subject: {session['subject']}")
            print(f"Hours: {session['hours']}")
            print(f"Date: {session['date']}")
            print(f"Mood: {session['mood']}")

            found = True

    if not found:

        print("No session found.")
def delete_session():

    data = load_sessions()

    if len(data) == 0:

        print("No study sessions found!")

    else:

        print("\n===== Delete Session =====")

        for i, session in enumerate(data, start=1):

            print(
                f"{i}. {session['subject']} | {session['hours']} hours | {session['date']}"
            )
        number =int(input("Enter session number:"))
        index=number-1
        if index>=0 and index<len(data):
                deleted_session=data.pop(index)
                save_sessions(data)
                print (f"Deleted :   {deleted_session['subject']}   |   {deleted_session['hours']}   |   {deleted_session['date']}")
        else :
                print('Invalid number!')
    
while True:

    print(f"\n===== AI Study Assistant | {name} =====")
    show_main()
    choice = input("Enter your choice: ")



    # =====================
    # Add Study Session
    # =====================
    if choice == "1":
        add_study_session()

    # =====================
    # View Sessions
    # =====================

    elif choice == "2":
        view_study_sessions()


    # =====================
    # Add Goal
    # =====================

    elif choice == "3":

      add_goal()


    # =====================
    # View Goals
    # =====================

    elif choice == "4":
        view_goals()

    # =====================
    # Analyze Progress
    # =====================

    elif choice == "5":
        analyze_progress()
            

        
       
    #======================
    #search seasions
    #======================
    elif choice == "6":
        search_sessions()
    
    #======================
    #Delete session
    #======================
    elif choice=="7":
        delete_session()


    #bye==========bye
    elif choice == "8":

        print(
            f"\nGoodbye {name} 👋"
        )

        break

    else:

        print("Invalid choice!")