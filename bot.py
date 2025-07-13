import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Ətraf dəyişənlərini oxuyur (Replit-də Tools > Secrets vasitəsilə əlavə olunmalıdır)
TOKEN = os.getenv("BOT_TOKEN")
SECRET_PASSWORD = os.getenv("BOT_PASSWORD")
GROUP_LINK = os.getenv("GROUP_LINK")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 Xoş gəlmisiniz! Şifrəni daxil edin:")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text.strip() == SECRET_PASSWORD:
        await update.message.reply_text(f"✅ Şifrə doğrudur!\n🔗 {GROUP_LINK}")
    else:
        await update.message.reply_text("❌ Şifrə yalnışdır. Yenidən yoxlayın.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("🤖 Bot polling başladı...")
    app.run_polling()
