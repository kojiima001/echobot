from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
import logging
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Enable logging to debug any issues
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Define the function to handle incoming messages
async def echo(update: Update, context):
    # Send back the same message received
    await update.message.reply_text(update.message.text)

# Define a start command to welcome users
async def start(update: Update, context):
    await update.message.reply_text("Hello! I am an Echo Bot. Send me any message, and I'll echo it back!")


if __name__ == "__main__":
    # Get the bot token from the .env file
    bot_token = os.getenv("BOT_TOKEN")

    if not bot_token:
        raise ValueError("Bot token not found. Please set BOT_TOKEN in your .env file.")

    # Create the application
    app = ApplicationBuilder().token(bot_token).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Bot is running...")
    # Start the bot
    app.run_polling()
