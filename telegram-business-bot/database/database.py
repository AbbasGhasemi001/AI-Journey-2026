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

def get_user_orders(user_id):
    cursor.execute(
        """
        SELECT id, order_details, status, created_at
        FROM orders
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    orders = cursor.fetchall()

    return orders

cursor.execute("""
CREATE TABLE IF NOT EXISTS support_tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

connection.commit()


def save_support_ticket(user_id, message, status):
    cursor.execute("""
    INSERT INTO support_tickets (user_id, message, status)
    VALUES (?, ?, ?)
    """, (user_id, message, status))
    connection.commit()
