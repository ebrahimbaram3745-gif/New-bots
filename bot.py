import os
from telegram import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import Updater, CommandHandler

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

def start(update, context):
    update.message.reply_text(
        "🌹 خوش آمدید",
        reply_markup=menu
    )

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

print("Bot Started...")

updater.start_polling()
updater.idle()
