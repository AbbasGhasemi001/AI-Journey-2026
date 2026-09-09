from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


admin_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=" View Orders",
                callback_data="admin_view_orders"
            )
        ],
        [
            InlineKeyboardButton(
                text=" View Support Tickets",
                callback_data="admin_view_tickets"
            )
        ]
    ]
)
