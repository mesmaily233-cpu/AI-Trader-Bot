from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN ="8845063172:AAEgF5-sMbMl9iOXlZiFhxTZLrBXRe_T8UY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات تریدر هوش مصنوعی آماده است ✅")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
