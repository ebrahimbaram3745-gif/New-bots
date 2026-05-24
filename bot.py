import os

from flask import Flask
from threading import Thread

app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is running"

def run():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

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

import os
TOKEN = os.getenv("TOKEN")

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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "خوش آمدید 🌹",
        reply_markup=menu
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")

app.run_polling()
