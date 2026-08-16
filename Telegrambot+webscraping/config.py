import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TELEGRAM_BUSINESS_TOKEN")
ADMIN_ID = os.getenv("ADMIN_CHAT_ID")

if not TOKEN:
    raise ValueError("Telegram Bot Token is missing in environment variables.")

MENU_TEXTS = {
    "welcome": "سلام مهندس! به رباتِ پورتفولیو خوش اومدی 🚀",
    "choose_action": "لطفاً یک گزینه رو انتخاب کن:",
}
