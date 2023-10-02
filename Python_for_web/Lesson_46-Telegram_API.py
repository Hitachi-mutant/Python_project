'''Home work for the lesson 46'''

# Start a chat with BotFather and send the command /newbot
# Create a new Telegram channel by tapping the "New Channel" in the Telegram app.
# Give channel a name
# To launch the bot use /start

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_BOT_TOKEN' with the actual token you obtained from BotFather
BOT_TOKEN = 'khUY798GIUFEG2hhsdjo68'
CHANNEL_ID = '@test_telegram_channel'  # Replace with your channel username or chat ID

def start(update, text_content):
    update.message.reply_text('Bot started. Send me your notes.')

def forward_note(update, text_content): 
    message_text = update.message.text
    text_content.bot.send_message(chat_id=CHANNEL_ID, text=message_text)

def main():
    my_updater = Updater(token=BOT_TOKEN, use_context=True)
    dp = my_updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, forward_note))

    my_updater.start_polling()
    my_updater.idle()

if __name__ == '__main__':
    main()
