from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from database.database import save_support_ticket
from keyboards.main_menu import main_menu_keyboard
from states.support import SupportStates


router = Router()


@router.callback_query(F.data == "support")
async def support_handler(
    callback_query: CallbackQuery,
    state: FSMContext
) -> None:
    await callback_query.answer()

    await state.set_state(
        SupportStates.waiting_for_support_message
    )

    if isinstance(callback_query.message, Message):
        await callback_query.message.answer(
            "Please send your support message. "
            "Our team will get back to you shortly."
        )


@router.message(
    SupportStates.waiting_for_support_message,
    F.text
)
async def support_message_handler(
    message: Message,
    state: FSMContext
) -> None:
    support_message = message.text

    save_support_ticket(
        user_id=message.from_user.id,
        message=support_message,
        status="open",
    )

    await message.answer(
        "Thank you for your message. "
        "Our support team will get back to you shortly.",
        reply_markup=main_menu_keyboard,
    )

    await state.clear()