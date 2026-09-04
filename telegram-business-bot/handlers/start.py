from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from keyboards.confirmation import confirmation_keyboard
from keyboards.main_menu import main_menu_keyboard
from states.order import OrderStates
from database.database import save_order

router = Router()


@router.message(Command("start"))
async def menu_handler(message: Message, state: FSMContext) -> None:
    await state.clear()

    await message.answer("Here is the main menu:", reply_markup=main_menu_keyboard)


@router.callback_query(F.data == "create_order")
async def create_order_handler(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    await callback_query.answer()

    await state.set_state(OrderStates.waiting_for_order_details)

    if isinstance(callback_query.message, Message):
        await callback_query.message.answer("Please provide the order details.")


@router.message(OrderStates.waiting_for_order_details, F.text)
async def order_details_handler(message: Message, state: FSMContext) -> None:
    order_details = message.text

    await state.update_data(order_details=order_details)

    await state.set_state(OrderStates.waiting_for_confirmation)

    await message.answer(
        f"Order Summary:\n\n"
        f"{order_details}\n\n"
        f"Would you like to confirm this order?",
        reply_markup=confirmation_keyboard,
    )


@router.message(OrderStates.waiting_for_order_details)
async def invalid_order_details_handler(message: Message) -> None:
    await message.answer("Please send the order details as text.")


@router.callback_query(OrderStates.waiting_for_confirmation, F.data == "confirm_order")
async def confirm_order_handler(
    callback_query: CallbackQuery, state: FSMContext
) -> None:

    await callback_query.answer()

    data = await state.get_data()
    order_details = data.get("order_details")

    save_order(
        user_id=callback_query.from_user.id,
        order_details=order_details,
        status="confirmed",
    )

    if isinstance(callback_query.message, Message):
        await callback_query.message.edit_reply_markup(reply_markup=None)

        await callback_query.message.answer(
            f" Your order has been confirmed.\n\n" f"Order details:\n{order_details}"
        )

    await state.clear()


@router.callback_query(OrderStates.waiting_for_confirmation, F.data == "cancel_order")
async def cancel_order_handler(
    callback_query: CallbackQuery, state: FSMContext
) -> None:
    await callback_query.answer()

    if isinstance(callback_query.message, Message):
        await callback_query.message.edit_reply_markup(reply_markup=None)

        await callback_query.message.answer(
            " Your order has been cancelled.", reply_markup=main_menu_keyboard
        )

    await state.clear()
