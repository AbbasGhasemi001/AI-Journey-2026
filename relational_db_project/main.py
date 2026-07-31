import sqlite3
from pathlib import Path 

#------------------------

database_path = Path(__file__).parent / "shop.db"
connection = sqlite3.connect(database_path)
cursor = connection.cursor() 

#------------------------

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE)''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    foreign key (user_id) references users(id))''')


cursor.execute('''
SELECT users.username, SUM(products.price)
FROM products
JOIN users ON products.user_id = users.id
GROUP BY users.username
''')

results = cursor.fetchall()

for row in results:
    print(f"User: {row[0]}, Product: {row[1]}, Price: {row[2]}")



connection.commit()
cursor.close()
