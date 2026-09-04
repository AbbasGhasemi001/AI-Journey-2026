import sqlite3


connection = sqlite3.connect('bot.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    order_details TEXT NOT NULL,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()

def save_order(user_id, order_details, status):
    cursor.execute("""
    INSERT INTO orders (user_id, order_details, status)
    VALUES (?, ?, ?)
    """, (user_id, order_details, status))
    connection.commit()