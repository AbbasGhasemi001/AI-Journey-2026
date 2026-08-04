import requests
from bs4 import BeautifulSoup
import csv

# -----------------------------


with open("scraped_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Team name", "Year", "Wins"])

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

            writer.writerow([team_name, year, wins])

    print("Scraping completed. Data saved to scraped_data.csv.")
