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

connection.commit()
connection.close()


def view_books():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books ORDER BY title ASC LIMIT 3")
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


def update_book(book_id, new_title, new_author):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE books SET title = ?, author = ? WHERE id = ?",
        (new_title, new_author, book_id),
    )

    connection.commit()
    updated_rows = cursor.rowcount
    connection.close()

    if updated_rows == 0:
        print("Book not found.")
    else:
        print("Book updated successfully!")


def search_books(keyword):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM books
        WHERE title LIKE ? OR author LIKE ?
        """,
        (f"%{keyword}%", f"%{keyword}%"),
    )

    books = cursor.fetchall()
    connection.close()

    if not books:
        print("No matching books found.")
    else:
        for book in books:
            print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]}")


def delete_book(book_id):
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    connection.commit()
    deleted_rows = cursor.rowcount
    connection.close()

    if deleted_rows == 0:
        print("Book not found.")
    else:
        print("Book deleted successfully!")


def count_books():
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    total = cursor.fetchone()[0]

    connection.close()

    print(f"Total books: {total}")


while True:
    print("\n--- Book Library Manager ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Delete Book")
    print("5. Search Books")
    print("6. Count Books")
    print("7. Exit")

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
        book_id = input("Enter book ID: ").strip()

        if book_id.isdigit():
            new_title = input("Enter new title: ").strip()
            new_author = input("Enter new author: ").strip()

            if new_title and new_author:
                update_book(int(book_id), new_title, new_author)
            else:
                print("Title and author cannot be empty.")
        else:
            print("ID must be a number.")

    elif choice == "4":
        book_id = input("Enter book ID: ").strip()

        if book_id.isdigit():
            delete_book(int(book_id))
        else:
            print("ID must be a number.")
    elif choice == "5":
        keyword = input("Enter title or author: ").strip()

        if keyword:
            search_books(keyword)
        else:
            print("Search text cannot be empty.")

    elif choice == "6":
        count_books()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
