#!/usr/bin/python3

from ast import Break
from datetime import date
from email import message
from itertools import count
from re import I, L
import re
from time import sleep
import telebot
import math
from random import randint
import json
import asyncio
import pandas as pd
from yaml import parse
from conversiontools import ConversionClient


token = ''
bot = telebot.TeleBot(token)

langNumber1 = [0]

user_data = {
            'id': '',
            'iin': '',
            'fio': '',
            'phone_number': '',
            'balans': '',
            'count_deti': '',
            'dengi': 0,
            'sportmaster_count': {"type_nominal": "", "count_5000": 0,"count_10000": 0, "count_15000": 0, "count_25000": 0},
            'mechta_count': {"type_nominal": "","count_5000": 0, "count_10000": 0, "count_15000": 0, "count_25000": 0},
            'lcwaikiki_count': {"type_nominal": "","count_5000": 0, "count_10000": 0, "count_15000": 0, "count_25000": 0},
            'abdi_count': {"type_nominal": "","count_5000": 0, "count_10000": 0, "count_15000": 0, "count_25000": 0},
            'dengi_count': {"type_nominal": "", "count_5000": 0, "count_10000": 0, "count_15000": 0, "count_25000": 0},
            'lok': '',
            'accept': False,
            'save': False,
            'lang': '',
            'sended': False,
            'comment': []
        }
info_data = {
    'count_plus': 0,
    'count_minus': 0,
    'in_korazina': True,
    'type':""
}


@bot.message_handler(commands=['start'])
def lang(message):

    bot.send_photo(message.from_user.id,
                   photo=open('img/images.jpg', 'rb'), caption="<b>Добро Пожаловать!\nҚош келдіңіз!</b>", parse_mode="HTML")
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listLang[0], callback_data='r')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text=listLang[1], callback_data='k')
    keyboard.add(callback_button1, callback_button2)
    bot.send_message(message.from_user.id,
                    '<b>Выберите язык:\nТілді таңдаңыз:\n</b>', reply_markup=keyboard, parse_mode="HTML")


def lox(message):
    b = 0
    with open('u.json', encoding='utf-8') as fil:
        lox = json.load(fil)

    for i in lox:
        if(i['ИИН'] == message.text):
            b = b+1
    listHelpCenter = ['Обратитесь по нижеуказанным номерам:\n\n     Бейпилбаева Сауле Боранбаевна\n     +7-7172-610-767\n     +7-777-610-68-41',
                      'Төмендегі нөмірлерге хабарласыңыз:\n\n     Бейпилбаева Сауле Боранбаевна\n     +7-7172-610-767\n     0+7-777-610-68-41']
    if(b > 0):
        bot.send_message(
            message.chat.id, listHelpCenter[langNumber1[0]],  parse_mode="HTML")
    else:
        bot.send_message(
            message.chat.id, listIINno[langNumber1[0]],  parse_mode="HTML")


def get_all_data(message):
    a = 0
    b = 0
    c = 0
    kuka = True
    global iin
    with open('u.json', encoding='utf-8') as file:
        stock = json.load(file)
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    with open('all.json', encoding='utf-8') as file:
        all = json.load(file)

    for n in all:
        if(find_iin(message) == n['ИИН Сотрудника']):
            repeat_start(message)
            break
    else:
        try:
            if(message.contact.user_id == message.from_user.id):
                for smth in stock:
                    if(smth['Телефон'].replace("+", "") == str(message.contact.phone_number).replace("+","")):
                        save_data_json(message)
                        a = a + 1
                        break
                else:
                    bot.send_message(
                        message.from_user.id, listIIN[langNumber1[0]],  parse_mode="HTML")
                    bot.register_next_step_handler(message, lox)

                    
            else:
                bot.send_message(
                    message.chat.id, listItIsNotU[langNumber1[0]])
                get_phone_number(message)
        except Exception as ex:
            print(ex)
      
        try:
            if(message.contact.user_id == message.from_user.id):
                for smth in stock:
                    if smth['Телефон'] == str(message.contact.phone_number).replace("+","") :
                        bot.send_message(
                            message.from_user.id, "<b>" + smth['ФИО'] + "</b>" + listuVas[langNumber1[0]] + str(get_count_deti(message)) + listRebenok[langNumber1[0]], parse_mode="HTML")
                        break
            if(message.contact.user_id == message.from_user.id):
                for smth in stock:
                    if smth['Телефон'] == str(message.contact.phone_number).replace("+","") :
                            birthday = int(between_date_day(
                                smth['Дата рождения Ребенка'], '01.09.2022') / 365)
                            bot.send_message(
                                message.from_user.id, "<b>" + smth['ФИО Ребенка'] + " " + str(birthday) + " " + listLet[langNumber1[0]] + "</b>", parse_mode="HTML")
            if(message.contact.user_id == message.from_user.id):
                for smth in stock:
                    if smth['Телефон'] == str(message.contact.phone_number).replace("+","") :
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
                            # bot.send_message(message.from_user.id,
                            #                  listCart[langNumber1[0]] + '<b>' + get_count() +  'тг</b>',parse_mode="HTML")
                            bot.send_message(message.from_user.id,
                                            list3Bank[langNumber1[0]], reply_markup=kb)
                            break
        except Exception as ex:
            print(ex)
            get_phone_number(message)


def append_deti(lok,message):
    with open('u.json', encoding='utf-8') as files:
        stock = json.load(files)
    for smth in stock:
        if(smth['Телефон'].replace("+", "") == str(message.contact.phone_number).replace("+","")):
            birthday = int(between_date_day(
                            smth['Дата рождения Ребенка'], '01.09.2022') / 365)
            lok.append({"ФИО Ребенка": smth['ФИО Ребенка'], "Дата рождения ребенка": smth["Дата рождения Ребенка"], "Возраст": str(birthday)})
def add_and_delete(message):
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    for i in data:
        if(i['id']==str(message.chat.id)):
            if(i[i['lok']]['type_nominal'] == "5000"):
                price = str(i[i['lok']]['count_5000'] * 5000) + 'тг'
                shtuk = str(i[i['lok']]['count_5000'])
            elif(i[i['lok']]['type_nominal'] == "10000"):
                price = str(i[i['lok']]['count_10000'] * 10000) + 'тг'
                shtuk = str(i[i['lok']]['count_10000'])
            elif(i[i['lok']]['type_nominal'] == "15000"):
                price = str(i[i['lok']]['count_15000'] * 15000) + 'тг'
                shtuk = str(i[i['lok']]['count_15000'])
            elif(i[i['lok']]['type_nominal'] == "25000"):
                price = str(i[i['lok']]['count_25000'] * 25000) + 'тг'
                shtuk = str(i[i['lok']]['count_25000'])
            elif(i[i['lok']] == i['dengi_count']):
                if(i[i['lok']]['type_nominal'] == "5000"):
                    price = str(i[i['lok']]
                                ['count_5000'] * 5000) + 'тг'
                    shtuk = str(i[i['lok']]['count_5000'])
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
            callback_button1 = telebot.types.InlineKeyboardButton(
                text='➕', callback_data='plus',)
            callback_button2 = telebot.types.InlineKeyboardButton(
                text=shtuk + 'шт.- ' + price, callback_data='howmany')
            callback_button3 = telebot.types.InlineKeyboardButton(
                text='➖', callback_data='minus')
            callback_button4 = telebot.types.InlineKeyboardButton(
                text=listAddMore[langNumber1[0]], callback_data='enough')
            callback_button5 = telebot.types.InlineKeyboardButton(
                text='❌', callback_data='delete_full')
            callback_button6 = telebot.types.InlineKeyboardButton(
                text=listOstatok[langNumber1[0]] + i['balans'] + "тг", callback_data='balans')
            callback_button7 = telebot.types.InlineKeyboardButton(
                text=listPodtverdit[langNumber1[0]], callback_data='soglasitsya')
            callback_button8 = telebot.types.InlineKeyboardButton(
                text=listVashaSumma[langNumber1[0]] + str(i['count_deti']*45000) + 'тг', callback_data='balans')
            if(i['balans'] == str(i['count_deti']*45000)):
                keyboard.add(callback_button8)
                keyboard.add(callback_button2)
                keyboard.row(callback_button1, callback_button3, callback_button5)
                keyboard.add(callback_button7)
                keyboard.add(callback_button4)
            else:
                keyboard.add(callback_button8)
                keyboard.add(callback_button6)
                keyboard.add(callback_button2)
                keyboard.row(callback_button1, callback_button3, callback_button5)
                keyboard.add(callback_button7)
                keyboard.add(callback_button4)
            if(i['lok'] == 'dengi_count'):
                bot.send_message(message.chat.id, "<b>Деньги</b>\n" +
                                listKratnuyu[langNumber1[0]] + i[i['lok']]['type_nominal'] + "тг", reply_markup=keyboard, parse_mode="HTML")
            elif(i['lok'] == 'sportmaster_count'):
                bot.send_photo(message.chat.id,
                            photo=open('img/sport.jpg', 'rb'), caption="<b>Спортмастер</b>\n" + listKratnuyu[langNumber1[0]] + i[i['lok']]['type_nominal'] + "тг\n" + listCountKol[langNumber1[0]], parse_mode="HTML", reply_markup=keyboard)
            elif(i['lok'] == 'mechta_count'):
                bot.send_photo(message.chat.id,
                            photo=open('img/mechta.png', 'rb'), caption="<b>Меchta</b>\n" + listKratnuyu[langNumber1[0]] + i[i['lok']]['type_nominal'] + "тг\n" + listCountKol[langNumber1[0]], parse_mode="HTML", reply_markup=keyboard)
            elif(i['lok'] == 'lcwaikiki_count'):
                bot.send_photo(message.chat.id,
                            photo=open('img/lcwaikiki.png', 'rb'), caption="<b>LCWaikiki</b>\n" + listKratnuyu[langNumber1[0]] + i[i['lok']]['type_nominal'] + "тг\n" + listCountKol[langNumber1[0]], parse_mode="HTML", reply_markup=keyboard)
            elif(i['lok'] == 'abdi_count'):
                bot.send_photo(message.chat.id,
                            photo=open('img/adbi.jpg', 'rb'), caption="<b>ABDI</b>\n" + listKratnuyu[langNumber1[0]] + i[i['lok']]['type_nominal'] + "тг\n" + listCountKol[langNumber1[0]], parse_mode="HTML", reply_markup=keyboard)


def get_cart(message):
    try:
        keyboard = telebot.types.ReplyKeyboardMarkup(
            resize_keyboard=True, row_width=1, one_time_keyboard=True)
        callback_button2 = telebot.types.KeyboardButton(listMoney[langNumber1[0]])
        callback_button1 = telebot.types.KeyboardButton('Сертификаты📃')
        callback_button5 = telebot.types.KeyboardButton(listPart[langNumber1[0]])
        # callback_button4 = telebot.types.KeyboardButton('Корзина'+'\U0001F5D1')
        callback_button3 = telebot.types.KeyboardButton(
            listChangeLang[langNumber1[0]]+'🔠')
        keyboard.add(callback_button2, callback_button1,
                    callback_button5, callback_button3)
        bot.send_message(message.chat.id, '<b>' + listCart[langNumber1[0]] + get_balans(message)+'тг</b>\n', reply_markup=keyboard, parse_mode="HTML")
    except Exception as ex:
        print(ex)

def get_balans(message):
    with open('result.json', encoding='utf-8') as files:
            data = json.load(files)
    for i in data:
        if i['id']==str(message.chat.id):
            return i['balans']
def get_nominal(message):
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(
        text="10000тг", callback_data='10000')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='15000тг', callback_data='15000')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='25000тг', callback_data='25000')
    for i in data:
        if(i['id']==str(message.chat.id)):
            callback_button4 = telebot.types.InlineKeyboardButton(
                text=listOstatok[langNumber1[0]] + i['balans'] + 'тг', callback_data='balans')
    callback_button5 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]], callback_data='nazad')
    callback_button6 = telebot.types.InlineKeyboardButton(
        text='5000тг', callback_data='5000')
    keyboard.add(callback_button4,callback_button6, callback_button1,
                 callback_button2, callback_button3, callback_button5)
    bot.send_message(
        message.chat.id, listChooseNominal[langNumber1[0]], reply_markup=keyboard)


def get_nominal_for_dengi(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(
        text="10000тг", callback_data='10000')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='15000тг', callback_data='15000')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='25000тг', callback_data='25000')
    callback_button5 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]], callback_data='nazad')
    callback_button6 = telebot.types.InlineKeyboardButton(
        text='5000тг', callback_data='5000')
    keyboard.row(callback_button6, callback_button1,
                 callback_button2, callback_button3,)
    keyboard.row(callback_button5)
    bot.send_message(
        message.chat.id, listChooseNominal[langNumber1[0]], reply_markup=keyboard)


def get_magazin(message):
    info_data['in_korazina'] = False
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listMoney[langNumber1[0]]+'\U0001F4B0', callback_data='dengi')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Сертификат'+'\U0001F4DC', callback_data='sertificaty')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text=listBalans[langNumber1[0]] + ": " + user_data['balans'] + 'тг', callback_data='balans')
    keyboard.add(callback_button4, callback_button1,
                 callback_button2, callback_button3)
    bot.send_message(message.chat.id, 'Каталог' +
                     '\U0001F6D2', reply_markup=keyboard)


def get_korzina(message):
    info_data['in_korazina'] = True
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listAccept[langNumber1[0]]+'\U00002705', callback_data='soglasitsya')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text=listWhatDelete[langNumber1[0]]+'\U0000274C', callback_data='delete')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text=listRedaktirovat[langNumber1[0]], callback_data='redaktirovat')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    keyboard.row(callback_button1)
    keyboard.row(callback_button3)
    keyboard.row(callback_button2)
    keyboard.row(callback_button4)
    bot.send_message(message.chat.id, get_info_only_exists(message),
                     reply_markup=keyboard, parse_mode="HTML")


def get_delete(message):
    info_data['in_korazina'] = True
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listMoney[langNumber1[0]]+'\U0001F4B0', callback_data='dengi_delete')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Спортмастер сертификат', callback_data='mel-sertificaty')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='Mechta сертификат', callback_data='mar-sertificaty')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text='LCWaikiki сертификат', callback_data='lc-sertificaty')
    callback_button5 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='back')
    callback_button6 = telebot.types.InlineKeyboardButton(
        text=listBalans[langNumber1[0]] + ": " + user_data['balans'] + 'тг', callback_data='balans')
    keyboard.row(callback_button6)
    keyboard.row(callback_button1, callback_button2)
    keyboard.row(callback_button3, callback_button4)
    keyboard.row(callback_button5)
    bot.send_message(
        message.chat.id, listChoose[langNumber1[0]], reply_markup=keyboard)

def save_fo(info):
    with open('result.json', "w", encoding='utf8') as f:
        f.write(json.dumps(info, ensure_ascii=False))

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
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text=listLangDef[langNumber1[0]] + " " + listLang[langNumber1[0]])
                bot.send_message(call.message.chat.id,
                                 listInstruck[langNumber1[0]] + '\n\nИнструкция: '+ listYouTube[langNumber1[0]],parse_mode="HTML")
                user_data['lang'] = listLang[langNumber1[0]]
                get_phone_number(call.message)
            elif call.data == "d" or call.data == "n" or call.data == "i" or call.data == "j":
                if call.data == 'd':
                    with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
                    for i in data:
                        if(i['id']==str(call.message.chat.id)):
                            i['accept'] = True
                    with open('result.json', "w", encoding='utf8') as f:
                        f.write(json.dumps(data, ensure_ascii=False))
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    bot.delete_message(call.message.chat.id,
                                       call.message.message_id)
                    get_cart(call.message)
                elif call.data == 'n':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    keyboard = telebot.types.InlineKeyboardMarkup()
                    callback_button1 = telebot.types.InlineKeyboardButton(
                        text=listProdolzhit[langNumber1[0]], callback_data='d')
                    keyboard.add(callback_button1)
                    bot.send_message(
                        call.message.chat.id, get_help_by_filial(find_city(), call.message), reply_markup=keyboard)

                elif call.data == 'i':
                    with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
                    for i in data:
                        if(i['id']==str(call.message.chat.id)):
                            i['accept'] = True
                    with open('result.json', "w", encoding='utf8') as f:
                        f.write(json.dumps(data, ensure_ascii=False))
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    bot.delete_message(call.message.chat.id,
                                       call.message.message_id)
                    get_cart(call.message)
                elif call.data == 'j':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    keyboard = telebot.types.InlineKeyboardMarkup()
                    callback_button1 = telebot.types.InlineKeyboardButton(
                        text=listProdolzhit[langNumber1[0]], callback_data='d')
                    keyboard.add(callback_button1)
                    bot.send_message(
                        call.message.chat.id, get_help_by_filial(find_city(), call.message), reply_markup=keyboard)
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
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'dengi_count'
                    user_data['lok'] = b
                    user_data['dengi_count']['type_nominal'] = "5000"
                    add_and_delete(call.message)
                elif call.data == 'sertificaty':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    get_sertificat(call.message)
                elif call.data == 'nazad':
                    get_cart(call.message)
                    bot.delete_message(call.message.chat.id,
                                       call.message.message_id)
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    info_data['in_korazina']
            elif call.data == "meloman" or call.data == "marwin" or call.data == "lcwaikiki" or call.data == 'abdi':
                with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
                if call.data == 'meloman':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'sportmaster_count'
                    for i in data:
                        if(i['id']==str(call.message.chat.id)):
                            i['lok'] = b
                    save_fo(data)
                    get_nominal(call.message)
                elif call.data == 'marwin':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'mechta_count'
                    for i in data:
                        if(i['id']==str(call.message.chat.id)):
                            i['lok'] = b
                    save_fo(data)
                    get_nominal(call.message)
                elif call.data == 'lcwaikiki':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'lcwaikiki_count'
                    for i in data:
                        if(i['id']==str(call.message.chat.id)):
                            i['lok'] = b
                    save_fo(data)
                    get_nominal(call.message)
                elif call.data == 'abdi':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'abdi_count'
                    for i in data:
                        if(i['id']==str(call.message.chat.id)):
                            i['lok'] = b
                    save_fo(data)
                    get_nominal(call.message)
            elif call.data == "soglasitsya" or call.data == "delete" or call.data == "redaktirovat":
                if call.data == 'soglasitsya':
                    with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
                    for i in data:
                        if i['id']==str(call.message.chat.id) and i['type']=='sert':
                            if(int(i['balans'])==0):
                                get_sogl(call.message)
                                bot.delete_message(call.message.chat.id,
                                        call.message.message_id)
                            else:
                                bot.send_message(
                                    call.message.chat.id, listVybrana[langNumber1[0]] + user_data['balans'])
                        elif i['id']==str(call.message.chat.id) and i['type']=='chast':
                            bot.delete_message(call.message.chat.id,
                                        call.message.message_id)
                            i['dengi_count']['count_5000'] = i['dengi_count']['count_5000'] + int(
                                int(i['balans'])/5000)
                            i['dengi'] = i['dengi'] + int(i['balans'])
                            i['balans'] = "0"
                            save_fo(data)
                            get_sogl(call.message)
                            bot.edit_message_reply_markup(
                                call.from_user.id, call.message.message_id, reply_markup=None)

                elif call.data == 'delete':
                    clear_cart(call.message)
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    bot.answer_callback_query(
                        callback_query_id=call.id, text=listDeleted[langNumber1[0]])
                    get_korzina(call.message)
                elif call.data == "redaktirovat":
                    get_delete(call.message)
                    bot.delete_message(call.message.chat.id,
                                       call.message.message_id)
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
            elif call.data == "dengi_delete" or call.data == "mel-sertificaty" or call.data == "mar-sertificaty" or call.data == "lc-sertificaty" or call.data == "back":
                if call.data == 'dengi_delete':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'dengi_count'
                    user_data['lok'] = b
                    user_data['dengi_count']['type_nominal'] = "5000"
                    add_and_delete(call.message)
                elif call.data == 'mel-sertificaty':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'sportmaster_count'
                    user_data['lok'] = b
                    get_nominal(call.message)
                elif call.data == 'mar-sertificaty':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'mechta_count'
                    user_data['lok'] = b
                    get_nominal(call.message)
                elif call.data == 'lc-sertificaty':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    b = 'lcwaikiki_count'
                    user_data['lok'] = b
                    get_nominal(call.message)
                elif call.data == "back":
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    get_korzina(call.message)
            elif call.data == "plus" or call.data == "minus" or call.data == 'enough' or call.data == 'delete_full' or call.data == 'korzina_add_and_delete' or call.data == 'get_all_babki':
                with open('result.json', encoding='utf-8') as file:
                    data = json.load(file)
                if call.data == 'plus':
                    add_plus(call.message, call)
                elif call.data == 'minus':
                    delete_minus(call.message, call)
                elif call.data == 'enough':
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    bot.delete_message(call.message.chat.id,
                                       call.message.message_id)
                    with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
                    for i in data:
                        if i['id'] == str(call.message.chat.id) and i['lok'] == 'sportmaster_count':
                            bot.delete_message(
                                call.message.chat.id, call.message.message_id-1)
                            get_sertificat(call.message)
                        elif i['id'] == str(call.message.chat.id) and i['lok'] == 'mechta_count':
                            bot.delete_message(
                                call.message.chat.id, call.message.message_id-1)
                            get_sertificat(call.message)
                        elif i['id'] == str(call.message.chat.id) and i['lok'] == 'lcwaikiki_count':
                            bot.delete_message(
                                call.message.chat.id, call.message.message_id-1)
                            get_sertificat(call.message)
                        elif i['id'] == str(call.message.chat.id) and i['lok'] == 'abdi_count':
                            bot.delete_message(
                                call.message.chat.id, call.message.message_id-1)
                            get_sertificat(call.message)
                elif call.data == 'delete_full':
                    bot.delete_message(call.message.chat.id,
                                       call.message.message_id)
                    with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
                    for i in data:
                        if i['id'] == str(call.message.chat.id):
                            if(i[i['lok']]['type_nominal'] == "5000"):
                                i['balans'] = str(int(
                                    i['balans']) + i[i['lok']]['count_5000']*5000)
                                i[i['lok']]['count_5000'] = 0
                            if(i[i['lok']]['type_nominal'] == "10000"):
                                i['balans'] = str(int(
                                    i['balans']) + i[i['lok']]['count_10000']*10000)
                                i[i['lok']]['count_10000'] = 0
                            elif(i[i['lok']]['type_nominal'] == "15000"):
                                i['balans'] = str(int(
                                    i['balans']) + i[i['lok']]['count_15000']*15000)
                                i[i['lok']]['count_15000'] = 0
                            elif(i[i['lok']]['type_nominal'] == "25000"):
                                i['balans'] = str(int(
                                    i['balans']) + i[i['lok']]['count_25000']*25000)
                                i[i['lok']]['count_25000'] = 0
                    save_fo(data)
                    get_sertificat(call.message)    
                elif call.data == 'korzina_add_and_delete':
                    bot.delete_message(call.message.chat.id,
                                       call.message.message_id)
                    get_korzina(call.message)
                elif call.data == 'get_all_babki':
                    user_data['dengi_count']['count_5000'] = user_data['dengi_count']['count_5000'] + (
                        int(user_data['balans'])/5000)
                    user_data['dengi'] = user_data['dengi'] + \
                        int(user_data['balans'])
                    user_data['balans'] = "0"
                    if(user_data[user_data['lok']]['type_nominal'] == "10000"):
                        price = str(int(user_data[user_data['lok']]
                                    ['count_10000'] * 10000)) + 'тг'
                        shtuk = str(
                            int(user_data[user_data['lok']]['count_10000']))
                    elif(user_data[user_data['lok']]['type_nominal'] == "15000"):
                        price = str(int(user_data[user_data['lok']]
                                    ['count_15000'] * 15000)) + 'тг'
                        shtuk = str(
                            int(user_data[user_data['lok']]['count_15000']))
                    elif(user_data[user_data['lok']]['type_nominal'] == "25000"):
                        price = str(int(user_data[user_data['lok']]
                                    ['count_25000'] * 25000)) + 'тг'
                        shtuk = str(
                            int(user_data[user_data['lok']]['count_25000']))
                    elif(user_data[user_data['lok']] == user_data['dengi_count']):
                        if(int(user_data[user_data['lok']]['type_nominal'] == "5000")):
                            price = str(int(
                                user_data[user_data['lok']]['count_5000'] * 5000)) + 'тг'
                            shtuk = str(int(
                                user_data[user_data['lok']]['count_5000']))

                    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
                    callback_button1 = telebot.types.InlineKeyboardButton(
                        text='➕', callback_data='plus',)
                    callback_button2 = telebot.types.InlineKeyboardButton(
                        text=shtuk + 'шт.- ' + price, callback_data='howmany')
                    callback_button3 = telebot.types.InlineKeyboardButton(
                        text='➖', callback_data='minus')
                    callback_button4 = telebot.types.InlineKeyboardButton(
                        text=listTagyKosu[langNumber1[0]], callback_data='enough')
                    callback_button5 = telebot.types.InlineKeyboardButton(
                        text='❌', callback_data='delete_full')
                    callback_button6 = telebot.types.InlineKeyboardButton(
                        text=listOstatok[langNumber1[0]] + user_data['balans'] + "тг", callback_data='balans')
                    callback_button7 = telebot.types.InlineKeyboardButton(
                        text='Корзина'+'\U0001F5D1', callback_data='korzina_add_and_delete')
                    callback_button8 = telebot.types.InlineKeyboardButton(
                        text='Забрать все деньгами 💵', callback_data='get_all_babki')
                    keyboard.add(callback_button6)
                    keyboard.add(callback_button2)
                    keyboard.row(callback_button5,
                                 callback_button3, callback_button1)
                    keyboard.add(callback_button8)
                    keyboard.add(callback_button4)
                    keyboard.add(callback_button7)
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=keyboard)

            elif call.data == "yes" or call.data == "no":
                if call.data == 'yes':
                    with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
                    for i in data:
                        if(i['id']==str(call.message.chat.id)):
                            i['save'] = True
                            i['dengi'] = int(
                                i['balans']) + i['dengi']
                            i['balans'] = '0'
                            counts = {
                                'sportmaster_count': {"Номанал 5000": i['sportmaster_count']['count_5000'],"Номанал 10000": i['sportmaster_count']['count_10000'], "Номанал 15000": i['sportmaster_count']['count_15000'], "Номанал 25000": i['sportmaster_count']['count_25000']},
                                'mechta_count': {"Номанал 5000": i['mechta_count']['count_5000'],"Номанал 10000": i['mechta_count']['count_10000'], "Номанал 15000": i['mechta_count']['count_15000'], "Номанал 25000": i['mechta_count']['count_25000']},
                                'lcwaikiki_count': {"Номанал 5000": i['lcwaikiki_count']['count_5000'],"Номанал 10000": i['lcwaikiki_count']['count_10000'], "Номанал 15000": i['lcwaikiki_count']['count_15000'], "Номанал 25000": i['lcwaikiki_count']['count_25000']},
                                'abdi_count': {"Номанал 5000": i['abdi_count']['count_5000'],"Номанал 10000": i['abdi_count']['count_10000'], "Номанал 15000": i['abdi_count']['count_15000'], "Номанал 25000": i['abdi_count']['count_25000']},
                            }
                            i['itogo'] = i['count_deti']*45000
                            del i['mechta_count']['type_nominal']
                            del i['lcwaikiki_count']['type_nominal']
                            del i['sportmaster_count']['type_nominal']
                            del i['abdi_count']['type_nominal']
                            with open('result.json', "w", encoding='utf8') as f:
                                f.write(json.dumps(data, ensure_ascii=False))
                            bot.edit_message_reply_markup(
                                call.from_user.id, call.message.message_id, reply_markup=None)
                            bot.answer_callback_query(
                                callback_query_id=call.id, text=listGoodByeSuccess[langNumber1[0]])
                            get_saved_person_for_excel(call.message,counts)
                            keyboard = telebot.types.ReplyKeyboardMarkup(
                                resize_keyboard=True)
                            callback_button1 = telebot.types.KeyboardButton(
                                ChecklastMess[langNumber1[0]])
                            keyboard.add(callback_button1)
                            bot.send_message(
                                call.message.chat.id, listGoodBye[langNumber1[0]], reply_markup=keyboard)
                    with open('result.json', "w", encoding='utf8') as f:
                        f.write(json.dumps(data, ensure_ascii=False))
                elif call.data == 'no':
                    with open('result.json', encoding='utf-8') as file:
                        data = json.load(file)
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    bot.answer_callback_query(
                        callback_query_id=call.id, text=listUnSuccess[langNumber1[0]]+'\U0001F614')
                    for i in data:
                        if(i['id'] == str(call.message.chat.id)):
                            i['balans'] = str(int(i['balans']) + i['dengi'] +
                                                    + i['sportmaster_count']['count_10000'] * 10000
                                                    + i['mechta_count']['count_10000'] * 10000
                                                    + i['lcwaikiki_count']['count_10000'] * 10000
                                                    + i['abdi_count']['count_10000'] * 10000
                                                    + i['sportmaster_count']['count_15000'] * 15000
                                                    + i['mechta_count']['count_15000'] * 15000
                                                    + i['lcwaikiki_count']['count_15000'] * 15000
                                                    + i['abdi_count']['count_15000'] * 15000
                                                    + i['sportmaster_count']['count_25000'] * 25000
                                                    + i['mechta_count']['count_25000'] * 25000
                                                    + i['lcwaikiki_count']['count_25000'] * 25000
                                                    + i['abdi_count']['count_25000'] * 25000
                                                    + i['sportmaster_count']['count_5000'] * 5000
                                                    + i['mechta_count']['count_5000'] * 5000
                                                    + i['lcwaikiki_count']['count_5000'] * 5000
                                                    + i['abdi_count']['count_5000'] * 5000
                                                    )
                            i['dengi'] = 0
                            i['dengi_count']['count_5000'] = 0
                            i['dengi_count']['count_10000'] = 0
                            i['dengi_count']['count_15000'] = 0
                            i['dengi_count']['count_25000'] = 0
                            i['sportmaster_count']['count_5000'] = 0
                            i['mechta_count']['count_5000'] = 0
                            i['lcwaikiki_count']['count_5000'] = 0
                            i['abdi_count']['count_5000'] = 0
                            i['sportmaster_count']['count_10000'] = 0
                            i['mechta_count']['count_10000'] = 0
                            i['lcwaikiki_count']['count_10000'] = 0
                            i['abdi_count']['count_10000'] = 0
                            i['sportmaster_count']['count_15000'] = 0
                            i['mechta_count']['count_15000'] = 0
                            i['lcwaikiki_count']['count_15000'] = 0
                            i['abdi_count']['count_15000'] = 0
                            i['sportmaster_count']['count_25000'] = 0
                            i['mechta_count']['count_25000'] = 0
                            i['lcwaikiki_count']['count_25000'] = 0
                            i['abdi_count']['count_25000'] = 0
                    save_fo(data)
                    get_cart(call.message)
            elif call.data == "rus" or call.data == "kz":
                with open('result.json', encoding='utf-8') as file:
                    data = json.load(file)
                if call.data == "rus":
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None,)
                    for i in data:
                        if(i['id'] == str(call.message.chat.id)):
                            i['lang'] = listLang[0]
                            langNumber1[0] = 0
                            bot.answer_callback_query(
                                callback_query_id=call.id, text=listLangChange[langNumber1[0]] + '✅')
                            get_cart(call.message)
                elif call.data == "kz":
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None)
                    for i in data:
                        if(i['id'] == str(call.message.chat.id)):
                            i['lang'] = listLang[1]
                            langNumber1[0] = 1
                            bot.answer_callback_query(
                                callback_query_id=call.id, text=listLangChange[langNumber1[0]] + '✅')
                            get_cart(call.message)
            elif call.data == "5000" or call.data == "10000" or call.data == "15000" or call.data == "25000" or call.data == "5000":
                with open('result.json', encoding='utf-8') as file:
                    data = json.load(file)
                if call.data == "10000":
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None,)
                    for i in data:
                        if i['id']==str(call.message.chat.id):
                            i[i['lok']]['type_nominal'] = "10000"
                    save_fo(data)
                    add_and_delete(call.message)
                elif call.data == "15000":
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None,)
                    for i in data:
                        if i['id']==str(call.message.chat.id):
                            i[i['lok']]['type_nominal'] = "15000"
                    save_fo(data)
                    add_and_delete(call.message)
                elif call.data == "25000":
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None,)
                    for i in data:
                        if i['id']==str(call.message.chat.id):
                            i[i['lok']]['type_nominal'] = "25000"
                    save_fo(data)
                    add_and_delete(call.message)
                elif call.data == "5000":
                    bot.edit_message_reply_markup(
                        call.from_user.id, call.message.message_id, reply_markup=None,)
                    for i in data:
                        if i['id']==str(call.message.chat.id):
                            i[i['lok']]['type_nominal'] = "5000"
                    save_fo(data)
                    add_and_delete(call.message)
            elif call.data == "kaspi" or call.data == "halyk" or call.data == "another":
                with open('result.json', encoding='utf-8') as file:
                    data = json.load(file)
                if call.data == "kaspi":
                    bot.edit_message_reply_markup(
                                        call.from_user.id, call.message.message_id, reply_markup=None)
                    for i in data:
                        if i['id']==str(call.message.chat.id):
                            i['cart_type'] = "Каспи Банк"
                    save_fo(data)
                    get_cart(call.message)
                if call.data == "halyk":
                    bot.edit_message_reply_markup(
                                        call.from_user.id, call.message.message_id, reply_markup=None)
                    for i in data:
                        if i['id']==str(call.message.chat.id):
                            i['cart_type'] = "Народный Банк"
                    save_fo(data)
                    get_cart(call.message)
                if call.data == "another":
                    bot.edit_message_reply_markup(
                                        call.from_user.id, call.message.message_id, reply_markup=None)
                    for i in data:
                        if i['id']==str(call.message.chat.id):
                            i['cart_type'] = "Другой Банк"
                    save_fo(data)
                    get_cart(call.message)
                for i in data:
                    if i['id']==str(call.message.chat.id):
                        bot.edit_message_text(
                            chat_id=call.message.chat.id, message_id=call.message.message_id, text=listLangDef[langNumber1[0]] +  i['cart_type'])
        
                    

        except Exception as ex:
            print(ex)

def get_bank(message):
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='Каспи Банк', callback_data='kaspi',)
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Народный Банк', callback_data='halyk')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='Другой Банк', callback_data='another')
    keyboard.add(callback_button1,callback_button2,callback_button3)
    bot.send_message(message.chat.id, listBankDer[langNumber1[0]], reply_markup=keyboard)


def repeat_start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    callback_button1 = telebot.types.KeyboardButton(
        ChecklastMess[langNumber1[0]])
    keyboard.add(callback_button1)
    bot.send_message(
        message.chat.id, get_info_only_exists(message), reply_markup=keyboard, parse_mode="HTML")
    bot.send_message(
        message.chat.id, listGoodBye[langNumber1[0]], reply_markup=keyboard)





@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == ChecklastMess[langNumber1[0]]:
        repeat_start(message)
    elif message.text == listChangeLang[langNumber1[0]]+'🔠':
        change_lang(message)
    elif message.text == listMoney[langNumber1[0]]:
        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)
        for i in data:
            if(i['id']==str(message.chat.id)):
                i['dengi'] = int(i['balans']) + int(i['dengi'])
                i['balans'] = "0"
                i['type'] = 'mmoney'
        with open('result.json', "w", encoding='utf8') as f:
                        f.write(json.dumps(data, ensure_ascii=False))
        get_sogl(message)
    elif message.text == "Сертификаты📃":
        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)
        for i in data:
            if(i['id']==str(message.chat.id)):
                i['type'] = 'sert'
        save_fo(data)
        get_sertificat(message)
    elif message.text == listPart[langNumber1[0]]:
        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)
        for i in data:
            if(i['id']==str(message.chat.id)):
                i['type'] = 'chast'
        save_fo(data)
        get_sertificat(message)
    elif message.text == "Старт":
        lang(message)


def get_help_by_filial(city, message):
    listOpros = ['2) По подтвержденным данным  пройдите опрос','2) Расталған деректер бойынша сауалнамадан өтіңіз']
    listnesogl = ['1) Если вы не согласны с данными, ','1) Егер сіз деректермен келіспесеңіз, ']
    string = '\n\n' + listOpros[langNumber1[0]]
    nesogl = '\n' + listnesogl[langNumber1[0]]
    if(city.replace(" ", "") == "Актобе"):
        listHelpAktobe = ['обратитесь по нижеуказанным номерам:\n\n     Аекенова Жанаргуль Амантаевна\n     +7-7132-974-592\n     +7-701-473-40-97',
                          'төмендегі нөмірлерге хабарласыңыз:\n\n     Аекенова Жанаргуль Амантаевна\n     +7-7132-974-592\n     +7-701-473-40-97']
        return nesogl + listHelpAktobe[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Алматы"):
        listHelpAlmaty = ['обратитесь по нижеуказанным номерам:\n\n     Жаниязова Клара Лепесовна\n     +7-7272-965-312\n     +7-701-985-89-63',
                          'төмендегі нөмірлерге хабарласыңыз:\n\n     Жаниязова Клара Лепесовна\n     +7-7272-965-312\n     +7-701-985-89-63']
        return nesogl + listHelpAlmaty[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Астана"):
        listHelpAstana = ['обратитесь по нижеуказанным номерам:\n\n     Рахманкулова Дина Советовна\n     +7-7172-600-035\n     +7-701-604-15-73',
                          'төмендегі нөмірлерге хабарласыңыз:\n\n     Рахманкулова Дина Советовна\n     +7-7172-600-035\n     +7-701-604-15-73']
        return nesogl + listHelpAstana[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Атырау"):
        listHelpAtyrau = ['обратитесь по нижеуказанным номерам:\n\n     Косдаулетова Гульшарбат Урингалиевна\n     +7-7122-953-549\n     +7-701-125-48-17',
                          'төмендегі нөмірлерге хабарласыңыз:\n\n     Косдаулетова Гульшарбат Урингалиевна\n     +7-7122-953-549\n     +7-701-125-48-17']
        return nesogl + listHelpAtyrau[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Актау"):
        listHelpAktau = ['обратитесь по нижеуказанным номерам:\n\n     Нурмагамбетова Жанат\n     +7-7292-462-345\n     +7-778-012-88-55',
                         'төмендегі нөмірлерге хабарласыңыз:\n\n     Нурмагамбетова Жанат\n     +7-7292-462-345\n     +7-778-012-88-55']
        return nesogl + listHelpAktau[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Жамбыл"):
        listHelpZhambyl = ['обратитесь по нижеуказанным номерам:\n\n     Алимбетова Светлана Альжановна\n     +7-7262-961-235\n     +7-747-543-14-20',
                           'төмендегі нөмірлерге хабарласыңыз:\n\n     Алимбетова Светлана Альжановна\n     +7-7262-961-235\n     +7-747-543-14-20']
        return nesogl + listHelpZhambyl[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Караганды"):
        listHelpKaraganda = ['обратитесь по нижеуказанным номерам:\n\n     Машрапова Арайлым\n     +7-7212-604-505\n     +7-700-966-49-15',
                             'төмендегі нөмірлерге хабарласыңыз:\n\n     Машрапова Арайлым\n     +7-7212-604-505\n     +7-700-966-49-15']
        return nesogl + listHelpKaraganda[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Кокшетау"):
        listHelpKokshetau = ['обратитесь по нижеуказанным номерам:\n\n     Абильмажинова Айгуль\n     +7-7262-293-433\n     +7-707-224 48-03',
                             'төмендегі нөмірлерге хабарласыңыз:\n\n     Абильмажинова Айгуль\n     +7-7262-293-433\n     +7-707-224-48-03']
        return nesogl + listHelpKokshetau[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Костанай"):
        listHelpKostanay = ['обратитесь по нижеуказанным номерам:\n\n     Курманкина Куаныш Атымтаевна\n     +7-7142-900-772\n     +7-777-998-16-18',
                            'төмендегі нөмірлерге хабарласыңыз:\n\n     Курманкина Куаныш Атымтаевна\n     +7-7142-900-772\n     +7-777-998-16-18']
        return nesogl + listHelpKostanay[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Кызылорда"):
        listHelpKyzylorda = ['обратитесь по нижеуказанным номерам:\n\n     Алматова Зауре Орынбасаровна\n     +7-7242-292-504\n     +7-776-864-39-13',
                             'төмендегі нөмірлерге хабарласыңыз:\n\n     Алматова Зауре Орынбасаровна\n     +7-7242-292-504\n     +7-776-864-39-13']
        return nesogl + listHelpKyzylorda[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Павлодар"):
        listHelpPavlodar = ['обратитесь по нижеуказанным номерам:\n\n     Алькенева Гульмира Каннасыровна\n     +7-7182-372-223\n     +7-702-223-62-65',
                            'төмендегі нөмірлерге хабарласыңыз:\n\n     Алькенева Гульмира Каннасыровна\n     +7-7182-372-223\n     +7-702-223-62-65']
        return nesogl + listHelpPavlodar[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Оскемен"):
        listHelpOskemen = ['обратитесь по нижеуказанным номерам:\n\n     Акежанова Клара Муздыбаевна\n     +7-7232-502-732\n     +7-778-735-25-92',
                           'төмендегі нөмірлерге хабарласыңыз:\n\n     Акежанова Клара Муздыбаевна\n     +7-7232-502-732\n     +7-778-735-25-92']
        return nesogl + listHelpOskemen[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Семей"):
        listHelpSemey = ['обратитесь по нижеуказанным номерам:\n\n     Зейнелгазинова Мадина Серикказыевна\n     +7-7222-380-144\n     +7-747-743-23-98',
                         'төмендегі нөмірлерге хабарласыңыз:\n\n     Зейнелгазинова Мадина Серикказыевна\n     +7-7222-380-144\n     +7-747-743-23-98']
        return nesogl + listHelpSemey[langNumber1[0]] + string
    elif(city.replace(" ", "") == "Шымкент"):
        listHelpShymkent = ['обратитесь по нижеуказанным номерам:\n\n     Бердыбаева Лазат Егизбаевна\n     +7-7252-953-122\n     +7-701-648-47-60',
                            'төмендегі нөмірлерге хабарласыңыз:\n\n     Бердыбаева Лазат Егизбаевна\n     +7-7252-953-122\n     +7-701-648-47-60']
        return nesogl + listHelpShymkent[langNumber1[0]] + string
    else:
        listHelpCenter = ['обратитесь по нижеуказанным номерам:\n\n     Бейпилбаева Сауле Боранбаевна\n     +7-7172-610-767\n     +7-777-610-68-41',
                          'төмендегі нөмірлерге хабарласыңыз:\n\n     Бейпилбаева Сауле Боранбаевна\n     +7-7172-610-767\     +7-777-610-68-41']
        return nesogl + listHelpCenter[langNumber1[0]] + string


def change_lang(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listLang[0], callback_data='rus')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text=listLang[1], callback_data='kz')
    keyboard.add(callback_button1, callback_button2)
    bot.send_message(message.from_user.id,
                     '<b>Выберите язык:\nТілді таңдаңыз:\n</b>', reply_markup=keyboard, parse_mode="HTML")


def add_plus(message, call):
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    try:
        for i in data:
            if(i['id'] == str(message.chat.id)):
                i['count_plus'] = 0
                krange = i['count_plus'] * \
                    int(i[i['lok']]['type_nominal'])
                if(int(i['balans'])-krange > 0):
                    if(i[i['lok']]['type_nominal'] == "10000"):
                        if(int(i['balans']) >= 10000):
                            i['count_plus'] = i['count_plus'] + 1
                            i[i['lok']
                                    ]['count_10000'] = i[i['lok']]['count_10000'] + 1
                        else:
                            bot.answer_callback_query(
                                callback_query_id=call.id, text=listNotEnough[langNumber1[0]])
                    elif(i[i['lok']]['type_nominal'] == "15000"):
                        if(int(i['balans']) >= 15000):
                            i['count_plus'] = i['count_plus'] + 1
                            i[i['lok']
                                    ]['count_15000'] = i[i['lok']]['count_15000'] + 1
                        else:
                            bot.answer_callback_query(
                                callback_query_id=call.id, text=listNotEnough[langNumber1[0]])
                    elif(i[i['lok']]['type_nominal'] == "25000"):
                        if(int(i['balans']) >= 25000):
                            i[i['lok']
                                    ]['count_25000'] = i[i['lok']]['count_25000'] + 1
                            i['count_plus'] = i['count_plus'] + 1
                        else:
                            bot.answer_callback_query(
                                callback_query_id=call.id, text=listNotEnough[langNumber1[0]])
                    elif(i[i['lok']]['type_nominal'] == "5000"):
                        if(int(i['balans']) >= 5000):
                            i[i['lok']
                                    ]['count_5000'] = i[i['lok']]['count_5000'] + 1
                            i['count_plus'] = i['count_plus'] + 1
                        else:
                            bot.answer_callback_query(
                                callback_query_id=call.id, text=listNotEnough[langNumber1[0]])
                else:
                    bot.answer_callback_query(
                        callback_query_id=call.id, text=listNotEnough[langNumber1[0]])
    except Exception as ex:
        print(ex)

    save_fo(data)
    for i in data:
        if(i['id'] == str(message.chat.id)):
            count_plus = i['count_plus']
            count_minus = i['count_minus']
            price1 = 0
            price2 = 0
            if((type(int(count_plus)) == int) and (type(int(count_minus)) == int)):
                if(i[i['lok']]['type_nominal'] == "10000"):
                    price1 = int(count_plus) * 10000
                    price2 = int(count_minus) * 10000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "15000"):
                    price1 = int(count_plus) * 15000
                    price2 = int(count_minus) * 15000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "25000"):
                    price1 = int(count_plus) * 25000
                    price2 = int(count_minus) * 25000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "5000"):
                    price1 = int(count_plus) * 5000
                    price2 = int(count_minus) * 5000
                    i['balans'] = str(int(i['balans'])+price2)

                if(int(i['balans']) >= int(price1)):
                    i['balans'] = str(int(i['balans'])-price1)
                    # user_data['sportmaster_count'] = user_data['sportmaster_count'] + \
                    #     int(count)
                    i['count_plus'] = 0
                    i['count_minus'] = 0
                    # print(user_data)
                else:
                    print("Ошибка")
    save_fo(data)
    for i in data:
        if(i['id']==str(call.message.chat.id)):
            if(i[i['lok']]['type_nominal'] == "5000"):
                price = str(i[i['lok']]
                            ['count_5000'] * 5000) + 'тг'
                shtuk = str(i[i['lok']]['count_5000'])
            elif(i[i['lok']]['type_nominal'] == "10000"):
                price = str(i[i['lok']]
                            ['count_10000'] * 10000) + 'тг'
                shtuk = str(i[i['lok']]['count_10000'])
            elif(i[i['lok']]['type_nominal'] == "15000"):
                price = str(i[i['lok']]
                            ['count_15000'] * 15000) + 'тг'
                shtuk = str(i[i['lok']]['count_15000'])
            elif(i[i['lok']]['type_nominal'] == "25000"):
                price = str(i[i['lok']]
                            ['count_25000'] * 25000) + 'тг'
                shtuk = str(i[i['lok']]['count_25000'])
            elif(i[i['lok']] == i['dengi_count']):
                if(i[i['lok']]['type_nominal'] == "5000"):
                    price = str(
                        i[i['lok']]['count_5000'] * 5000) + 'тг'
                    shtuk = str(
                        i[i['lok']]['count_5000'])
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
            callback_button1 = telebot.types.InlineKeyboardButton(
                text='➕', callback_data='plus',)
            callback_button2 = telebot.types.InlineKeyboardButton(
                text=shtuk + 'шт.- ' + price, callback_data='howmany')
            callback_button3 = telebot.types.InlineKeyboardButton(
                text='➖', callback_data='minus')
            callback_button4 = telebot.types.InlineKeyboardButton(
                text=listTagyKosu[langNumber1[0]], callback_data='enough')
            callback_button5 = telebot.types.InlineKeyboardButton(
                text='❌', callback_data='delete_full')
            callback_button6 = telebot.types.InlineKeyboardButton(
                text=listOstatok[langNumber1[0]] + i['balans'] + "тг", callback_data='balans')
            callback_button7 = telebot.types.InlineKeyboardButton(
                text=listAccept[langNumber1[0]], callback_data='soglasitsya')
            callback_button8 = telebot.types.InlineKeyboardButton(
                text=listVashaSumma[langNumber1[0]] + str(i['count_deti']*45000) + 'тг', callback_data='balans')
            if(i['balans'] == str(i['count_deti']*45000)):
                keyboard.add(callback_button8)
                keyboard.add(callback_button2)
                keyboard.row(callback_button1,
                            callback_button3, callback_button5)
                keyboard.add(callback_button7)
                keyboard.add(callback_button4)
            else:
                keyboard.add(callback_button8)
                keyboard.add(callback_button6)
                keyboard.add(callback_button2)
                keyboard.row(callback_button1,
                            callback_button3, callback_button5)
                keyboard.add(callback_button7)
                keyboard.add(callback_button4)
            bot.edit_message_reply_markup(
                call.from_user.id, call.message.message_id, reply_markup=keyboard)



def delete_minus(message, call):
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    try:
        for i in data:
            if(i[i['lok']]['type_nominal'] == "10000"):
                if(i[i['lok']]['count_10000'] > 0):
                    i['count_minus'] = i['count_minus']+1
                    i[i['lok']
                            ]['count_10000'] = i[i['lok']]['count_10000'] - 1
                elif(i[i['lok']]['count_10000'] == 0):
                    bot.answer_callback_query(
                        callback_query_id=call.id, text='Невозможно меньше нуля')
            elif(i[i['lok']]['type_nominal'] == "15000"):
                if(i[i['lok']]['count_15000'] > 0):
                    i['count_minus'] = i['count_minus']+1
                    i[i['lok']
                            ]['count_15000'] = i[i['lok']]['count_15000'] - 1
                elif(i[i['lok']]['count_15000'] == 0):
                    bot.answer_callback_query(
                        callback_query_id=call.id, text='Невозможно меньше нуля')
            elif(i[i['lok']]['type_nominal'] == "25000"):
                if(i[i['lok']]['count_25000'] > 0):
                    i['count_minus'] = i['count_minus']+1
                    i[i['lok']
                            ]['count_25000'] = i[i['lok']]['count_25000'] - 1
                elif(i[i['lok']]['count_25000'] == 0):
                    bot.answer_callback_query(
                        callback_query_id=call.id, text='Невозможно меньше нуля')
            elif(i[i['lok']]['type_nominal'] == "5000"):
                if(i[i['lok']]['count_5000'] > 0):
                    i['count_minus'] = i['count_minus']+1
                    i[i['lok']
                            ]['count_5000'] = i[i['lok']]['count_5000'] - 1
                elif(i[i['lok']]['count_5000'] == 0):
                    bot.answer_callback_query(
                        callback_query_id=call.id, text='Невозможно меньше нуля')
    except Exception as ex:
        print(ex)
    save_fo(data)
    for i in data:
        if(i['id'] == str(message.chat.id)):
            count_plus = i['count_plus']
            count_minus = i['count_minus']
            price1 = 0
            price2 = 0
            if((type(int(count_plus)) == int) and (type(int(count_minus)) == int)):
                if(i[i['lok']]['type_nominal'] == "10000"):
                    price1 = int(count_plus) * 10000
                    price2 = int(count_minus) * 10000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "15000"):
                    price1 = int(count_plus) * 15000
                    price2 = int(count_minus) * 15000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "25000"):
                    price1 = int(count_plus) * 25000
                    price2 = int(count_minus) * 25000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "5000"):
                    price1 = int(count_plus) * 5000
                    price2 = int(count_minus) * 5000
                    i['balans'] = str(int(i['balans'])+price2)

                if(int(i['balans']) >= int(price1)):
                    i['balans'] = str(int(i['balans'])-price1)
                    # user_data['sportmaster_count'] = user_data['sportmaster_count'] + \
                    #     int(count)
                    i['count_plus'] = 0
                    i['count_minus'] = 0
                    # print(user_data)
                else:
                    print("Ошибка")
    save_fo(data)
    for i in data:
        if(i['id']==str(call.message.chat.id)):
            if(i[i['lok']]['type_nominal'] == "5000"):
                price = str(i[i['lok']]
                            ['count_5000'] * 5000) + 'тг'
                shtuk = str(i[i['lok']]['count_5000'])
            elif(i[i['lok']]['type_nominal'] == "10000"):
                price = str(i[i['lok']]
                            ['count_10000'] * 10000) + 'тг'
                shtuk = str(i[i['lok']]['count_10000'])
            elif(i[i['lok']]['type_nominal'] == "15000"):
                price = str(i[i['lok']]
                            ['count_15000'] * 15000) + 'тг'
                shtuk = str(i[i['lok']]['count_15000'])
            elif(i[i['lok']]['type_nominal'] == "25000"):
                price = str(i[i['lok']]
                            ['count_25000'] * 25000) + 'тг'
                shtuk = str(i[i['lok']]['count_25000'])
            elif(i[i['lok']] == i['dengi_count']):
                if(i[i['lok']]['type_nominal'] == "5000"):
                    price = str(
                        i[i['lok']]['count_5000'] * 5000) + 'тг'
                    shtuk = str(
                        i[i['lok']]['count_5000'])
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
            callback_button1 = telebot.types.InlineKeyboardButton(
                text='➕', callback_data='plus',)
            callback_button2 = telebot.types.InlineKeyboardButton(
                text=shtuk + 'шт.- ' + price, callback_data='howmany')
            callback_button3 = telebot.types.InlineKeyboardButton(
                text='➖', callback_data='minus')
            callback_button4 = telebot.types.InlineKeyboardButton(
                text=listTagyKosu[langNumber1[0]], callback_data='enough')
            callback_button5 = telebot.types.InlineKeyboardButton(
                text='❌', callback_data='delete_full')
            callback_button6 = telebot.types.InlineKeyboardButton(
                text=listOstatok[langNumber1[0]] + i['balans'] + "тг", callback_data='balans')
            callback_button7 = telebot.types.InlineKeyboardButton(
                text=listAccept[langNumber1[0]], callback_data='soglasitsya')
            callback_button8 = telebot.types.InlineKeyboardButton(
                text=listVashaSumma[langNumber1[0]] + str(i['count_deti']*45000) + 'тг', callback_data='balans')
            if(i['balans'] == str(i['count_deti']*45000)):
                keyboard.add(callback_button8)
                keyboard.add(callback_button2)
                keyboard.row(callback_button1,
                            callback_button3, callback_button5)
                keyboard.add(callback_button7)
                keyboard.add(callback_button4)
            else:
                keyboard.add(callback_button8)
                keyboard.add(callback_button6)
                keyboard.add(callback_button2)
                keyboard.row(callback_button1,
                            callback_button3, callback_button5)
                keyboard.add(callback_button7)
                keyboard.add(callback_button4)
            bot.edit_message_reply_markup(
                call.from_user.id, call.message.message_id, reply_markup=keyboard)



def get_dengi(message):
    global count_plus
    global count_minus
    count_plus = info_data['count_plus']
    count_minus = info_data['count_minus']
    price1 = 0
    price2 = 0
    try:
        if((type(int(count_plus)) == int) and (type(int(count_minus)) == int)):
            if(user_data[user_data['lok']]['type_nominal'] == "10000"):
                price1 = int(count_plus) * 10000
                price2 = int(count_minus) * 10000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "15000"):
                price1 = int(count_plus) * 15000
                price2 = int(count_minus) * 15000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "25000"):
                price1 = int(count_plus) * 25000
                price2 = int(count_minus) * 25000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "5000"):
                price1 = int(count_plus) * 5000
                price2 = int(count_minus) * 5000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            if(int(user_data['balans']) >= int(price1)):
                user_data['balans'] = str(int(user_data['balans'])-price1)
                # user_data['sportmaster_count'] = user_data['sportmaster_count'] + \
                #     int(count)
                user_data['dengi'] = user_data['dengi'] + price1-price2
                info_data['count_plus'] = 0
                info_data['count_minus'] = 0
                save_data(user_data)
                # print(user_data)
            else:
                print("Ошибка")
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id,
                         listDontUnderstand[langNumber1[0]]+'\U0001F914')
        get_cart(message)



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
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listYes[langNumber1[0]], callback_data='yes')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text=listNo[langNumber1[0]], callback_data='no')
    keyboard.add(callback_button1, callback_button2)
    bot.send_message(message.chat.id, get_info_only_exists(message) +
                     '\n\n', parse_mode="HTML")
    bot.send_message(
        message.chat.id, listEndAccept[langNumber1[0]], reply_markup=keyboard, parse_mode="HTML")


def get_meloman_sert(message):
    global count_plus
    global count_minus
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    for i in data:
        if(i['id']==str(message.chat.id)):
            count_plus = i['count_plus']
            count_minus = i['count_minus']
            price1 = 0
            price2 = 0
            if((type(int(count_plus)) == int) and (type(int(count_minus)) == int)):
                if(i[i['lok']]['type_nominal'] == "10000"):
                    price1 = int(count_plus) * 10000
                    price2 = int(count_minus) * 10000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "15000"):
                    price1 = int(count_plus) * 15000
                    price2 = int(count_minus) * 15000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "25000"):
                    price1 = int(count_plus) * 25000
                    price2 = int(count_minus) * 25000
                    i['balans'] = str(int(i['balans'])+price2)
                elif(i[i['lok']]['type_nominal'] == "5000"):
                    price1 = int(count_plus) * 5000
                    price2 = int(count_minus) * 5000
                    i['balans'] = str(int(i['balans'])+price2)

                if(int(i['balans']) >= int(price1)):
                    i['balans'] = str(int(i['balans'])-price1)
                    # user_data['sportmaster_count'] = user_data['sportmaster_count'] + \
                    #     int(count)
                    info_data['count_plus'] = 0
                    info_data['count_minus'] = 0
                    save_data(user_data)
                    # print(user_data)
                else:
                    print("Ошибка")
    save_fo(data)
    print(data)



def get_abdi_sert(message):
    global count_plus
    global count_minus
    count_plus = info_data['count_plus']
    count_minus = info_data['count_minus']
    price1 = 0
    price2 = 0
    try:
        if((type(int(count_plus)) == int) and (type(int(count_minus)) == int)):
            if(user_data[user_data['lok']]['type_nominal'] == "10000"):
                price1 = int(count_plus) * 10000
                price2 = int(count_minus) * 10000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "15000"):
                price1 = int(count_plus) * 15000
                price2 = int(count_minus) * 15000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "25000"):
                price1 = int(count_plus) * 25000
                price2 = int(count_minus) * 25000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "5000"):
                price1 = int(count_plus) * 5000
                price2 = int(count_minus) * 5000
                user_data['balans'] = str(int(user_data['balans'])+price2)

            if(int(user_data['balans']) >= int(price1)):
                user_data['balans'] = str(int(user_data['balans'])-price1)
                # user_data['sportmaster_count'] = user_data['sportmaster_count'] + \
                #     int(count)
                info_data['count_plus'] = 0
                info_data['count_minus'] = 0
                save_data(user_data)
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
    price1 = 0
    price2 = 0
    try:
        if((type(int(count_plus)) == int) and (type(int(count_minus)) == int)):
            if(user_data[user_data['lok']]['type_nominal'] == "10000"):
                price1 = int(count_plus) * 10000
                price2 = int(count_minus) * 10000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "15000"):
                price1 = int(count_plus) * 15000
                price2 = int(count_minus) * 15000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "25000"):
                price1 = int(count_plus) * 25000
                price2 = int(count_minus) * 25000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "5000"):
                price1 = int(count_plus) * 5000
                price2 = int(count_minus) * 5000
                user_data['balans'] = str(int(user_data['balans'])+price2)

            if(int(user_data['balans']) >= int(price1)):
                user_data['balans'] = str(int(user_data['balans'])-price1)
                # user_data['sportmaster_count'] = user_data['sportmaster_count'] + \
                #     int(count)
                info_data['count_plus'] = 0
                info_data['count_minus'] = 0
                save_data(user_data)
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
    price1 = 0
    price2 = 0
    try:
        if((type(int(count_plus)) == int) and (type(int(count_minus)) == int)):
            if(user_data[user_data['lok']]['type_nominal'] == "10000"):
                price1 = int(count_plus) * 10000
                price2 = int(count_minus) * 10000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "15000"):
                price1 = int(count_plus) * 15000
                price2 = int(count_minus) * 15000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "25000"):
                price1 = int(count_plus) * 25000
                price2 = int(count_minus) * 25000
                user_data['balans'] = str(int(user_data['balans'])+price2)
            elif(user_data[user_data['lok']]['type_nominal'] == "5000"):
                price1 = int(count_plus) * 5000
                price2 = int(count_minus) * 5000
                user_data['balans'] = str(int(user_data['balans'])+price2)

            if(int(user_data['balans']) >= int(price1)):
                user_data['balans'] = str(int(user_data['balans'])-price1)
                # user_data['sportmaster_count'] = user_data['sportmaster_count'] + \
                #     int(count)
                info_data['count_plus'] = 0
                info_data['count_minus'] = 0
                save_data(user_data)
                # print(user_data)
            else:
                print("Ошибка")
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id,
                         listDontUnderstand[langNumber1[0]]+'\U0001F914')
        get_sertificat(message)


def get_sertificat(message):
    info_data['in_korazina'] = False
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='Спортмастер', callback_data='meloman')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Mechta', callback_data='marwin')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='LC Waikiki', callback_data='lcwaikiki')
    callback_button5 = telebot.types.InlineKeyboardButton(
        text='ABDI', callback_data='abdi')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2,
                 callback_button3, callback_button5, callback_button4)
    bot.send_message(
        message.chat.id, listCertificateEach[langNumber1[0]]+'\U0001F4B8', reply_markup=keyboard)


def between_date_day(from_date, to_date):
    from_date = from_date.split(".")
    to_date = to_date.split(".")
    result_date = date(int(to_date[2]), int(to_date[1]), int(
        to_date[0])) - date(int(from_date[2]), int(from_date[1]), int(from_date[0]))
    return result_date.days


def get_count(message):
    try:
        a = 0
        with open('u.json', encoding='utf-8') as file:
            stock = json.load(file)
        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)
        for smth in stock:
            for i in range(len(data)):
                if data[i][id] == str(message.from_user.id):
                    a = a + 1
        price = a * 45000
        return str(int(price))
    except Exception as ex:
        print(ex)


def get_count_deti(message):
    a = 0
    with open('u.json', encoding='utf-8') as file:
        stock = json.load(file)
    for smth in stock:
        if (smth['Телефон'].replace("+", "") == str(message.contact.phone_number).replace("+","")):
            birthday = int(between_date_day(
                smth['Дата рождения Ребенка'], '01.01.2022') / 365)
            a = a + 1
    return a


def user_data_clear():
    user_data['iin'] = ''
    user_data['fio'] = ''
    user_data['phone_number'] = ''
    user_data['balans'] = ''
    user_data['count_deti'] = ''
    user_data['dengi'] = 0,
    user_data['sportmaster_count'] = 0,
    user_data['mechta_count'] = 0,
    user_data['lcwaikiki_count'] = 0,
    user_data['abdi_count'] = 0,
    user_data['dengi_count'] = 0,
    user_data['lok'] = '',
    user_data['accept'] = False,
    user_data['save'] = False,
    user_data['lang'] = ''
    return user_data


def clear_cart(message):
    user_data['balans'] = str(int(user_data['balans']) + user_data['dengi'] +
                              + user_data['sportmaster_count']['count_5000'] * 5000
                              + user_data['mechta_count']['count_5000'] * 5000
                              + user_data['lcwaikiki_count']['count_5000'] * 5000
                              + user_data['abdi_count']['count_5000'] * 5000
                              + user_data['sportmaster_count']['count_10000'] * 10000
                              + user_data['mechta_count']['count_10000'] * 10000
                              + user_data['lcwaikiki_count']['count_10000'] * 10000
                              + user_data['abdi_count']['count_10000'] * 10000
                              + user_data['sportmaster_count']['count_15000'] * 15000
                              + user_data['mechta_count']['count_15000'] * 15000
                              + user_data['lcwaikiki_count']['count_15000'] * 15000
                              + user_data['abdi_count']['count_15000'] * 15000
                              + user_data['sportmaster_count']['count_25000'] * 25000
                              + user_data['mechta_count']['count_25000'] * 25000
                              + user_data['lcwaikiki_count']['count_25000'] * 25000
                              + user_data['abdi_count']['count_25000'] * 25000
                              )
    user_data['dengi'] = 0
    user_data['dengi_count']['count_5000'] = 0
    user_data['dengi_count']['count_10000'] = 0
    user_data['dengi_count']['count_15000'] = 0
    user_data['dengi_count']['count_25000'] = 0
    user_data['sportmaster_count']['count_5000'] = 0
    user_data['mechta_count']['count_5000'] = 0
    user_data['lcwaikiki_count']['count_5000'] = 0
    user_data['abdi_count']['count_5000'] = 0
    user_data['sportmaster_count']['count_10000'] = 0
    user_data['mechta_count']['count_10000'] = 0
    user_data['lcwaikiki_count']['count_10000'] = 0
    user_data['sportmaster_count']['count_15000'] = 0
    user_data['mechta_count']['count_15000'] = 0
    user_data['lcwaikiki_count']['count_15000'] = 0
    user_data['sportmaster_count']['count_25000'] = 0
    user_data['mechta_count']['count_25000'] = 0
    user_data['lcwaikiki_count']['count_25000'] = 0
    user_data['abdi_count']['count_10000'] = 0
    user_data['abdi_count']['count_15000'] = 0
    user_data['abdi_count']['count_25000'] = 0
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text=listAccept[langNumber1[0]]+'\U00002705', callback_data='soglasitsya')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text=listWhatDelete[langNumber1[0]]+'\U0000274C', callback_data='delete')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text=listRedaktirovat[langNumber1[0]], callback_data='redaktirovat')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text=listBack[langNumber1[0]]+' '+'\U0001F519', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2,
                 callback_button3, callback_button4)
    bot.edit_message_text(
        chat_id=message.chat.id, message_id=message.message_id, text=get_info_only_exists(message), reply_markup=keyboard, parse_mode="HTML")
    save_data(user_data)


def save_data(user_data):
    user_data['balans'] = str(int(user_data['balans']))
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    minimal = 0
    for txt in data:
        if txt['phone_number'] == user_data['phone_number']:
            data.pop(minimal)
        else:
            None
        minimal = minimal + 1
    data.append(user_data)
    with open('result.json', "w", encoding='utf8') as file:
        file.write(json.dumps(data, ensure_ascii=False))

def save_data_json(message):
    luk = {
            'id': str(message.from_user.id),
            'iin': find_iin(message),
            'fio': find_fio(message),
            'phone_number': str(message.contact.phone_number).replace("+",""),
            'balans': str(get_count_deti(message) * 45000),
            'count_deti': get_count_deti(message),
            'dengi': 0,
            'sportmaster_count': {"type_nominal": "", "count_5000": 0,"count_10000": 0, "count_15000": 0, "count_25000": 0},
            'mechta_count': {"type_nominal": "","count_5000": 0, "count_10000": 0, "count_15000": 0, "count_25000": 0},
            'lcwaikiki_count': {"type_nominal": "","count_5000": 0, "count_10000": 0, "count_15000": 0, "count_25000": 0},
            'abdi_count': {"type_nominal": "","count_5000": 0, "count_10000": 0, "count_15000": 0, "count_25000": 0},
            'dengi_count': {"type_nominal": "", "count_5000": 0, "count_10000": 0, "count_15000": 0, "count_25000": 0},
            'lok': '',
            'accept': False,
            'save': False,
            'lang': '',
            'sended': False,
            'comment': [],
            'filial': '',
            'count_plus': 0,
            'count_minus': 0
        }
    append_deti(luk['comment'],message)
    luk['filial'] = 'Атырау'
    try:
        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)
        minimal = 0
        for txt in data:
            if txt['phone_number'] == luk['phone_number']:
                data.pop(minimal)
            else:
                None
            minimal = minimal + 1
        data.append(luk)
        with open('result.json', "w", encoding='utf8') as file:
            file.write(json.dumps(data, ensure_ascii=False))
    except Exception as ex:
        print(ex)


def get_phone_number(message):

    keyboard = telebot.types.ReplyKeyboardMarkup(
        row_width=1, resize_keyboard=True)
    button_phone = telebot.types.KeyboardButton(
        text=listPhone[langNumber1[0]], request_contact=True)
    keyboard.add(button_phone)  # Добавляем эту кнопку
    bot.send_message(
        message.chat.id, listCheckPhone[langNumber1[0]], reply_markup=keyboard)
    bot.register_next_step_handler(message, get_all_data)


def get_info_only_exists(message):
    string = listVybrali[langNumber1[0]]
    dengi = ''
    sport = ''
    mechta = ''
    lcwaikiki = ''
    abdi = ''
    all = ''
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    for i in data:
        if i['id']==str(message.chat.id):
            all  = str(i['count_deti']* 45000)
            if(i['dengi'] > 0):
                dengi = "\n" + listDengiRazmer[langNumber1[0]] + \
                    str(i['dengi']) + 'тг'+'\U0001F4B0'
            if(i['sportmaster_count']['count_5000'] or i['sportmaster_count']['count_10000'] > 0 or i['sportmaster_count']['count_15000'] > 0 or i['sportmaster_count']['count_25000'] > 0):
                if(i['sportmaster_count']['count_5000'] > 0):
                    sport = sport + " сертификат номиналом 5000тг " + "- " + \
                        str(i['sportmaster_count']['count_5000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['sportmaster_count']['count_10000'] > 0):
                    sport = sport + " сертификат номиналом 10000тг " + "- " + \
                        str(i['sportmaster_count']['count_10000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['sportmaster_count']['count_15000'] > 0):
                    sport = sport + " сертификат номиналом 15000тг " + "- " + \
                        str(i['sportmaster_count']['count_15000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['sportmaster_count']['count_25000'] > 0):
                    sport = sport + " сертификат номиналом 25000тг " + "- " + \
                        str(i['sportmaster_count']['count_25000']
                            ) + ' ' + listCount[langNumber1[0]]
            if(i['mechta_count']['count_5000'] or i['mechta_count']['count_10000'] > 0 or i['mechta_count']['count_15000'] > 0 or i['mechta_count']['count_25000'] > 0):
                if(i['mechta_count']['count_5000'] > 0):
                    mechta = mechta + " сертификат номиналом 5000тг " + "- " + \
                        str(i['mechta_count']['count_5000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['mechta_count']['count_10000'] > 0):
                    mechta = mechta + " сертификат номиналом 10000тг " + "- " + \
                        str(i['mechta_count']['count_10000']) + \
                        ' ' + listCount[langNumber1[0]] + ", "
                if(i['mechta_count']['count_15000'] > 0):
                    mechta = mechta + " сертификат номиналом 15000тг " + "- " + \
                        str(i['mechta_count']['count_15000']) + \
                        ' ' + listCount[langNumber1[0]] + ", "
                if(i['mechta_count']['count_25000'] > 0):
                    mechta = mechta + " сертификат номиналом 25000тг " + "- " + \
                        str(i['mechta_count']['count_25000']) + \
                        ' ' + listCount[langNumber1[0]]
            if(i['lcwaikiki_count']['count_5000'] or i['lcwaikiki_count']['count_10000'] > 0 or i['lcwaikiki_count']['count_15000'] > 0 or i['lcwaikiki_count']['count_25000'] > 0):
                if(i['lcwaikiki_count']['count_5000'] > 0):
                    lcwaikiki = lcwaikiki + " сертификат номиналом 5000тг " + "- " + \
                        str(i['lcwaikiki_count']['count_5000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['lcwaikiki_count']['count_10000'] > 0):
                    lcwaikiki = lcwaikiki + " сертификат номиналом 10000тг " + "- " + \
                        str(i['lcwaikiki_count']['count_10000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['lcwaikiki_count']['count_15000'] > 0):
                    lcwaikiki = lcwaikiki + " сертификат номиналом 15000тг " + "- " + \
                        str(i['lcwaikiki_count']['count_15000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['lcwaikiki_count']['count_25000'] > 0):
                    lcwaikiki = lcwaikiki + " сертификат номиналом 25000тг " + "- " + \
                        str(i['lcwaikiki_count']['count_25000']
                            ) + ' ' + listCount[langNumber1[0]]
            if(i['abdi_count']['count_5000'] or i['abdi_count']['count_10000'] > 0 or i['abdi_count']['count_15000'] > 0 or i['abdi_count']['count_25000'] > 0):
                if(i['abdi_count']['count_5000'] > 0):
                    abdi = abdi + " сертификат номиналом 5000тг " + "- " + \
                        str(i['abdi_count']['count_5000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['abdi_count']['count_10000'] > 0):
                    abdi = abdi + " сертификат номиналом 10000тг " + "- " + \
                        str(i['abdi_count']['count_10000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['abdi_count']['count_15000'] > 0):
                    abdi = abdi + " сертификат номиналом 15000тг " + "- " + \
                        str(i['abdi_count']['count_15000']
                            ) + ' ' + listCount[langNumber1[0]] + ", "
                if(i['abdi_count']['count_25000'] > 0):
                    abdi = abdi + " сертификат номиналом 25000тг " + "- " + \
                        str(i['abdi_count']['count_25000']
                            ) + ' ' + listCount[langNumber1[0]]
            if(i['sportmaster_count']['count_5000'] > 0 or i['sportmaster_count']['count_10000'] > 0 or i['sportmaster_count']['count_15000'] > 0 or i['sportmaster_count']['count_25000'] > 0):
                sport = "\nСпортмастер:" + sport
            if(i['mechta_count']['count_5000'] > 0 or i['mechta_count']['count_10000'] > 0 or i['mechta_count']['count_15000'] > 0 or i['mechta_count']['count_25000'] > 0):
                mechta = "\nMechta:" + mechta
            if(i['lcwaikiki_count']['count_5000'] > 0 or i['lcwaikiki_count']['count_10000'] > 0 or i['lcwaikiki_count']['count_15000'] > 0 or i['lcwaikiki_count']['count_25000'] > 0):
                lcwaikiki = "\nLC Waikiki:" + lcwaikiki
            if(i['abdi_count']['count_5000'] > 0 or i['abdi_count']['count_10000'] > 0 or i['abdi_count']['count_15000'] > 0 or i['abdi_count']['count_25000'] > 0):
                abdi = "\nABDI:" + abdi
            string =  string + sport + mechta + lcwaikiki + abdi + dengi +"\n\nИтого: " + all + "тг"
            return string

def get_birthday(message):
    with open('result.json', encoding='utf-8') as file:
        data = json.load(file)
    for i in data:
        if(i['id']==str(message.chat.id)):
            birthday = i['iin']
            if(int(birthday[0])==0):
                birthday = birthday[4] + birthday[5] + '.' + birthday[2]+ birthday[3] + '.20' + birthday[0]+ birthday[1]
            else:
                birthday = birthday[4] + birthday[5] + '.' + birthday[2]+ birthday[3] + '.19' + birthday[0]+ birthday[1]
            return birthday
def get_saved_person_for_excel(message,counts):
    with open('result.json', encoding='utf-8') as file:
        result_json = json.load(file)
    for i in result_json:
        if i['save'] == True and i['id'] == str(message.chat.id):
            result = {
                'Филиал': i['filial'],
                'ФИО Сотрудника': i['fio'],
                'ИИН Сотрудника': i['iin'],
                'Число детей': i['count_deti'],
                'Дата рождения': get_birthday(message),
                'Информация о Ребенке': i['comment'],
                'Денежная компенсация': i['dengi'],
                'Спортмастер сертификаты': counts['sportmaster_count'],
                'Mechta сертификаты': counts['mechta_count'],
                'LC Waikiki сертификаты': counts['lcwaikiki_count'],
                'ABDI сертификаты': counts['abdi_count'],
                'Итого': i['itogo']
            }
    counts.clear()
    with open('all.json', encoding='utf-8') as files:
        data = json.load(files)
    data.append(result)
    with open('all.json', "w", encoding='utf8') as f:
        f.write(json.dumps(data, ensure_ascii=False))

    # df_json = pd.read_json('all.json')
    # df_json.to_excel('all.xlsx')
    # client = ConversionClient(
    #     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImI2ZmI4NjAzNDk2NjQ4MjJiMmZjYzQ1Y2NmODY0NWEwIiwiaWF0IjoxNjU3MjEzMDUyfQ.PHN_7SBLWyzvBfMk4sBOtk55tN_Z53dFbW3EIUmlucw')
    # try:
    #     client.convert('convert.json_objects_to_excel',
    #                    'all.json', 'all.xlsx', {'excel_format': 'xlsx'})
    # except Exception as error:
    #     print(error)


def find_iin(message):
    with open('u.json', encoding='utf-8') as files:
        data = json.load(files)
    iin = ''
    for i in data:
        if(i['Телефон'] == str(message.contact.phone_number).replace("+","")):
            iin = i['ИИН']
    return iin

def find_fio(message):
    with open('u.json', encoding='utf-8') as files:
        data = json.load(files)
    fio = ''
    for i in data:
        if(i['Телефон'] == str(message.contact.phone_number).replace("+","")):
            fio = i['ФИО']
    return fio

def find_city():
    with open('u.json', encoding='utf-8') as files:
        data = json.load(files)
    city = ''
    for i in data:
        if(i['Телефон'] == user_data['phone_number']):
            city = i['Филиал']
    return city


langNumber = langNumber1[0]
listLang = ['Русский язык', 'Қазақ тілі']
listLangDef = ['Вы выбрали:', 'Сіз таңдадыңыз:']
listPhone = ['Отправить номер телефона', 'Телефон нөмірін жіберу']
listIIN = ['В базе данных не нашли ваш номер\nНапишите свой ИИН:',
           "Деректер базасында сіздің нөміріңіз табылмады\nИИН-iздi жазыныз:"]

listBalans = ['Ваша сумма', 'Сiздiн балансыныз', ]
listuVas = [' у вас ', ' сізде ']
listRebenok = [' ребенок/детей школьного возраста\n\nНа 1 ребенок-школьника в возрасте от 6 до 17 лет включительно полагается 45000тг',
               ' мектеп жаcтағы балаңыз бар\n\n1 балаға-оқушыға 45 000 теңгеден берiледi (ағымдағы жылдың 1 қыркүйегіндегі жағдай бойынша 6-дан 17 жасқа дейін)  !!!', ' ребенок/детей школьного возраста\n\nНа 1 школьника в возрасте от 6 до 17 лет включительно полагается 45000тг']
list3Bank = ['Согласны ли вы с указаными данными? ',
             'Көрсетiлген ақпаратпен келiсеciз бе?']

listSupport = ['Обратитесь по',
               'Егер сiз келiспесенiз мына номiрге конырау шалыныз:87077012916']
listLet = ['лет', 'жаста']
listVyhod = ['Выход', 'Шығу']
listCart = ['Ваша сумма: ', 'Сіздің сомаңыз: ']

listMoney = ['Денежная компенсация💵', 'Ақшалай өтем💵']
listBack = ['Назад', 'Артқа']
listAccept = ['Подтвердить✅', 'Растау✅']
listDeleteTovar = ['Удалить товар', 'Тауарды алып тастау']
listCount = ['штук', 'дана']
listNaSummu = [', на сумму:', ', сомада:']
listChoose = ['Выберите', 'Таңдаңыз']
listGoodBye = ['Ваш запрос успешно направлен! ✅',
               'Сіздің сұрауыңыз сәтті жіберілді! ✅']
listVyvesti = ['1 штук = 5000тг\nНапишите количество:',
               '1 штук = 5000тг\nНСанын жазыныз:']
listCertificate = ['1 Сертификат = 5000тг\nДобавляйте, сколько штук сертификатов хотите:',
                   '1 Сертификат = 5000тг\nҚанша дана сертификат алғыңыз келетінін танданыз:']
listEndAccept = ['Вы уверены в своем выборе?',
                 'Сіз өз таңдауыңызға сенімдісіз бе?']
listWhatDelete = ['Очистить корзину', 'Корзинаны тазалау']
listReturnMoney = ['Напишите сколько штук вы хотите вернуть на баланс:',
                   'Балансқа қанша штук қайтарғыңыз келетінін жазыңыз:']
listReturnMeloman = ['Спортмастер - спортивный магазин для всей семьи. Всё для спорта и активного отдыха в одном месте.',
                     'Спортмастер - бүкіл отбасы үшін спорт дүкені. Барлығы бір жерде спорт пен белсенді демалыс үшін.']
listReturnMarwin = ['Mechta - специализированная торговая сеть магазинов электроники и бытовой техники.',
                    'Mechta - электроника және тұрмыстық техника дүкендерінің мамандандырылған сауда желісі.']
listReturnLCWaikiki = ['LC Waikiki – качественная и комфортная одежда для детей, мужчин и женщин. Пополните свой гардероб стильной одеждой с оригинальным дизайном.',
                       'LC Waikiki-балалар, ерлер мен әйелдер үшін сапалы және жайлы киім. Гардеробыңызды түпнұсқа дизайнымен стильді киіммен толықтырыңыз.']
listSuccess = ['Успешно', 'Сәтті']
listNotEnough = ['У вас недостаточно средств', 'Сiзде қаражат жеткіліксіз']
listUnSuccess = ['Не удалось!', 'Сәтсіз!']
listGoodByeSuccess = ['Ваш запрос успешно направлен! ✅',
                      'Сіздің сұрауыңыз сәтті жіберілді! ✅']
listDontUnderstand = ['Я вас не понял напишите еще раз',
                      'Мен сізді түсінбедім қайта жазыңыз']

listUndefinedIIN = ['Не нашли такой ИИН', 'Мұндай ИИН табылмады']
listChoosed = ['Вы уже сделали выбор', 'Сіз таңдау жасадыңыз']
listRedaktirovat = ['Редактировать товары', 'Өнімдерді өңдеу']
listDeleted = ['Корзина очищена', 'Себет тазаланды']
listChangeLang = ['Сменить язык', 'Тілді өзгерту']
listYes = ['Да', 'Ия']
listNo = ['Нет', 'Жок']
listKratnuyu = ['Вы выбрали сертификат номиналом ', 'теңгеге еселі сома ']
cerKz = 'Сертификаттар'
cerRu = 'Сертификаты'
listCertificateEach = [cerRu, cerKz]
listCheckPhone = ['Проверка номера\nНажмите на кнопку "Отправить номер телефона"',
                  'Нөмірді тексеру\n"Телефон нөмірін жіберу" батырмасын басыңыз']
listLangChange = ['Язык изменен ', 'Тіл өзгерді']
ChecklastMess = ['Проверить Корзину', 'Себетті Тексеру']
listInstruck = ['Уважаемые коллеги!!\n\nДля получения компенсации или сертификатов на подготовку детей к школе просим пройти опрос.\nСрок  прохождения опроса до <b>20</b> июля 2022 года.',
                'Құрметті әріптестер!!\nӨтемақы немесе балаларды мектепке дайындауға сертификат алу үшін сауалнамадан өтуіңізді сұраймыз.\nСауалнамадан өту мерзімі 2022 жылғы <b>20</b> шілдеге дейін.']
listPart = ['Частично деньги или сертификаты',
            'Ішінара ақша немесе сертификаттар']
listNotinBD = ['<b>Вас нету базе данных</b>\nНапишите свой ИИН',
               '<b > Сіз деректер базасында жоқсыз < / b > \ЖСН-дi жазыңыз']
listItIsNotU = ['Это не вы! Нажмите на кнопку (Отправить номер телефона)',
                'Бұл сіз емес! Түймесін басыңыз (телефон нөмірін жіберу)']
listOstatok = ['Остаток: ', 'Қалдығы: ']
listAddMore = ['🔙 Добавить еще', '🔙Тағы қосу']
listVashaSumma = ['Ваша сумма: ', 'Сіздің сомаңыз: ']
listPodtverdit = ['Подтвердить✅', 'Растау✅']
listChooseNominal = ['Выберите сумму номинала:', 'Номинал сомасын таңдаңыз:']
listIINno = ['Ваши данные не найдены в базе данных, возможно возраст Ваших детей не соответствует условию (ученик образовательного учереждения от 5 до 17 лет)!',
             'Сіздің деректер базада табылмады , Сіздің балаларыныңыз шарт бойынша сәйкес келмеуі мүмкін (5 жастан 17 жасқа дейінгі білім беру мекемесінің оқушысы)!']
listProdolzhit = ['Далее', 'Әрі қарай']
listVybrali = ['Вы выбрали:', 'Сіз таңдадыңыз:']
listDengiRazmer = ['Денежную компенсацию в размере: ',
                   'Мөлшерінде ақшалай өтемақы: ']
listCountKol = ['Выберите количество', 'Санын таңдаңыз']
listVashaSumma = ['Ваша сумма: ', 'Сіздің сомаңыз: ']
listOstatok = ['Остаток: ', 'Қалдығы: ']
listTagyKosu = ['🔙 Добавить еще', '🔙 Тағы қосу']
listVybrana = ['Сумма полностью не выбрана! Выберите еще сертификаты на сумму ','Сома толығымен таңдалмаған! Тағы сертификаттарды таңдаңыз ']
listOpros = ['По подтвержденным данным  пройдите опрос','Расталған деректер бойынша сауалнамадан өтіңіз']
listYouTube = ['https://youtu.be/WlIOcnXNw40','https://www.youtube.com/watch?v=IW7fmwgf_XI']
listBankDer= ['Держателем какой карты вы являетесь?','Сіз қандай карта ұстаушысыз?']
try:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
except:
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
