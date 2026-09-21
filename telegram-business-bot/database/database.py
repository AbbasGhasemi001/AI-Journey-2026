import sqlite3

connection = sqlite3.connect("bot.db")
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
    cursor.execute(
        """
    INSERT INTO orders (user_id, order_details, status)
    VALUES (?, ?, ?)
    """,
        (user_id, order_details, status),
    )
    connection.commit()


def get_user_orders(user_id):
    cursor.execute(
        """
        SELECT id, order_details, status, created_at
        FROM orders
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,),
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
    cursor.execute(
        """
    INSERT INTO support_tickets (user_id, message, status)
    VALUES (?, ?, ?)
    """,
        (user_id, message, status),
    )
    connection.commit()


def get_all_orders():
    cursor.execute("""
        SELECT id, user_id, order_details, status, created_at
        FROM orders
        ORDER BY created_at DESC
        """)

    orders = cursor.fetchall()

    return orders

def get_all_support_tickets():
    cursor.execute(
        """
        SELECT id, user_id, message, status, created_at
        FROM support_tickets
        ORDER BY created_at DESC
        """
    )

    tickets = cursor.fetchall()

    return tickets


def get_order_by_id(order_id):
    """Get specific order by ID"""
    cursor.execute(
        """
        SELECT id, user_id, order_details, status, created_at
        FROM orders
        WHERE id = ?
        """,
        (order_id,)
    )
    return cursor.fetchone()


def get_ticket_by_id(ticket_id):
    """Get specific ticket by ID"""
    cursor.execute(
        """
        SELECT id, user_id, message, status, created_at
        FROM support_tickets
        WHERE id = ?
        """,
        (ticket_id,)
    )
    return cursor.fetchone()


def update_order_status(order_id, new_status):
    """Update order status by order_id"""
    cursor.execute(
        """
        UPDATE orders
        SET status = ?
        WHERE id = ?
        """,
        (new_status, order_id)
    )
    connection.commit()


def update_ticket_status(ticket_id, new_status):
    """Update support ticket status by ticket_id"""
    cursor.execute(
        """
        UPDATE support_tickets
        SET status = ?
        WHERE id = ?
        """,
        (new_status, ticket_id)
    )
    connection.commit()


def get_total_orders_count():
    cursor.execute("""
        SELECT COUNT(*)
        FROM orders
    """)
    return cursor.fetchone()[0]


def get_total_tickets_count():
    cursor.execute("""
        SELECT COUNT(*)
        FROM support_tickets
    """)
    return cursor.fetchone()[0]


def get_open_tickets_count():
    cursor.execute("""
        SELECT COUNT(*)
        FROM support_tickets
        WHERE status = 'open'
    """)
    return cursor.fetchone()[0]


def get_orders_by_status():
    cursor.execute("""
        SELECT status, COUNT(*)
        FROM orders
        GROUP BY status
    """)
    return cursor.fetchall()