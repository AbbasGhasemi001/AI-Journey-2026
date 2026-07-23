import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "library.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()


def view_books():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    connection.close()

    if not books:
        print("No books found.")
    else:
        for book in books:
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]}")


def add_book(title, author):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

    connection.commit()
    connection.close()

    print("Book added successfully!")


def delete_book(book_id):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    connection.commit()

    if cursor.rowcount == 0:
        print("Book not found.")
    else:
        print("Book deleted successfully!")

    connection.close()


while True:
    print("\n--- Book Library Manager ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Delete Books")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()

        if title and author:
            add_book(title, author)
        else:
            print("Title and author cannot be empty.")

    elif choice == "2":
        view_books()

    elif choice == "3":
        delete_book()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
