from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup    


main_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Create order", callback_data="create_order")],
        [InlineKeyboardButton(text="My orders", callback_data="my_orders")],
        [InlineKeyboardButton(text="Support", callback_data="support")],
    ]
)