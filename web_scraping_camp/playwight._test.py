import sqlite3
import time
from playwright.sync_api import sync_playwright

# ===============================================

print("ready data base")
conn = sqlite3.connect("web_scraping_camp.db")
cursor = conn.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        author TEXT
    )
""")
cursor.execute("delete from products")
conn.commit()
# ===============================================
# script part
# ===============================================
with sync_playwright() as p:
    print("start browser")
    browser = p.chromium.launch(headless=False, channel="chrome")
    page = browser.new_page()
    print("go to page")
    page.goto("http://quotes.toscrape.com/scroll")
    time.sleep(5)

    for i in range(10):
        print(f"scroll {i}")
        page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(2)

    print("get data")
    quotes = page.locator(".quote").all
    saved = 0
    for element in quotes:
        text = element.locator(".text").inner_text()
        author = element.locator(".author").inner_text()
        cursor.execute(
            "INSERT INTO products (text, author) VALUES (?, ?)", (text, author)
        )
        saved += 1

    conn.commit()
    print(f"saved {saved} records")
    browser.close()

conn.close()

print("done")
