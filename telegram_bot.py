from datetime import date
from email import message
from itertools import count
from re import L
import re
from time import sleep
import telebot
import math
from random import randint
import json
import asyncio


token = '5512229550:AAF9qGoRFPa3ukPqxTgbbbJb4dR_NJtAEeE'
bot = telebot.TeleBot(token)
langNumber1 = [0]
user_data = {
    'iin': '',
    'fio': '',
    'phone_number': '',
    'email': '',
    'balans': '',
    'count_deti': '',
    'dengi': 0,
    'meloman_count': 0,
    'marwin_count': 0,
    'lcwaikiki_count': 0,
    'dengi_count': 0,
    'lok': '',
    'accept': False,
    'save': False,
    'lang': ''
}

info_data = {
    'count_plus': 0,
    'count_minus': 0,
    'in_korazina': True
}



@bot.message_handler(commands=['start'])
def lang(message):
    bot.send_photo(message.from_user.id,
                   photo=open('img/ttc.jpg', 'rb'),caption="<b>Добро Пожаловать!\nҚош келдіңіз!</b>",parse_mode = "HTML")
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listLang[0], callback_data='r')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text=listLang[1], callback_data='k')
    keyboard.add(callback_button1, callback_button2)
    bot.send_message(message.from_user.id,
                     '<b>Выберите язык:\nТілді таңдаңыз:\n</b>', reply_markup=keyboard,parse_mode = "HTML")


def get_all_data(message):
    a = 0
    b = 0
    c = 0
    kuka = True
    global iin
    with open('data.json', encoding='utf-8') as file:
        stock = json.load(file)

    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    user_data['phone_number'] = message.contact.phone_number
    for smth in stock:
        if(smth['Телефон'] == user_data['phone_number']):
            iin = smth['ИИН']
    for smth in stock:
        if smth['ИИН'] == iin.replace(" ", ""):
            a = a + 1
    for i in data:
        if(user_data['phone_number'] == i['phone_number']):
            user_data['iin'] = i['iin']
            user_data['fio'] = i['fio']
            user_data['phone_number'] = i['phone_number']
            user_data['email'] = i['email']
            user_data['balans'] = i['balans']
            user_data['count_deti'] = i['count_deti']
            user_data['dengi'] = i['dengi']
            user_data['meloman_count'] = i['meloman_count']
            user_data['marwin_count'] = i['marwin_count']
            user_data['lcwaikiki_count'] = i['lcwaikiki_count']
            user_data['accept'] = i['accept']
            user_data['save'] = i['save']
            user_data['lang'] = i['lang']



    for smth in stock:
        if smth['ИИН'] == iin.replace(" ", "") and user_data['save'] == False and user_data['accept'] == False: 
            if(a == 1):
                if(langNumber1[0] == 0):
                    bot.send_message(
                        message.from_user.id, smth['ФИО'] + listuVas[0] + str(a) + listRebenok[0])
                    user_data['fio'] = smth['ФИО']
                    user_data['email'] = smth['Почта']
                    user_data['iin'] = str(iin)
                    break
                elif(langNumber1[0] == 1):
                    bot.send_message(
                        message.from_user.id, smth['ФИО'] + listuVas[1] + str(a) + listRebenok[1])
                    user_data['fio'] = smth['ФИО']
                    user_data['email'] = smth['Почта']
                    user_data['iin'] = str(iin)
                    break
            elif(a > 1):
                if(langNumber1[0] == 0):
                    bot.send_message(
                        message.from_user.id, smth['ФИО'] + listuVas[0] + str(a) + listRebenok[2])
                    user_data['fio'] = smth['ФИО']
                    user_data['email'] = smth['Почта']
                    user_data['iin'] = str(iin)
                    break
                elif(langNumber1[0] == 1):
                    bot.send_message(
                        message.from_user.id, smth['ФИО'] + listuVas[1] + str(a) + listRebenok[1])
                    user_data['fio'] = smth['ФИО']
                    user_data['email'] = smth['Почта']
                    user_data['iin'] = str(iin)
                    break
    for smth in stock:
        if smth['ИИН'] == iin.replace(" ", "") and user_data['save'] == False and user_data['accept'] == False:
            birthday = int(between_date_day(
                smth['Дата рождения Ребенка'], '01.09.2022') / 365)
            if(6 <= birthday <= 17):
                bot.send_message(
                    message.from_user.id, smth['ФИО Ребенка'] + " " + str(birthday) + " " + listLet[langNumber1[0]])
                b = b + 1
    user_data['count_deti'] = str(b)
    for smth in stock:
        if smth['ИИН'] == iin.replace(" ", "") and user_data['save'] == False and user_data['accept'] == False:
            kb = telebot.types.InlineKeyboardMarkup(row_width=1)
            if(langNumber1[0] == 0):
                callback_button1 = telebot.types.InlineKeyboardButton(
                    text='Да', callback_data='d')
                callback_button2 = telebot.types.InlineKeyboardButton(
                    text='Нет', callback_data='n')
                kb.add(callback_button1, callback_button2)
            else:
                callback_button1 = telebot.types.InlineKeyboardButton(
                    text='Ия', callback_data='i')
                callback_button2 = telebot.types.InlineKeyboardButton(
                    text='Жок', callback_data='j')
                kb.add(callback_button1, callback_button2)
            bot.send_message(message.from_user.id,
                             list3Bank[langNumber1[0]], reply_markup=kb)
            break
    if(user_data['accept'] == True):
        get_cart(message)
    if(user_data['save'] == True):
        bot.send_message(
            message.from_user.id, listChoosed[langNumber1[0]])
        mel = user_data['meloman_count'] * 5000
        mar = user_data['marwin_count'] * 5000
        lc = user_data['lcwaikiki_count'] * 5000
        bot.send_message(message.chat.id, 'Корзина'+'\U0001F5D1'+'\n' +
                         listBalans[langNumber1[0]] + ':' + str(user_data['balans']) + 'тг\n' +
                         listMoney[langNumber1[0]] + ':' +
                         str(user_data['dengi']) + 'тг' +
                         '\nМеломан сертификаты:' + str(user_data['meloman_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(mel) +
                         'тг\nMarwin сертификаты:' + str(user_data['marwin_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(mar) +
                         'тг\nLCWaikiki сертификаты:' + str(user_data['lcwaikiki_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(lc)+'тг')
        repeat_start(message)



def add_and_delete(message):
    price = str(user_data[user_data['lok']] * 5000) + 'тг'
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(text='➕',callback_data='plus',)
    callback_button2 = telebot.types.InlineKeyboardButton(text=str(user_data[user_data['lok']]) + 'шт.- ' + price,callback_data='howmany')
    callback_button3 = telebot.types.InlineKeyboardButton(text='➖',callback_data='minus')
    callback_button4 = telebot.types.InlineKeyboardButton(text='🔙 Каталог',callback_data='enough')
    callback_button5 = telebot.types.InlineKeyboardButton(text='❌',callback_data='delete_full')
    keyboard.add( callback_button2)
    keyboard.row(callback_button5,callback_button3,callback_button1)
    keyboard.add(callback_button4)
    if(user_data['lok']=='dengi_count'):
        bot.send_photo(message.chat.id,
                    photo=open('img/tenge.jpg', 'rb'),caption="<b>Деньги</b>\nЦена: 5000тг",parse_mode = "HTML", reply_markup=keyboard)
    elif(user_data['lok']=='meloman_count'):
        bot.send_photo(message.chat.id,
                    photo=open('img/marw_melo.jpg', 'rb'),caption="<b>Сертификат Меломан</b>\nЦена: 5000тг",parse_mode = "HTML", reply_markup=keyboard)
    elif(user_data['lok']=='marwin_count'):
        bot.send_photo(message.chat.id,
                    photo=open('img/marw_melo.jpg', 'rb'),caption="<b>Сертификат Marwin</b>\nЦена: 5000тг",parse_mode = "HTML", reply_markup=keyboard)
    elif(user_data['lok']=='lcwaikiki_count'):
        bot.send_photo(message.chat.id,
                    photo=open('img/lcwaikiki.png', 'rb'),caption="<b>Сертификат LCWaikiki</b>\nЦена: 5000тг",parse_mode = "HTML", reply_markup=keyboard)


def get_cart(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    callback_button2 =  telebot.types.KeyboardButton('Корзина'+'\U0001F5D1')
    callback_button1 =  telebot.types.KeyboardButton('Каталог'+'\U0001F6D2')
    callback_button3 =  telebot.types.KeyboardButton(listChangeLang[langNumber1[0]]+'\U0001F6AA')
    keyboard.add(callback_button1, callback_button2, callback_button3)
    bot.send_message(message.chat.id, '<b>' + listCart[langNumber1[0]] +str(user_data['balans'])+'тг</b>\n', reply_markup=keyboard,parse_mode="HTML")


def get_magazin(message):
    info_data['in_korazina'] = False
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listMoney[langNumber1[0]]+'\U0001F4B0', callback_data='dengi')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Сертификат'+'\U0001F4DC', callback_data='sertificaty')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2, callback_button3)
    bot.send_message(message.chat.id, 'Каталог'+'\U0001F6D2', reply_markup=keyboard)


def get_korzina(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listAccept[langNumber1[0]]+'\U00002705', callback_data='soglasitsya')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text=listWhatDelete[langNumber1[0]]+'\U0000274C', callback_data='delete')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text=listRedaktirovat[langNumber1[0]], callback_data='redaktirovat')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4)
    mel = user_data['meloman_count'] * 5000
    mar = user_data['marwin_count'] * 5000
    lc = user_data['lcwaikiki_count'] * 5000
    bot.send_message(message.chat.id, 'Корзина'+'\U0001F5D1'+'\n' +
                     listBalans[langNumber1[0]] + ':' + str(user_data['balans']) + 'тг\n\n' +
                     listMoney[langNumber1[0]] + ':' +
                         str(user_data['dengi']) + 'тг'+'\U0001F4B0'
                     '\nМеломан сертификаты:' + str(user_data['meloman_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(mel) +
                     'тг\nMarwin сертификаты:' + str(user_data['marwin_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(mar) +
                     'тг\nLCWaikiki сертификаты:' + str(user_data['lcwaikiki_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(lc)+'тг', reply_markup=keyboard)



def get_delete(message):
    info_data['in_korazina'] = True
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listMoney[langNumber1[0]]+'\U0001F4B0', callback_data='dengi_delete')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Меломан сертификат', callback_data='mel-sertificaty')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='Marwin сертификат', callback_data='mar-sertificaty')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text='LCWaikiki сертификат', callback_data='lc-sertificaty')
    callback_button5 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2,
                 callback_button3, callback_button4, callback_button5)
    bot.send_message(
        message.chat.id, listChoose[langNumber1[0]], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callbackLang(call):
    b = ''
    if call.message:
        try:
            if call.data == "r" or call.data == "k":
                if call.data == "r":
                    langNumber1[0] = 0

                elif call.data == "k":
                    langNumber1[0] = 1

                # print(langNumber1[0], listLang[langNumber1[0]])
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text=listLangDef[langNumber1[0]])
                bot.send_message(call.message.chat.id,
                                 listLang[langNumber1[0]])
                user_data['lang'] = listLang[langNumber1[0]]
                get_phone_number(call.message)
                bot.register_next_step_handler(call.message, get_all_data)
            elif call.data == "d" or call.data == "n" or call.data == "i" or call.data == "j":
                if call.data == 'd':
                    b = get_count()
                    user_data['balans'] = b
                    # print(user_data)
                    if(user_data['accept']==False):
                        user_data['accept'] = True
                        save_data(user_data)
                        #clear nuzhno zavtra
                    get_cart(call.message)
                elif call.data == 'n':
                    bot.send_message(call.message.chat.id,
                                     listSupport[langNumber1[0]])
                elif call.data == 'i':
                    b = get_count()
                    user_data['balans'] = b
                    # print(user_data)
                    if(user_data['accept']==False):
                        user_data['accept'] = True
                        save_data(user_data)
                    get_cart(call.message)
                elif call.data == 'j':
                    bot.send_message(call.message.chat.id,
                                     listSupport[langNumber1[0]])
            elif call.data == "korzina" or call.data == "magazin" or call.data == "vyhod":
                if call.data == 'korzina':
                    get_korzina(call.message)
                elif call.data == 'magazin':
                    get_magazin(call.message)
                elif call.data == 'vyhod':
                    user_data_clear()
                    repeat_start(call.message)
            elif call.data == "dengi" or call.data == "sertificaty" or call.data == "nazad":
                if call.data == 'dengi':
                    b = 'dengi_count'
                    user_data['lok'] = b
                    add_and_delete(call.message)

                elif call.data == 'sertificaty':
                    get_sertificat(call.message)
                elif call.data == 'nazad':
                    get_cart(call.message)
            elif call.data == "meloman" or call.data == "marwin" or call.data == "lcwaikiki":
                
                if call.data == 'meloman':
                    b = 'meloman_count'
                    user_data['lok'] = b
                    add_and_delete(call.message)
                elif call.data == 'marwin':
                    b = 'marwin_count'
                    user_data['lok'] = b
                    add_and_delete(call.message)
                elif call.data == 'lcwaikiki':
                    b = 'lcwaikiki_count'
                    user_data['lok'] = b
                    add_and_delete(call.message)
            elif call.data == "soglasitsya" or call.data == "delete" or call.data == "redaktirovat":
                if call.data == 'soglasitsya':
                    bot.send_message(call.message.chat.id,
                                     listEndAccept[langNumber1[0]])
                    bot.register_next_step_handler(
                        call.message, get_sogl)
                elif call.data == 'delete':
                    clear_cart(call.message)
                    bot.send_message(call.message.chat.id,
                                     listDeleted[langNumber1[0]])
                elif call.data == "redaktirovat":
                    get_delete(call.message)
            elif call.data == "dengi_delete" or call.data == "mel-sertificaty" or call.data == "mar-sertificaty" or call.data == "lc-sertificaty":
                if call.data == 'dengi_delete':
                    b = 'dengi_count'
                    user_data['lok'] = b
                    bot.send_message(call.message.chat.id,
                                     listReturnMoney[langNumber1[0]])
                    add_and_delete(call.message)
                elif call.data == 'mel-sertificaty':
                    b = 'meloman_count'
                    user_data['lok'] = b
                    bot.send_message(call.message.chat.id,
                                     listReturnMeloman[langNumber1[0]])
                    add_and_delete(call.message)
                elif call.data == 'mar-sertificaty':
                    b = 'marwin_count'
                    user_data['lok'] = b
                    bot.send_message(call.message.chat.id,
                                     listReturnMarwin[langNumber1[0]])
                    add_and_delete(call.message)
                elif call.data == 'lc-sertificaty':
                    b = 'lcwaikiki_count'
                    user_data['lok'] = b
                    bot.send_message(call.message.chat.id,
                                     listReturnLCWaikiki[langNumber1[0]])
                    add_and_delete(call.message)
            elif call.data == "plus" or call.data == "minus" or call.data == 'enough' or call.data == 'delete_full':
                if call.data == 'plus':
                    add_plus(call.message)
                    price = str(user_data[user_data['lok']] * 5000) + 'тг'
                    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
                    callback_button1 = telebot.types.InlineKeyboardButton(text='➕',callback_data='plus',)
                    callback_button2 = telebot.types.InlineKeyboardButton(text=str(user_data[user_data['lok']]) + 'шт.- ' + price,callback_data='howmany')
                    callback_button3 = telebot.types.InlineKeyboardButton(text='➖',callback_data='minus')
                    callback_button4 = telebot.types.InlineKeyboardButton(text='🔙 Каталог',callback_data='enough')
                    callback_button5 = telebot.types.InlineKeyboardButton(text='❌',callback_data='delete_full')
                    keyboard.add( callback_button2)
                    keyboard.row(callback_button5,callback_button3,callback_button1)
                    keyboard.add(callback_button4)
                    bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=keyboard)
                    get_all_func(call.message)
                elif call.data == 'minus':
                    delete_minus(call.message)
                    price = str(user_data[user_data['lok']] * 5000) + 'тг'
                    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
                    callback_button1 = telebot.types.InlineKeyboardButton(text='➕',callback_data='plus',)
                    callback_button2 = telebot.types.InlineKeyboardButton(text=str(user_data[user_data['lok']]) + 'шт.- ' + price,callback_data='howmany')
                    callback_button3 = telebot.types.InlineKeyboardButton(text='➖',callback_data='minus')
                    callback_button4 = telebot.types.InlineKeyboardButton(text='🔙 Каталог',callback_data='enough')
                    callback_button5 = telebot.types.InlineKeyboardButton(text='❌',callback_data='delete_full')
                    keyboard.add( callback_button2)
                    keyboard.row(callback_button5,callback_button3,callback_button1)
                    keyboard.add(callback_button4)
                    bot.edit_message_reply_markup(call.from_user.id, call.message.message_id, reply_markup=keyboard)
                    get_all_func(call.message)
                elif call.data == 'enough':
                    if(user_data['lok']=='meloman_count'):
                        get_sertificat(call.message)
                    elif(user_data['lok']=='marwin_count'):
                        get_sertificat(call.message)
                    elif(user_data['lok']=='lcwaikiki_count'):
                        get_sertificat(call.message)
                    elif(user_data['lok']=='dengi_count'):
                        get_magazin(call.message)
                elif call.data == 'delete_full':
                    if(user_data['lok'] == 'dengi_count'):
                        user_data['dengi'] = 0
                        user_data['balans'] = int(user_data['balans']) + user_data[user_data['lok']]*5000
                        user_data[user_data['lok']] = 0
                    else:
                        user_data['balans'] = int(user_data['balans']) + user_data[user_data['lok']]*5000
                        user_data[user_data['lok']] = 0
                        
                    if(info_data['in_korazina'] == False):
                        get_magazin(call.message)
                    else:
                        get_korzina(call.message)



        except Exception as ex:
            print(ex)


def repeat_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    callback_button1 = telebot.types.KeyboardButton('Старт')
    keyboard.add(callback_button1)
    bot.send_message(
        message.chat.id, listGoodBye[langNumber1[0]]+'\U0001F44B', reply_markup=keyboard)
def get_all_func(message):
    if(user_data['lok']=='meloman_count'):
        get_meloman_sert(message)
    elif(user_data['lok']=='marwin_count'):
        get_marwin_sert(message)
    elif(user_data['lok']=='lcwaikiki_count'):
        get_lcwaikiki_sert(message)
    elif(user_data['lok']=='dengi_count'):
        get_dengi(message)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Старт":
        lang(message)
    elif message.text == "Добавить":
        print(user_data[user_data['lok']])
        add_plus(message)
        bot.send_message(message.chat.id, 'Вы выбрали:' +
                         str(user_data[user_data['lok']]))
    elif message.text == "Убрать":
        delete_minus(message)
        bot.send_message(message.chat.id, 'Вы выбрали:' +
                         str(user_data[user_data['lok']]))
    elif message.text == "Достаточно":
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        callback_button1 = telebot.types.KeyboardButton('Назад')
        keyboard.add(callback_button1)
        bot.send_message(message.chat.id, 'Назад', reply_markup=keyboard)
        if(user_data['lok']=='meloman_count'):
            get_meloman_sert(message)
        elif(user_data['lok']=='marwin_count'):
            get_marwin_sert(message)
        elif(user_data['lok']=='lcwaikiki_count'):
            get_lcwaikiki_sert(message)
    elif message.text == "Назад":
        get_cart(message)
    elif message.text == 'Каталог'+'\U0001F6D2':
        get_magazin(message)
    elif message.text == 'Корзина'+'\U0001F5D1':
        get_korzina(message)






def add_plus(message):
    try:
        krange = info_data['count_plus'] * 5000 
        if(int(user_data['balans'])-krange>0):
            info_data['count_plus']=info_data['count_plus']+1
            user_data[user_data['lok']] = user_data[user_data['lok']] + 1
        else:
            bot.send_message(message.chat.id, 'У вас не хватает баланса')
    except Exception as ex:
        print(ex)


def delete_minus(message):
    try:
        krange = info_data['count_minus'] * 5000
        if(user_data[user_data['lok']] > 0):
            info_data['count_minus']=info_data['count_minus']+1
            user_data[user_data['lok']] = user_data[user_data['lok']] - 1
        elif(user_data[user_data['lok']] == 0):
            bot.send_message(message.chat.id, 'Невозможно меньше нуля')
    except Exception as ex:
        print(ex)


def get_dengi(message):
    global count_plus
    global count_minus
    count_plus = info_data['count_plus']
    count_minus = info_data['count_minus']
    try:
        if((type(int(count_plus)) == int) and (type(int(count_minus)) == int) ):
            price1 = int(count_plus) * 5000
            price2 = int(count_minus) * 5000
            user_data['balans'] =str(int(user_data['balans'])+price2)
            # print(price)
            if(int(user_data['balans']) >= int(price1)):
                user_data['balans'] = str(int(user_data['balans'])-price1)
                # user_data['meloman_count'] = user_data['meloman_count'] + \
                #     int(count)
                user_data['dengi'] = user_data['dengi'] + price1-price2
                info_data['count_plus'] = 0
                info_data['count_minus'] = 0
                # print(user_data)
            else:
                print("Ошибка")
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id,
                         listDontUnderstand[langNumber1[0]]+'\U0001F914')
        get_cart(message)




def add_mel(message):
    count = message.text
    if(int(user_data['meloman_count']) >= int(count)):
        price = int(count)*5000
        user_data['balans'] = str(int(user_data['balans']) + price)
        user_data['meloman_count'] = user_data['meloman_count'] - int(count)
        bot.send_message(
            message.chat.id, listSuccess[langNumber1[0]]+'\U0001F44D')
        get_korzina(message)
    else:
        bot.send_message(message.chat.id,
                         listUnSuccess[langNumber1[0]]+'\U0001F614')
        get_korzina(message)


def add_mar(message):
    count = message.text
    if(int(user_data['marwin_count']) >= int(count)):
        price = int(count)*5000
        user_data['balans'] = str(int(user_data['balans']) + price)
        user_data['marwin_count'] = user_data['marwin_count'] - int(count)
        bot.send_message(
            message.chat.id, listSuccess[langNumber1[0]]+'\U0001F44D')
        get_korzina(message)
    else:
        bot.send_message(
            message.chat.id, listUnSuccess[langNumber1[0]]+'\U0001F614')
        get_korzina(message)


def add_lcwai(message):
    count = message.text
    if(int(user_data['lcwaikiki_count']) >= int(count)):
        price = int(count)*5000
        user_data['balans'] = str(int(user_data['balans']) + price)
        user_data['lcwaikiki_count'] = user_data['lcwaikiki_count'] - \
            int(count)
        bot.send_message(
            message.chat.id, listSuccess[langNumber1[0]]+'\U0001F44D')
        get_korzina(message)
    else:
        bot.send_message(message.chat.id,
                         listUnSuccess[langNumber1[0]]+'\U0001F614')
        get_korzina(message)


def add_balans(message):
    global dengi
    dengi = message.text
    if(int(user_data['dengi']) >= int(dengi)):
        user_data['balans'] = str(int(user_data['balans']) + int(dengi))
        user_data['dengi'] = user_data['dengi'] - int(dengi)
        bot.send_message(
            message.chat.id, listSuccess[langNumber1[0]]+'\U0001F44D')
        get_korzina(message)
    else:
        bot.send_message(
            message.chat.id, listUnSuccess[langNumber1[0]]+'\U0001F614')
        get_korzina(message)


def get_sogl(message):
    global sogl
    sogl = message.text
    if(sogl.lower() == 'соглашаюсь' or sogl.lower() == 'келісемін'):
        bot.send_message(
            message.chat.id, listGoodByeSuccess[langNumber1[0]]+'\U0001F44B')
        # print(user_data)
        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)
        # 2. Update json object
        data.append(user_data)
        # 3. Write json file
        with open('result.json', "w", encoding='utf8') as file:
            file.write(json.dumps(data, ensure_ascii=False))
        user_data_clear()
        # print(user_data)
    else:
        bot.send_message(
            message.chat.id, listUnSuccess[langNumber1[0]]+'\U0001F614')
        get_korzina(message)


def get_meloman_sert(message):
    global count_plus
    global count_minus
    count_plus = info_data['count_plus']
    count_minus = info_data['count_minus']
    try:
        if((type(int(count_plus)) == int) and (type(int(count_minus)) == int) ):
            price1 = int(count_plus) * 5000
            price2 = int(count_minus) * 5000
            user_data['balans'] =str(int(user_data['balans'])+price2)
            # print(price)
            if(int(user_data['balans']) >= int(price1)):
                user_data['balans'] = str(int(user_data['balans'])-price1)
                # user_data['meloman_count'] = user_data['meloman_count'] + \
                #     int(count)
                info_data['count_plus'] = 0
                info_data['count_minus'] = 0
                # print(user_data)
            else:
                print("Ошибка")
    except Exception as ex:
        print(ex)
        get_sertificat(message)


def get_marwin_sert(message):
    global count_plus
    global count_minus
    count_plus = info_data['count_plus']
    count_minus = info_data['count_minus']
    try:
        if((type(int(count_plus)) == int) and (type(int(count_minus)) == int) ):
            price1 = int(count_plus) * 5000
            price2 = int(count_minus) * 5000
            user_data['balans'] =str(int(user_data['balans'])+price2)
            # print(price)
            if(int(user_data['balans']) >= int(price1)):
                user_data['balans'] = str(int(user_data['balans'])-price1)
                # user_data['meloman_count'] = user_data['meloman_count'] + \
                #     int(count)
                info_data['count_plus'] = 0
                info_data['count_minus'] = 0
                # print(user_data)
            else:
                print("Ошибка")
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id,
                         listDontUnderstand[langNumber1[0]]+'\U0001F914')
        get_sertificat(message)

def get_lcwaikiki_sert(message):
    global count_plus
    global count_minus
    count_plus = info_data['count_plus']
    count_minus = info_data['count_minus']
    try:
        if((type(int(count_plus)) == int) and (type(int(count_minus)) == int) ):
            price1 = int(count_plus) * 5000
            price2 = int(count_minus) * 5000
            user_data['balans'] =str(int(user_data['balans'])+price2)
            # print(price)
            if(int(user_data['balans']) >= int(price1)):
                user_data['balans'] = str(int(user_data['balans'])-price1)
                # user_data['meloman_count'] = user_data['meloman_count'] + \
                #     int(count)
                info_data['count_plus'] = 0
                info_data['count_minus'] = 0
                # print(user_data)
            else:
                print("Ошибка")
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id,
                         listDontUnderstand[langNumber1[0]]+'\U0001F914')
        get_sertificat(message)


def get_sertificat(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='Meloman', callback_data='meloman')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Marwin', callback_data='marwin')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='LCWaikiki', callback_data='lcwaikiki')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2,
                 callback_button3, callback_button4)
    bot.send_message(
        message.chat.id, listCertificateEach[langNumber1[0]]+'\U0001F4B8', reply_markup=keyboard)


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


def user_data_clear():
    user_data['iin'] = ''
    user_data['fio'] = ''
    user_data['phone_number'] = ''
    user_data['email'] = ''
    user_data['balans'] = ''
    user_data['count_deti'] = ''
    user_data['dengi'] = 0,
    user_data['meloman_count'] = 0,
    user_data['marwin_count'] = 0,
    user_data['lcwaikiki_count'] = 0,
    user_data['dengi_count'] = 0,
    user_data['lok'] = '',
    user_data['accept'] = False,
    user_data['save'] =  False,
    user_data['lang'] =  ''
    return user_data

def clear_cart(message):
    user_data['balans'] = str(int(user_data['balans']) + user_data['dengi'] + user_data['lcwaikiki_count']*5000 + user_data['meloman_count']*5000+user_data['marwin_count']*5000)
    user_data['dengi'] = 0
    user_data['meloman_count'] = 0
    user_data['marwin_count'] = 0
    user_data['lcwaikiki_count'] = 0
    user_data['dengi_count'] = 0 
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listAccept[langNumber1[0]]+'\U00002705', callback_data='soglasitsya')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text=listWhatDelete[langNumber1[0]]+'\U0000274C', callback_data='delete')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text=listRedaktirovat[langNumber1[0]], callback_data='redaktirovat')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4)
    mel = user_data['meloman_count'] * 5000
    mar = user_data['marwin_count'] * 5000
    lc = user_data['lcwaikiki_count'] * 5000
    bot.edit_message_text(
                    chat_id=message.chat.id, message_id=message.message_id, text='Корзина'+'\U0001F5D1'+'\n' +
                     listBalans[langNumber1[0]] + ':' + str(user_data['balans']) + 'тг\n\n' +
                     listMoney[langNumber1[0]] + ':' +
                         str(user_data['dengi']) + 'тг'+'\U0001F4B0'
                     '\nМеломан сертификаты:' + str(user_data['meloman_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(mel) +
                     'тг\nMarwin сертификаты:' + str(user_data['marwin_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(mar) +
                     'тг\nLCWaikiki сертификаты:' + str(user_data['lcwaikiki_count']) + ' ' + listCount[langNumber1[0]] + listNaSummu[langNumber1[0]] + ' ' + str(lc)+'тг', reply_markup=keyboard)

def save_data(user_data):
    with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
    data.append(user_data)
    with open('result.json', "w", encoding='utf8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

def get_phone_number(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
    button_phone = telebot.types.KeyboardButton(text=listPhone[langNumber1[0]], request_contact=True) 
    keyboard.add(button_phone) #Добавляем эту кнопку
    bot.send_message(message.chat.id, 'Проверка номера', reply_markup=keyboard)
langNumber = langNumber1[0]
listLang = ['Русский язык', 'Қазақ тілі']
listLangDef = ['Вы выбрали:', 'Сіз таңдадыңыз:']
listPhone = ['Отправить номер телефона','Телефон нөмірін жіберу']
listIIN = ['Напишите свой ИИН:', "ИИН-iздi жазыныз:"]

listBalans = ['Ваш баланс', 'Сiздiн балансыныз', ]
listuVas = [' у вас ', ' сізде ']
listRebenok = [' ребенок\nРебенку дается подарок от 6 до 17 лет!!!',
               ' балаңыз бар\nБалаға 6 жастан бастап 17 жасқа дейін подарок беріледі !!!', ' детей\nРебенку дается подарок от 6 до 17 лет!!!']
list3Bank = ['Согласны ли вы? ', 'Келiсеciз бе?']

listSupport = ['Если вы не согланы обратитесь по номеру: 87077012916',
               'Егер сiз келiспесенiз мына номiрге конырау шалыныз:87077012916']
listLet = ['лет', 'жаста']
listVyhod = ['Выход', 'Шығу']
listCart = ['Меню:\nВаш баланс: ', 'Мәзір:\nСіздің балансыңыз: ']
listMoney = ['Деньги', 'Ақша']
listBack = ['Назад', 'Артқа']
listAccept = ['Согласится', 'Келісу']
listDeleteTovar = ['Удалить товар', 'Тауарды алып тастау']
listCount = ['штук', 'дана']
listNaSummu = [', на сумму:', ', сомада:']
listChoose = ['Выберите', 'Таңдаңыз']
listGoodBye = ['Спасибо! До свидания!', 'Рахмет! Қош сау болыңыз!']
listVyvesti = ['1 штук = 5000тг\nНапишите количество:',
               '1 штук = 5000тг\nНСанын жазыныз:']
listCertificate = ['1 Сертификат = 5000тг\nДобавляйте, сколько штук сертификатов хотите:',
                   '1 Сертификат = 5000тг\nҚанша дана сертификат алғыңыз келетінін танданыз:']
listEndAccept = ['Если вы уверенны своем выборе напишите: Соглашаюсь',
                 'Егер сіз өз таңдауыңызға сенімді болсаңыз, жазыңыз: Келісемін']
listWhatDelete = ['Очистить корзину', 'Корзинаны тазалау']
listReturnMoney = ['1 штук = 5000тг\nНапишите сколько штук вы хотите вернуть на баланс:',
                   '1 штук = 5000тг\nБалансқа қанша штук қайтарғыңыз келетінін жазыңыз:']
listReturnMeloman = ['1 штук = 5000тг\nНапишите сколько сертификатов Меломана хотите вернуть:',
                     '1 штук = 5000тг\nҚанша дана Меломан сертификатын қайтарғыңыз келетінін жазыңыз:']
listReturnMarwin = ['1 штук = 5000тг\nНапишите сколько сертификатов Marwin хотите вернуть:',
                    '1 штук = 5000тг\nҚанша дана Marwin сертификатын қайтарғыңыз келетінін жазыңыз:']
listReturnLCWaikiki = ['1 штук = 5000тг\nНапишите сколько сертификатов LCWaikiki хотите вернуть:',
                       '1 штук = 5000тг\nҚанша дана LCWaikiki сертификатын қайтарғыңыз келетінін жазыңыз:']
listSuccess = ['Успешно', 'Сәтті']
listNotEnough = ['Не достаточно средств', 'Қаражат жеткіліксіз']
listUnSuccess = ['Не удалось!', 'Сәтсіз!']
listGoodByeSuccess = ['Успешно! До свидания!', 'Сәтті! Қош сау болыңыз!']
listDontUnderstand = ['Я вас не понял напишите еще раз',
                      'Мен сізді түсінбедім қайта жазыңыз']
cerKz = 'Сертификаттар\nБір сертификаттын құны ' + '5000' + 'тг'
cerRu = 'Сертификаты\nОдин сертификат стоит ' + '5000' + 'тг'
listCertificateEach = [cerRu, cerKz]
listUndefinedIIN = ['Не нашли такой ИИН', 'Мұндай ИИН табылмады']
listChoosed = ['Вы уже сделали выбор', 'Сіз таңдау жасадыңыз']
listRedaktirovat = ['Редактировать товары', 'Өнімдерді өңдеу']
listDeleted=['Очистили корзину','Себетті тазаланды']
listChangeLang = ['Сменить язык','Тілді өзгерту']
bot.infinity_polling(timeout=10, long_polling_timeout = 5)
