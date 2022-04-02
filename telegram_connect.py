# ! pip install python-telegram-bot

# 1 зарегистрировать бота в телеграмею 
# 2 подключить наш код к библиотеке telegram-bot
# надо получить уникальный код

# найти BotFather (с галочкой - верифицированный)
# /help
# /newbot
# ***AIbot
# can be the same name
# use token

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

BOT_KEY = '000000000'

def hello(update: Update, context: CallbackContext):
      update.message.reply_text(r'Hello {update.effective_user.first_name}')

# функция вызывается при получении сообщения
def botMessage():
    text = Update.update.message.text # что нам написал пользователь
    reply = bot(text) # готовим ответ
    Update.update.message.reply_text(reply) # отправляем ответ

updater = Updater(BOT_KEY)

updater.dispatcher.add_handler(CommandHandler('hello', hello)) # конфигурация. при получении  hello вызвать функцию hello
updater.dispatcher.add_handler(MessageHandler(Filters.text, botMessage))

updater.start_polling()
updater.idle()