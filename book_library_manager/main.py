import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "library.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
""")
cursor.execute("SELECT * FROM books")

books = cursor.fetchall()

for book in books:
    print(book)

connection.commit()
connection.close()

print("Books displayed successfully!")