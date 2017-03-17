from Nvg.old_code import telebot

class Bot:
    dialog_id=-1;
    telebot =None
    def __init__(self,telebot,dialog_id):
        self.telebot=telebot
        self.dialog_id=dialog_id
    def get_answer(self,input_string):
        self.telebot.send_message(self.dialog_id, input_string+'  answer of bot '+str(self.dialog_id))
