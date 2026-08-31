import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot dari HP siap mengirim foto dan video.")

async def kirim_media(update: Update, context: ContextTypes.DEFAULT_TYPE):
    foto_url = "https://picsum.photos/800/600"
    video_url = "https://www.w3schools.com/html/mov_bbb.mp4"
    await update.message.reply_photo(photo=foto_url, caption="Foto dari bot!")
    await update.message.reply_video(video=video_url, caption="Video dari bot!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("media", kirim_media))
    app.run_polling()

if __name__ == "__main__":
    main()
