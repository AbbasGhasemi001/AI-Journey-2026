from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup    


confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Confirm",
                callback_data="confirm_order"
            ),
            InlineKeyboardButton(
                text="Cancel",
                callback_data="cancel_order"
            )
        ]
    ]
)