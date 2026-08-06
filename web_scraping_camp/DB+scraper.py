import requests
from bs4 import BeautifulSoup
import sqlite3

# sql-----------------------------
conn = sqlite3.connect("scraped_data.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS teams (  
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT,
    year TEXT,
    wins TEXT)""")

# scraper -----------------------------
for page_number in range(1, 6):
    url = f"https://www.scrapethissite.com/pages/forms/?page_num={page_number}"
    print(f"Scraping page {page_number}...")

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    rows = soup.find_all("tr", class_="team")

    for row in rows:
        team_name = row.find("td", class_="name").text.strip()
        year = row.find("td", class_="year").text.strip()
        wins = row.find("td", class_="wins").text.strip()

        cursor.execute(
            """
            INSERT INTO teams (team_name, year, wins) VALUES (?, ?, ?)""",
            (team_name, year, wins),
        )

conn.commit()
conn.close()

print("Scraping completed. Data saved to scraped_data.db. good job!")
