#https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter1.h



from Nvg.Bot.TelegramBot import config
from Nvg.old_code import telebot


bot = telebot.TeleBot(config.token)








@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if(message.text=='Привет'):
        bot.send_message(message.chat.id,'и тебе привет')
    else:
        text=message.text



if __name__ == '__main__':
     bot.polling(none_stop=True)