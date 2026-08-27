import asyncio
from aiogram import Dispatcher, Bot
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)
    
print("Bot is running333")

if __name__ == "__main__":
    asyncio.run(main())

print("Bot is running...")