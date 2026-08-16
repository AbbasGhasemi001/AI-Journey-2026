import sqlite3


#=========================
def init_db():
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT NOT NULL,
            price INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def add_order(product, price):
    conn = sqlite3.connect("orders.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (product, price) VALUES (?, ?)", (product, price)
    )
    conn.commit()
    conn.close()


def get_orders():
    conn =sqlite3.connect("orders.db")
    cursor = conn.cursor()  
    cursor.execute("SELECT product, price FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders