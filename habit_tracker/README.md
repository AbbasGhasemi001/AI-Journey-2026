# Habit Tracker

A simple command-line Habit Tracker built with Python and Object-Oriented Programming.

This project allows users to create habits, track daily progress, view habit history, delete habits, and analyze overall habit performance using JSON file storage.

---

## Features

- Add a new habit
- View all habits
- Mark a habit as done for today
- Prevent duplicate daily records
- View habit history
- Delete a habit
- Analyze habit progress
- Store data in a JSON file
- Handle invalid inputs

---

## Technologies Used

- Python
- Object-Oriented Programming
- JSON
- datetime module
- File handling
- Error handling with try/except

---

## Project Structure

```text
habit_tracker/
│
├── habit_tracker.py
├── habits.json
└── README.md
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/AbbasGhasemi001/AI-Journey-2026.git
```

Go to the project folder:

```bash
cd AI-Journey-2026
```

Run the program:

```bash
python habit_tracker.py
```

---

## Menu

```text
===== Habit Tracker =====
1. Add Habit
2. View Habits
3. Mark Habit as Done
4. View Habit History
5. Delete Habit
6. Analyze Habits
7. Exit
```

---

## Example Habit Data

```json
{
    "name": "programming",
    "created_at": "2026-07-08",
    "history": [
        "2026-07-08"
    ]
}
```

---

## What I Learned

In this project, I practiced:

- Creating classes in Python
- Using `self`
- Defining methods inside a class
- Working with JSON files
- Reading and writing data to a file
- Using lists and dictionaries
- Handling user input
- Using `try/except`
- Preventing duplicate records
- Analyzing data with loops
- Structuring a CLI project

---

## Future Improvements

- Add current streak calculation
- Add longest streak calculation
- Add weekly habit summary
- Add edit habit feature
- Refactor the project into multiple classes
- Create a separate `Habit` class
- Split the project into multiple files
- Add data visualization
- Add a GUI version

---

## Status

Habit Tracker v1 is complete.

This project is part of my Python and AI learning journey.