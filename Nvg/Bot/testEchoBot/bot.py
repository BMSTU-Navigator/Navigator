#https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter1.h

from Nvg.Bot import telebot
from Nvg.Bot.testEchoBot import config


from Nvg.Bot.chatterbot import ChatBot



bot = telebot.TeleBot(config.token)
chatbot = ChatBot('Charlie')







@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if(message.text=='Привет'):
        bot.send_message(message.chat.id,'и тебе привет')
    else:
        text=message.text
        response = chatbot.get_response(text)
        print(response)
        bot.send_message(message.chat.id, response)

if __name__ == '__main__':
     bot.polling(none_stop=True)