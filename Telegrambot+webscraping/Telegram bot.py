import os
import random
import logging
import telebot
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# ============================
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Telegram Bot Token is missing in environment variables.")

bot = telebot.TeleBot(TOKEN)

# ======================================

LOCAL_LOVE_MESSAGES = [
    "❤️ عباس تو رو خیلی دوست داره!",
    "💖 عشق من، تو بهترین چیزی هستی که برام اتفاق افتاده.",
    "😍 هر لحظه با تو بودن، یه دنیای جدیده.",
    "🌹 تو مثل یه گل زیبا در قلب من شکوفا شدی.",
    "💌 هر روز که می‌گذره، عشقم بهت بیشتر می‌شه.",
]


@bot.message_handler(commands=["start"])
def handle_start(message):
    welcome_text = (
        "سلام نفس عباس خوبی! "
        "برای اینکه بگم چقدر عباس دوستت داره دستور /love "
        "و برای یه جمله رندوم قشنگ /love_scrape رو بزن ❤️"
    )
    bot.reply_to(message, welcome_text)


@bot.message_handler(commands=["love"])
def handle_local_love(message):
    selected_message = random.choice(LOCAL_LOVE_MESSAGES)
    bot.reply_to(message, selected_message)


@bot.message_handler(commands=["love_scrape"])
def handle_web_scrape_love(message):
    bot.reply_to(message, "❤️ در حال استخراج...")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, channel="chrome")
            page = browser.new_page()

            page.goto("https://quotes.toscrape.com/tag/love/")

            quote_containers = page.locator(".quote").all()

            if quote_containers:
                target_quote = random.choice(quote_containers)

                quote_text = target_quote.locator(".text").inner_text()
                quote_author = target_quote.locator(".author").inner_text()

                formatted_response = f"{quote_text}\n\n👤 {quote_author} ❤️"
                bot.reply_to(message, formatted_response)
            else:
                bot.reply_to(message, "❌ محتوایی در صفحه یافت نشد.")

            browser.close()

    except Exception as e:
        logging.error(f"Scraping failed: {e}")
        bot.reply_to(
            message, "❌ ارتباط با سرور مقصد برقرار نشد. لطفاً بعداً تلاش کنید."
        )


if __name__ == "__main__":
    logging.info("Bot service is starting...")
    bot.infinity_polling()
