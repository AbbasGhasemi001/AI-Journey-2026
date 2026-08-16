import os
import random
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Telegram Bot Token is missing in environment variables.")

bot = telebot.TeleBot(TOKEN)

LOCAL_LOVE_MESSAGES = [
    "❤️ عباس تو رو خیلی دوست داره!",
    "💖 عشق من، تو بهترین چیزی هستی که برام اتفاق افتاده.",
    "😍 هر لحظه با تو بودن، یه دنیای جدیده.",
    "🌹 تو مثل یه گل زیبا در قلب من شکوفا شدی.",
    "💌 هر روز که می‌گذره، عشقم بهت بیشتر می‌شه.",
    "💞 تو دلیل لبخند منی و همیشه در قلبم خواهی بود.",
    "💘 تو مثل یه ستاره در شب تاریک من می‌درخشی.",
    "💝 تو مثل یه نور در تاریکی من می‌باشی.",
    "💗 تو مثل یه آتش در قلب من می‌سوزی.",
    "💓 تو همه کس و تنها دلیل زندگی منی جوجوی عباس",
]


@bot.message_handler(commands=["start"])
def handle_start(message):
    markup = InlineKeyboardMarkup()
    btn_local_love = InlineKeyboardButton(
        "حرف دل عباست", callback_data="btn_local_love"
    )
    btn_scrape_love = InlineKeyboardButton(
        "حرف دل رندوم", callback_data="btn_scrape_love"
    )

    markup.add(btn_local_love)
    markup.add(btn_scrape_love)

    welcome_text = "دوست داری امروز چطور سوپرایز بشی دین و دنیای عباس 🥰"
    bot.reply_to(message, welcome_text, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "btn_local_love":
        random_message = random.choice(LOCAL_LOVE_MESSAGES)
        bot.send_message(call.message.chat.id, random_message)

    elif call.data == "btn_scrape_love":
        wait_msg = bot.send_message(
            call.message.chat.id,
            " یه لحظه طول میکشه تا یه حرف دل رندوم برات پیدا کنم... ⏳",
        )

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
                    bot.edit_message_text(
                        formatted_response, call.message.chat.id, wait_msg.message_id
                    )
                else:
                    bot.edit_message_text(
                        "❌ محتوایی در صفحه یافت نشد.",
                        call.message.chat.id,
                        wait_msg.message_id,
                    )

                browser.close()

        except Exception as e:
            logging.error(f"Scraping failed: {e}")
            bot.edit_message_text(
                "❌ ارتباط با سرور مقصد برقرار نشد.",
                call.message.chat.id,
                wait_msg.message_id,
            )


if __name__ == "__main__":
    logging.info("Bot service is starting...")
    bot.infinity_polling()
