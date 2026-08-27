import os 
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("Bot_token_prototype_v2")

if not BOT_TOKEN:
    raise ValueError("Bot token is not set in the environment variables.")
