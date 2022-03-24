import telebot

token = "5104927403:AAEG_V8qtQQtzCNdkGhLbopFG9BKEWCx2Ho"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'И тебе привет')

bot.polling(none_stop=True)
