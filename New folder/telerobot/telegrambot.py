# pip install python-telegram-bot --upgrade 
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler

token = 'your token' # you can find your acount token from telegram botfather

updater = Updater(token=token,use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.sent_message(chat_id=update.effective_chat_id,text='i love learning python by SamCodeHub')
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()