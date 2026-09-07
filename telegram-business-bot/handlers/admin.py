from aiogram import  Router
from aiogram.filters import Command 
from aiogram.types import Message

from config import ADMIN_ID

router = Router()

@router.message(Command("admin"))
async def admin_handler(message: Message) -> None:
    if message.from_user.id != ADMIN_ID:
        await message.answer("Access denied.")
        return

    await message.answer(
        "Access granted. You are the admin of this bot."
    )

@router.message(Command("id"))
async def get_id_handler(message: Message) -> None:
    if message.from_user:
        await message.answer(
            f"Your Telegram ID is: {message.from_user.id}"
        )