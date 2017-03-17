from Nvg.old_code import telebot
from Nvg.WayBuilder.WayBuilderClass import *
from Nvg.SQL.SQL import *
class Bot:
    bot_id=-1
    dialog_id=-1;
    dialog_state=-1
    telebot =None

    building = None
    wb = None






    from_id=-1
    to_id=-1
    detalization_level=2


    def __init__(self,telebot,dialog_id,id):
        self.telebot=telebot
        self.dialog_id=dialog_id
        self.dialog_state=-2
        self.bot_id=id

        self.building = get_building()
        self.wb = WayBuilderClass(self.building)
        self.wb.init_pre_count()


    def get_answer(self,input_string):
        if self.dialog_state==-2:
            self.send_message('bot itit-2')
            self.dialog_state=-1
            return
        if self.dialog_state==-1:
            self.send_message('bot itit-1')
            self.dialog_state=0
            return
        if self.dialog_state==0:
            self.send_message('Привет')
            self.send_message('Скажи мне "да"')
            self.dialog_state=1
            return
        if self.dialog_state==1:
            if(input_string=='да'):
                self.send_message('Молодец')
                self.send_message('Все, я готов тебе помочь. Напиши где ты? (ключ)')
                self.dialog_state=2
            else:
                self.send_message('Еще раз. Я тебя не понял')
            return
        if self.dialog_state==2:
            if int(input_string) in range(0,17):
                self.from_id=int(input_string)
                self.send_message('Ага. ТЫ у кабинета '+str(self.from_id))
                self.send_message('А куда тебе надо? (ключ)')
                self.dialog_state=3
            else:
                self.send_message('Еще раз. Я тебя не понял')
            return
        if self.dialog_state==3:
            if int(input_string) in range(0,17):
                self.to_id=int(input_string)
                self.send_message('Ага. ТЫ хочешь пройти в кабинет '+str(self.to_id))
                self.send_message('Все, ща посчитаю маршрут и напишу тебе')



                path = self.wb.request_path(self.from_id, self.to_id)



                for i in range(len(path.points)):
                    self.send_message(path.points[i].name)
                    #if (i < len(path.connections)): print('com ' + str(path.connections[i].connection_comment))

                self.send_message('а еще лови план здания')
                self.send_photo('all.jpeg')
                self.dialog_state=2
            else:
                self.send_message('Еще раз. Я тебя не понял')








    def send_message(self,text):
        self.telebot.send_message(self.dialog_id, text + '  answer of bot '+str(self.bot_id) +'  chat_id='+ str(self.dialog_id))
    def send_photo(self,path):
        self.telebot.send_message(self.dialog_id,'+')
        self.telebot.send_photo(self.dialog_id,open(path, 'rb'))
        self.telebot.send_message(self.dialog_id,'+')