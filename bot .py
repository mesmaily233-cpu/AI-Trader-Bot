import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import pandas as pd
import ta

TOKEN = "8845063172:AAEgF5-sMbMl9iOXlZiFhxTZLrBXRe_T8UY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 ربات تحلیل‌گر تریدر آماده است\n\n"
        "/price - قیمت بیت‌کوین\n"
        "/analyze - تحلیل بازار"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()

    await update.message.reply_text(
        f"₿ قیمت BTC:\n{data['price']} USDT"
    )


async def analyze(update: Update, context: ContextTypes.DEFAULT_TYPE):

    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=100"
    data = requests.get(url).json()

    close = [float(x[4]) for x in data]

    df = pd.DataFrame(close, columns=["close"])

    rsi = ta.momentum.RSIIndicator(
        df["close"], window=14
    ).rsi().iloc[-1]

    if rsi < 30:
        signal = "🟢 احتمال برگشت و بررسی خرید"
    elif rsi > 70:
        signal = "🔴 احتمال اصلاح و بررسی فروش"
    else:
        signal = "🟡 وضعیت خنثی"

    await update.message.reply_text(
        f"📊 تحلیل BTC\n\n"
        f"RSI: {round(rsi,2)}\n"
        f"{signal}"
    )


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("price", price))
app.add_handler(CommandHandler("analyze", analyze))

app.run_polling()
