import logging
import telebot
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN, MENU_TEXTS
from database import init_db, add_order, get_orders

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
bot = telebot.TeleBot(TOKEN)

user_data = {}


@bot.message_handler(commands=["start"])
def handle_start(message):
    markup = InlineKeyboardMarkup()

    btn_form = InlineKeyboardButton("📝 ثبت سفارش جدید", callback_data="btn_form")
    btn_db = InlineKeyboardButton("💾 تست دیتابیس", callback_data="btn_db")
    btn_api = InlineKeyboardButton("🌐 قیمت بیتکوین :( ", callback_data="btn_api")

    markup.add(btn_form)
    markup.row(btn_db, btn_api)

    bot.reply_to(message, MENU_TEXTS["welcome"], reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    chat_id = call.message.chat.id

    if call.data == "btn_form":
        bot.answer_callback_query(call.id)
        msg = bot.send_message(
            chat_id,
            "📦 بسیار عالی! لطفاً **نام کالا** را وارد کنید:",
            parse_mode="Markdown",
        )
        bot.register_next_step_handler(msg, process_product_name_step)

    elif call.data == "btn_db":
        bot.answer_callback_query(call.id)
        orders = get_orders()

        if not orders:
            bot.send_message(chat_id, "📭 دیتابیس خالی است! سفارشی ثبت نشده.")
            return

        response_text = "📊 **لیست سفارشات ثبت شده:**\n\n"
        for idx, (product, price) in enumerate(orders, 1):
            response_text += f"{idx}. 🛒 **{product}** ➖ 💰 {price} تومان\n"

        bot.send_message(chat_id, response_text, parse_mode="Markdown")

    elif call.data == "btn_api":
        bot.answer_callback_query(call.id, "در حال اتصال به سرور جهانی Binance...")

        try:

            url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"

            response = requests.get(url, timeout=5)
            data = response.json()

            # استخراج قیمت بیت‌کوین از بایننس
            if "price" in data:
                raw_price = float(data["price"])
                price_formatted = f"{raw_price:,.2f}"  # دو رقم اعشار و جداکننده هزارگان

                api_response = f"🟠 **قیمت لحظه‌ای بیت‌کوین (BTC)**\n\n💵 {price_formatted} دلار\n\n💡 منبع: هسته معاملات Binance"

                bot.send_message(chat_id, api_response, parse_mode="Markdown")
            else:
                bot.send_message(chat_id, "❌ ساختار دیتای صرافی تغییر کرده است.")

        except requests.exceptions.Timeout:
            bot.send_message(chat_id, "❌ زمان اتصال به سرور طولانی شد (Timeout).")
        except Exception as e:
            logging.error(f"Error fetching API data: {e}")
            bot.send_message(
                chat_id, "❌ ارتباط با سرور بایننس برقرار نشد. اینترنت را چک کنید."
            )


def process_product_name_step(message):
    chat_id = message.chat.id
    product_name = message.text

    user_data[chat_id] = {"product": product_name}

    msg = bot.send_message(
        chat_id,
        f"✅ کالای «{product_name}» ثبت شد.\nحالا لطفاً **قیمت کالا** را (فقط به صورت عدد و به تومان) وارد کنید:",
        parse_mode="Markdown",
    )
    bot.register_next_step_handler(msg, process_price_step)


def process_price_step(message):
    chat_id = message.chat.id
    price = message.text

    if not price.isdigit():
        msg = bot.send_message(
            chat_id, "❌ لطفاً قیمت را فقط به صورت عدد وارد کنید. دوباره تلاش کنید:"
        )
        bot.register_next_step_handler(msg, process_price_step)
        return

    user_data[chat_id]["price"] = price
    product = user_data[chat_id]["product"]

    add_order(product, int(price))

    invoice = (
        "🧾 **فاکتور نهایی شما صادر و در سیستم ثبت شد**\n\n"
        f"🔸 **محصول:** {product}\n"
        f"🔸 **مبلغ:** {price} تومان\n\n"
        "سپاس از ثبت اطلاعات. 🙏"
    )

    bot.send_message(chat_id, invoice, parse_mode="Markdown")

    if chat_id in user_data:
        del user_data[chat_id]


if __name__ == "__main__":
    logging.info("Initializing Database...")
    init_db()
    logging.info("Advanced Portfolio Bot is starting...")
    bot.infinity_polling()
