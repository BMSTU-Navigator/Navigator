#https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter1.h



from Nvg.Bot.TelegramBot import config
from Nvg.old_code import telebot
from Nvg.Bot.TelegramBot.Bot import *

bot = telebot.TeleBot(config.token)

id_list=[]
bots={}






@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.chat.id not in id_list:
        id_list.append(message.chat.id)
        tmp_bot=Bot(bot,message.chat.id)
        bots[message.chat.id]=tmp_bot
        tmp_bot=None

    bots[message.chat.id].get_answer(message.text)



    #if(message.text!='Привет'):
    #    bot.send_message(message.chat.id,'и тебе привет')
    #else:
    #    bot.send_message(message.chat.id, 'start')
    #    bot.send_photo(message.chat.id,open('fl2.jpeg', 'rb'))
    #    bot.send_message(message.chat.id, 'stop')



if __name__ == '__main__':
     bot.polling(none_stop=True)