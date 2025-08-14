import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Bot token (Render-এ Environment Variable হিসেবে BOT_TOKEN সেট করবেন)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# /start কমান্ড
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Free Fire Tournament Bot-এ স্বাগতম!\n\n/use /register <Your Name> দিয়ে রেজিস্টার করুন।")

# /register কমান্ড
async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("❌ ব্যবহার: /register <Your Name>")
    else:
        name = " ".join(context.args)
        await update.message.reply_text(f"✅ {name} সফলভাবে রেজিস্টার হয়েছে!")

# Default message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ℹ️ দয়া করে /register বা /start কমান্ড ব্যবহার করুন।")

if __name__ == '__main__':
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN পাওয়া যায়নি। দয়া করে Environment Variable সেট করুন।")
        exit(1)

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("register", register))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ Bot started...")
    app.run_polling()