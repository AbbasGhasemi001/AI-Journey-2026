from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from keyboards.main_menu import main_menu_keyboard


router = Router()


@router.message(Command("start"))
async def menu_handler(message: Message) -> None:
    await message.answer(
        "Here is the main menu:",
        reply_markup=main_menu_keyboard
    )
