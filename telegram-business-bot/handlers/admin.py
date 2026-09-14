from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from config import ADMIN_ID
from database.database import (
    get_all_orders,
    get_all_support_tickets,
    get_order_by_id,
    get_ticket_by_id,
    update_order_status,
    update_ticket_status,
)
from keyboards.admin import admin_keyboard
from keyboards.status import order_status_keyboard, ticket_status_keyboard

router = Router()


# =========================================================
# ADMIN PANEL
# =========================================================


@router.message(Command("admin"))
async def admin_handler(message: Message) -> None:

    if not message.from_user or message.from_user.id != ADMIN_ID:
        await message.answer("❌ Access denied.")
        return

    await message.answer(
        "🛠 Admin Panel\n\n" "Choose an option:", reply_markup=admin_keyboard
    )


# =========================================================
# VIEW ALL ORDERS
# =========================================================


@router.callback_query(F.data == "admin_view_orders")
async def admin_view_orders_handler(callback_query: CallbackQuery) -> None:

    await callback_query.answer()

    # Security check
    if callback_query.from_user.id != ADMIN_ID:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id, text="❌ Access denied."
        )
        return

    orders = get_all_orders()

    if not orders:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id, text="❌ No orders found."
        )
        return

    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f"📦 All Orders\n\nTotal: {len(orders)}",
    )

    for order in orders:

        order_id, user_id, order_details, status, created_at = order

        order_text = (
            f"📦 Order #{order_id}\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👤 User ID: {user_id}\n"
            f"📝 Details: {order_details}\n"
            f"🔔 Status: {status}\n"
            f"📅 Created at: {created_at}"
        )

        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id,
            text=order_text,
            reply_markup=order_status_keyboard(order_id)
        )


# =========================================================
# VIEW SUPPORT TICKETS
# =========================================================


@router.callback_query(F.data == "admin_view_tickets")
async def admin_view_tickets_handler(callback_query: CallbackQuery) -> None:

    await callback_query.answer()

    # Security check
    if callback_query.from_user.id != ADMIN_ID:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id, text="❌ Access denied."
        )
        return

    tickets = get_all_support_tickets()

    if not tickets:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id, text="❌ No support tickets found."
        )
        return

    await callback_query.bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f"🎫 Support Tickets\n\nTotal: {len(tickets)}",
    )

    for ticket in tickets:

        ticket_id, user_id, message, status, created_at = ticket

        ticket_text = (
            f"🎫 Ticket #{ticket_id}\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👤 User ID: {user_id}\n"
            f"💬 Message: {message}\n"
            f"🔔 Status: {status}\n"
            f"📅 Created at: {created_at}"
        )

        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id,
            text=ticket_text,
            reply_markup=ticket_status_keyboard(ticket_id)
        )


# =========================================================
# UPDATE ORDER STATUS
# =========================================================


@router.callback_query(F.data.startswith("update_order_status_"))
async def update_order_status_handler(callback_query: CallbackQuery) -> None:
    
    await callback_query.answer()
    
    # Security check
    if callback_query.from_user.id != ADMIN_ID:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id, text="❌ Access denied."
        )
        return
    
    try:
        # Parse callback_data: update_order_status_5_confirmed
        parts = callback_query.data.split("_")
        order_id = int(parts[3])
        new_status = parts[4]
        
        # Get current order
        order = get_order_by_id(order_id)
        
        if not order:
            await callback_query.bot.send_message(
                chat_id=callback_query.from_user.id, 
                text="❌ Order not found."
            )
            return
        
        # Update in database
        update_order_status(order_id, new_status)
        
        # Confirm to admin
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id,
            text=f"✅ Order #{order_id} status updated to: {new_status}"
        )
    
    except Exception as e:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id,
            text=f"❌ Error updating order: {str(e)}"
        )


# =========================================================
# UPDATE TICKET STATUS
# =========================================================


@router.callback_query(F.data.startswith("update_ticket_status_"))
async def update_ticket_status_handler(callback_query: CallbackQuery) -> None:
    
    await callback_query.answer()
    
    # Security check
    if callback_query.from_user.id != ADMIN_ID:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id, text="❌ Access denied."
        )
        return
    
    try:
        # Parse callback_data: update_ticket_status_3_closed
        parts = callback_query.data.split("_")
        ticket_id = int(parts[3])
        new_status = parts[4]
        
        # Get current ticket
        ticket = get_ticket_by_id(ticket_id)
        
        if not ticket:
            await callback_query.bot.send_message(
                chat_id=callback_query.from_user.id, 
                text="❌ Ticket not found."
            )
            return
        
        # Update in database
        update_ticket_status(ticket_id, new_status)
        
        # Confirm to admin
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id,
            text=f"✅ Ticket #{ticket_id} status updated to: {new_status}"
        )
    
    except Exception as e:
        await callback_query.bot.send_message(
            chat_id=callback_query.from_user.id,
            text=f"❌ Error updating ticket: {str(e)}"
        )
