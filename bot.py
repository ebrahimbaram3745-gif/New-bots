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

TOKEN = "8844046661:AAEiVxd8MAEJVhN9wYIXM_AXUExiDcQRucE"

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
