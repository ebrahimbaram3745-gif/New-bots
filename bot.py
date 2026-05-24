import os
from threading import Thread
from flask import Flask

from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

TOKEN = os.getenv("TOKEN")

# ---------- WEB APP BUTTON ----------

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                text="📋 منو",
                web_app=WebAppInfo(
                    url="https://6a13329df1dc50457d96c0a3--chic-queijadas-d84af7.netlify.app/"
                )
            )
        ]
    ],
    resize_keyboard=True
)

# ---------- START COMMAND ----------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🌹 خوش آمدید",
        reply_markup=menu
    )

# ---------- TELEGRAM BOT ----------

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

# ---------- FLASK SERVER ----------

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running"

def run():
    flask_app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

# ---------- START BOT ----------

print("Bot Started...")

app.run_polling()
