Markdown
# Book Library Manager 📚

A modular command-line application built with **Python** and **SQLite** to manage a personal book collection. This project demonstrates practical database integration and robust error handling.

## 🚀 Features

- **CRUD Operations:** Add, View (alphabetically sorted), Update, and Delete books.
- **Search Functionality:** Find books by partial title or author matches using SQL `LIKE`.
- **Data Persistence:** Uses an SQLite database (`library.db`) to store records permanently.
- **Input Validation:** Prevents empty entries, handles non-numeric IDs, and manages missing records gracefully.
- **Automated Database Creation:** Automatically generates the database and tables upon first run.

## 🛠️ Technologies Used

- **Python 3**
- **SQLite3** (Built-in standard library)

## 💻 How to Run

1. Navigate to the project directory in your terminal.
2. Run the script:
   ```bash
   python main.py
   ```
Follow the interactive on-screen menu!

📂 Project Structure
main.py: The core script containing the application logic, menu, and SQLite queries.

library.db: The local database file (automatically ignored via .gitignore to keep data private).