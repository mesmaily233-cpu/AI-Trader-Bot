from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8845063172:AAEgF5-sMbMl9iOXlZiFhxTZLrBXRe_T8UY"

app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running ✅"

def run_web():
    app_web.run(host="0.0.0.0", port=10000)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات تریدر هوش مصنوعی آماده است ✅")

def run_bot():
    bot_app = ApplicationBuilder().token(TOKEN).build()
    bot_app.add_handler(CommandHandler("start", start))
    bot_app.run_polling()

Thread(target=run_web).start()
run_bot()
