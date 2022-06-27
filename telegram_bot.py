from datetime import date
from email import message
from re import L
from time import sleep
import telebot
import math
from random import randint
import json

token = '5512229550:AAF9qGoRFPa3ukPqxTgbbbJb4dR_NJtAEeE'
bot = telebot.TeleBot(token)
langNumber1 = [0]




@bot.message_handler(commands=['start'])
def lang(message):
    bot.send_message(message.from_user.id, "Добро Пожаловать!\nҚош келдіңіз!\nWelcome!")
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(text='rus', callback_data='r')
    callback_button2 = telebot.types.InlineKeyboardButton(text='kaz', callback_data='k')
    keyboard.add(callback_button1, callback_button2)
    bot.send_message(message.from_user.id, 'Выберите язык:\nТілді таңдаңыз:\n', reply_markup=keyboard)


def get_all_data(message): 
    a = 0 
    global iin
    iin = message.text
    print(iin)
    with open('data.json', encoding='utf-8') as file:
        stock = json.load(file)
    for smth in stock:
        if smth['ИИН'] == iin:
            a = a + 1
        else:
            bot.send_message(message.from_user.id, 'Не правильный ИИН')  
            break          
    for smth in stock:
        if smth['ИИН'] == iin:
            if(a == 1):
                if(langNumber1[0]==0):
                    bot.send_message(message.from_user.id,smth['ФИО'] + listuVas[0] + str(a) + listRebenok[0])
                    break
                elif(langNumber1[0]==1):
                    bot.send_message(message.from_user.id,smth['ФИО'] + listuVas[1] + str(a) +  listRebenok[1])
                    break
            elif(a > 1):
                if(langNumber1[0]==0):
                    bot.send_message(message.from_user.id,smth['ФИО'] + listuVas[0] + str(a) + listRebenok[2])
                    break
                elif(langNumber1[0]==1):
                    bot.send_message(message.from_user.id,smth['ФИО'] + listuVas[1] + str(a) + listRebenok[1])
                    break
    for smth in stock:
        if smth['ИИН'] == iin:
            birthday = int(between_date_day(
                smth['Дата рождения Ребенка'], '01.09.2022') / 365)
            if(6 <= birthday <= 17):
               bot.send_message(message.from_user.id,smth['ФИО Ребенка'] + " " + str(birthday) + "лет")
    kb = telebot.types.InlineKeyboardMarkup(row_width=1)
    if(langNumber1[0]==0):
        callback_button1 = telebot.types.InlineKeyboardButton(text='Да', callback_data='d')
        callback_button2 = telebot.types.InlineKeyboardButton(text='Нет', callback_data='n')
        kb.add(callback_button1, callback_button2)
    else:
        callback_button1 = telebot.types.InlineKeyboardButton(text='Ия', callback_data='i')
        callback_button2 = telebot.types.InlineKeyboardButton(text='Жок', callback_data='j')
        kb.add(callback_button1, callback_button2)
    bot.send_message(message.from_user.id, list3Bank[langNumber1[0]], reply_markup=kb)
    # else:
    #     bot.send_message(message.from_user.id, 'Не правильный ИИН')
    return a


@bot.callback_query_handler(func=lambda call: True)
def callbackLang(call):
    if call.message:
        try:
            if call.data == "r" or call.data == "k":
                if call.data == "r":
                    langNumber1[0] = 0

                elif call.data == "k":
                    langNumber1[0] = 1

                print(langNumber1[0], listLang[langNumber1[0]])
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=listLangDef[langNumber1[0]])
                bot.send_message(call.message.chat.id,
                                 listLang[langNumber1[0]])
                bot.send_message(call.message.chat.id,
                                 listIIN[langNumber1[0]])
                bot.register_next_step_handler(call.message, get_all_data);
            if(langNumber1[0] == 0 ):
                if call.data == "d" or call.data == "n" :
                    if call.data == 'd':
                        b = get_count()
                        print(b)
                        bot.send_message(call.message.chat.id,
                                 listBalans[langNumber1[0]]+str(b)+"тг")

                    elif call.data == 'n':
                        bot.send_message(call.message.chat.id,
                                 listSupport[langNumber1[0]])
            elif(langNumber1[0] == 1 ):
                if call.data == "i" or call.data == "j":
                    if call.data == 'i':
                        b = get_count()
                        print(b)
                        bot.send_message(call.message.chat.id,
                                 listBalans[langNumber1[0]])
                            

                    elif call.data == 'j':
                        bot.send_message(call.message.chat.id,
                                 listSupport[langNumber1[0]]+str(b)+"тг")
                  
                
        except Exception as ex:
            print(ex)

def between_date_day(from_date, to_date):
    from_date = from_date.split(".")
    to_date = to_date.split(".")
    result_date = date(int(to_date[2]), int(to_date[1]), int(
        to_date[0])) - date(int(from_date[2]), int(from_date[1]), int(from_date[0]))
    return result_date.days


def get_count(): 
    a = 0 
    with open('data.json', encoding='utf-8') as file:
        stock = json.load(file)
    for smth in stock:
        if smth['ИИН'] == iin:
            birthday = int(between_date_day(
                smth['Дата рождения Ребенка'], '01.09.2022') / 365)
            if(6 <= birthday <= 17):
                a = a + 1
    price = a * 45000
    return price

langNumber = langNumber1[0]
listLang = ['Русский язык', 'Қазақ тілі']
listLangDef = ['Вы выбрали:', 'Сіз таңдадыңыз:']

listR_rus = ['Кассовые операции', 'Оформление кредита/депозита', 'Денежные переводы', 'Консультации']
listR_kaz = ['Кассалық операциялар', 'Несие/депозит өндеу', 'Ақша аударымдары', 'Консультациялар']

listRLists = [listR_rus, listR_kaz]

listIIN = ['Напишите свой ИИН:', "ИИН-iздi жазыныз:"]

listBalans = ['Ваш баланс:', 'Сiздiн балансыныз:',]
listuVas = [' у вас ', ' сізде ']
listRebenok = [' ребенок\nРебенку дается подарок от 6 до 17 лет!!!', ' балаңыз бар\nБалаға 6 жастан бастап 17 жасқа дейін подарок беріледі !!!',' детей\nРебенку дается подарок от 6 до 17 лет!!!']
list3Bank = ['Согласны ли вы? ', 'Келiсеciз бе?']

listSupport = ['Если вы не согланы обратитесь по номеру: 87077012916', 'Егер сiз келiспесенiз мына номiрге конырау шалыныз:87077012916']
bot.polling(none_stop=True) 