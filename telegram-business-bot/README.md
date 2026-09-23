# Telegram Business Automation Bot V2 🤖

A modular, production-ready Telegram bot designed for business automation, order management, and customer support. 

## 🚀 Features
- **State Machine (FSM):** Multi-step order registration without data collision.
- **Role-Based Access Control (RBAC):** Isolated and secure Admin Panel.
- **Persistent Storage:** SQLite integration for tracking orders and support tickets.
- **External API Consumer:** Real-time data fetching with timeout handling.
- **Modular Architecture:** Clean separation of concerns (`handlers`, `database`, `config`).

## 🛠️ Tech Stack
- **Language:** Python 3.13
- **Framework:** aiogram 3.x
- **Database:** SQLite3
- **Environment:** python-dotenv

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/telegram-business-bot.git](https://github.com/YourUsername/telegram-business-bot.git)
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   Create a `.env` file in the root directory:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ADMIN_ID=your_numeric_telegram_id_here
   ```

5. Run the bot:
   ```bash
   python main.py
   ```

## 🛡️ Security Note
This project utilizes environment variables (`.env`) to protect sensitive credentials. The `.gitignore` is properly configured to prevent pushing API keys or local database files to the remote repository.