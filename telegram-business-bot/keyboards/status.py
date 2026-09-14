from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def order_status_keyboard(order_id):
    """Status keyboard for order - includes order_id in callback"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✅ Confirmed",
                    callback_data=f"update_order_status_{order_id}_confirmed"
                ),
                InlineKeyboardButton(
                    text="⏳ Processing",
                    callback_data=f"update_order_status_{order_id}_processing"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="✔️ Completed",
                    callback_data=f"update_order_status_{order_id}_completed"
                ),
                InlineKeyboardButton(
                    text="❌ Cancelled",
                    callback_data=f"update_order_status_{order_id}_cancelled"
                ),
            ],
        ]
    )


def ticket_status_keyboard(ticket_id):
    """Status keyboard for ticket - includes ticket_id in callback"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🟡 Open",
                    callback_data=f"update_ticket_status_{ticket_id}_open"
                ),
                InlineKeyboardButton(
                    text="🔵 In Progress",
                    callback_data=f"update_ticket_status_{ticket_id}_in_progress"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🟢 Closed",
                    callback_data=f"update_ticket_status_{ticket_id}_closed"
                ),
            ],
        ]
    )
