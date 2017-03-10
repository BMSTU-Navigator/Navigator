#https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter1.h

from Nvg.Bot import telebot
from Nvg.Bot.testEchoBot import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)