from datetime import date
from email import message
from itertools import count
from re import L
from time import sleep
import telebot
import math
from random import randint
import json

token = '5512229550:AAF9qGoRFPa3ukPqxTgbbbJb4dR_NJtAEeE'
bot = telebot.TeleBot(token)
langNumber1 = [0]
user_data = {
    'iin': '',
    'fio': '',
    'email': '',
    'balans': '',
    'count_deti': '',
    'dengi': 0,
    'meloman_count': 0,
    'marwin_count': 0,
    'lcwaikiki_count': 0
}


@bot.message_handler(commands=['start'])
def lang(message):
    bot.send_message(message.from_user.id,
                     "Добро Пожаловать!\nҚош келдіңіз!\nWelcome!")
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='rus', callback_data='r')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='kaz', callback_data='k')
    keyboard.add(callback_button1, callback_button2)
    bot.send_message(message.from_user.id,
                     'Выберите язык:\nТілді таңдаңыз:\n', reply_markup=keyboard)


def get_all_data(message):
    a = 0
    b = 0
    global iin
    iin = message.text
    with open('data.json', encoding='utf-8') as file:
        stock = json.load(file)
    for smth in stock:
        if smth['ИИН'] == iin:
            a = a + 1
    for smth in stock:
        if smth['ИИН'] == iin:
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
        if smth['ИИН'] == iin:
            birthday = int(between_date_day(
                smth['Дата рождения Ребенка'], '01.09.2022') / 365)
            if(6 <= birthday <= 17):
                bot.send_message(
                    message.from_user.id, smth['ФИО Ребенка'] + " " + str(birthday) + "лет")
                b = b + 1
    user_data['count_deti'] = str(b)

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


def get_cart(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='Корзина', callback_data='korzina')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Магазин', callback_data='magazin')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='Выход', callback_data='vyhod')
    keyboard.add(callback_button1, callback_button2, callback_button3)
    bot.send_message(message.chat.id, ' Меню:\nВаш баланс:' +
                     str(user_data['balans'])+'\n', reply_markup=keyboard)


def get_magazin(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='Деньги', callback_data='dengi')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Сертификат', callback_data='sertificaty')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='Назад', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2, callback_button3)
    bot.send_message(message.chat.id, ' Магазин', reply_markup=keyboard)


def get_korzina(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='Согласится', callback_data='soglasitsya')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Удалить товар', callback_data='delete')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='Назад', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2, callback_button3)
    mel = user_data['meloman_count'] * 5000
    mar = user_data['marwin_count'] * 5000
    lc = user_data['lcwaikiki_count'] * 5000
    bot.send_message(message.chat.id, ' Корзина\nВаш баланс:'+str(user_data['balans'])+'\nДеньги:'+str(user_data['dengi']) +
                     '\nМеломан сертификаты:'+str(user_data['meloman_count'])+', на сумму:' + str(mel) +
                     '\nMarwin сертификаты:'+str(user_data['marwin_count'])+', на сумму:' + str(mar) +
                     '\nLCWaikiki сертификаты:'+str(user_data['lcwaikiki_count'])+', на сумму:' + str(lc), reply_markup=keyboard)


def get_delete(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='Деньги', callback_data='dengi_delete')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Меломан сертификат', callback_data='mel-sertificaty')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='Marwin сертификат', callback_data='mar-sertificaty')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text='LCWaikiki сертификат', callback_data='lc-sertificaty')
    callback_button5 = telebot.types.InlineKeyboardButton(
        text='Назад', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2,
                 callback_button3, callback_button4, callback_button5)
    bot.send_message(message.chat.id, ' Выберите', reply_markup=keyboard)


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
                bot.edit_message_text(
                    chat_id=call.message.chat.id, message_id=call.message.message_id, text=listLangDef[langNumber1[0]])
                bot.send_message(call.message.chat.id,
                                 listLang[langNumber1[0]])
                bot.send_message(call.message.chat.id,
                                 listIIN[langNumber1[0]])
                bot.register_next_step_handler(call.message, get_all_data)
            elif call.data == "d" or call.data == "n" or call.data == "i" or call.data == "j":
                if call.data == 'd':
                    b = get_count()
                    user_data['balans'] = b
                    # print(user_data)
                    get_cart(call.message)
                elif call.data == 'n':
                    bot.send_message(call.message.chat.id,
                                     listSupport[langNumber1[0]])
                elif call.data == 'i':
                    b = get_count()
                    user_data['balans'] = b
                    bot.send_message(call.message.chat.id,
                                     listBalans[langNumber1[0]])
                    # print(user_data)
                    get_cart(call.message)
                elif call.data == 'j':
                    bot.send_message(call.message.chat.id,
                                     listSupport[langNumber1[0]]+str(b)+"тг")
            elif call.data == "korzina" or call.data == "magazin" or call.data == "vyhod":
                if call.data == 'korzina':
                    get_korzina(call.message)
                elif call.data == 'magazin':
                    get_magazin(call.message)
                elif call.data == 'vyhod':
                    bot.send_message(call.message.chat.id,
                                     "Спасибо! До свидания!")
            elif call.data == "dengi" or call.data == "sertificaty" or call.data == "nazad":
                if call.data == 'dengi':
                    bot.send_message(call.message.chat.id,
                                     "Напишите сумму которую вы хотите вывести:")
                    bot.register_next_step_handler(call.message, get_dengi)
                elif call.data == 'sertificaty':
                    get_sertificat(call.message)
                elif call.data == 'nazad':
                    get_cart(call.message)
            elif call.data == "meloman" or call.data == "marwin" or call.data == "lcwaikiki":
                if call.data == 'meloman':
                    bot.send_message(call.message.chat.id,
                                     "Напишите сколько штук сертификатов хотити:")
                    bot.register_next_step_handler(
                        call.message, get_meloman_sert)
                elif call.data == 'marwin':
                    bot.send_message(call.message.chat.id,
                                     "Напишите сколько штук сертификатов хотити:")
                    bot.register_next_step_handler(
                        call.message, get_marwin_sert)
                elif call.data == 'lcwaikiki':
                    bot.send_message(call.message.chat.id,
                                     "Напишите сколько штук сертификатов хотити:")
                    bot.register_next_step_handler(
                        call.message, get_lcwaikiki_sert)
            elif call.data == "soglasitsya" or call.data == "delete":
                if call.data == 'soglasitsya':
                    bot.send_message(call.message.chat.id,
                                     "Если вы уверенны своем выборе напишите: СОГЛАШАЮСЬ")
                    bot.register_next_step_handler(
                        call.message, get_sogl)
                elif call.data == 'delete':
                    bot.send_message(call.message.chat.id,
                                     "Что хотите удалить?")
                    get_delete(call.message)
            elif call.data == "dengi_delete" or call.data == "mel-sertificaty" or call.data == "mar-sertificaty" or call.data == "lc-sertificaty":
                if call.data == 'dengi_delete':
                    bot.send_message(call.message.chat.id,
                                     "Напишите сколько денег вы хотите вернуть на баланс:")
                    bot.register_next_step_handler(
                        call.message, add_balans)
                elif call.data == 'mel-sertificaty':
                    bot.send_message(call.message.chat.id,
                                     "Напишите сколько сертификатов Меломана хотите вернуть:")
                    bot.register_next_step_handler(
                        call.message, add_mel)
                elif call.data == 'mar-sertificaty':
                    bot.send_message(call.message.chat.id,
                                     "Напишите сколько сертификатов Marwin хотите вернуть:")
                    bot.register_next_step_handler(
                        call.message, add_mar)
                elif call.data == 'lc-sertificaty':
                    bot.send_message(call.message.chat.id,
                                     "Напишите сколько сертификатов LCWaikiki хотите вернуть:")
                    bot.register_next_step_handler(
                        call.message, add_lcwai)

        except Exception as ex:
            print(ex)


def get_dengi(message):
    global dengi
    dengi = message.text
    result = int(user_data['balans'])-int(dengi)
    if(result >= 0):
        user_data['balans'] = str(result)
        user_data['dengi'] = int(dengi) + user_data['dengi']
        bot.send_message(message.chat.id, "Успешно")
    else:
        bot.send_message(message.chat.id, "Не достаточно средств")
    # print(user_data)
    get_magazin(message)

def add_mar(message):
    count = message.text
    if(int(user_data['marwin_count']) >= int(count)):
        price = int(count)*5000
        user_data['balans'] = str(int(user_data['balans']) + price)
        user_data['marwin_count'] = user_data['marwin_count'] - int(count)
        bot.send_message(message.chat.id, "Успешно")
        get_korzina(message)
    else:
        bot.send_message(message.chat.id, "Не удалось!")
        get_korzina(message)

def add_lcwai(message):
    count = message.text
    if(int(user_data['lcwaikiki_count']) >= int(count)):
        price = int(count)*5000
        user_data['balans'] = str(int(user_data['balans']) + price)
        user_data['lcwaikiki_count'] = user_data['lcwaikiki_count'] - int(count)
        bot.send_message(message.chat.id, "Успешно")
        get_korzina(message)
    else:
        bot.send_message(message.chat.id, "Не удалось!")
        get_korzina(message)
    
def add_balans(message):
    global dengi
    dengi = message.text
    if(int(user_data['dengi']) >= int(dengi)):
        user_data['balans'] = str(int(user_data['balans']) + int(dengi))
        user_data['dengi'] = user_data['dengi'] - int(dengi)
        bot.send_message(message.chat.id, "Успешно")
        get_korzina(message)
    else:
        bot.send_message(message.chat.id, "Не удалось!")
        get_korzina(message)


def get_sogl(message):
    global sogl
    sogl = message.text
    if(sogl.lower() == 'соглашаюсь'):
        bot.send_message(message.chat.id, "Успешно! До Свидания!")
        print(user_data)
        with open('result.json', encoding='utf-8') as file:
            data = json.load(file)
        # 2. Update json object
        data.append(user_data)
        # 3. Write json file
        with open('result.json', "w",encoding='utf8') as file:
            file.write(json.dumps(data, ensure_ascii=False))
        user_data['iin'] = ''
        user_data['fio'] = ''
        user_data['email'] = ''
        user_data['balans'] = ''
        user_data['count_deti'] = ''
        user_data['dengi'] = 0
        user_data['meloman_count'] = 0
        user_data['marwin_count'] = 0
        user_data['lcwaikiki_count'] = 0
        print(user_data)
    else:
        bot.send_message(message.chat.id, "Не удалось!")
        get_korzina(message)


def get_meloman_sert(message):
    global count
    count = message.text
    try:
        if(type(int(count)) == int):
            price = int(count) * 5000
            print(price)
            result = int(user_data['balans'])-int(price)
            if(result >= 0):
                user_data['balans'] = str(result)
                user_data['meloman_count'] = user_data['meloman_count'] + \
                    int(count)
                bot.send_message(message.chat.id, "Успешно")
                get_magazin(message)
                # print(user_data)
            else:
                bot.send_message(message.chat.id, "Не достаточно средств")
                get_magazin(message)
    except Exception as ex:
        print(ex)
        bot.send_message(message.chat.id,
                         "Я вас не понял напишите еще раз")
        get_magazin(message)


def get_marwin_sert(message):
    global count
    count = message.text
    try:
        if(type(int(count)) == int):
            price = int(count) * 5000
            print(price)
            result = int(user_data['balans'])-int(price)
            if(result >= 0):
                user_data['balans'] = str(result)
                bot.send_message(message.chat.id, "Успешно")
                user_data['marwin_count'] = user_data['marwin_count'] + \
                    int(count)
                get_magazin(message)
                # print(user_data)
            else:
                bot.send_message(message.chat.id, "Не достаточно средств")
                get_magazin(message)
    except Exception as ex:
        bot.send_message(message.chat.id,
                         "Я вас не понял напишите еще раз")
        get_magazin(message)


def get_lcwaikiki_sert(message):
    global count
    count = message.text
    try:
        if(type(int(count)) == int):
            price = int(count) * 5000
            print(price)
            result = int(user_data['balans'])-int(price)
            if(result >= 0):
                user_data['balans'] = str(result)
                user_data['lcwaikiki_count'] = user_data['lcwaikiki_count'] + \
                    int(count)
                bot.send_message(message.chat.id, "Успешно")
                get_magazin(message)
                # print(user_data)
            else:
                bot.send_message(message.chat.id, "Не достаточно средств")
                get_magazin(message)
    except Exception as ex:
        bot.send_message(message.chat.id,
                         "Я вас не понял напишите еще раз")
        get_magazin(message)


def get_sertificat(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    callback_button1 = telebot.types.InlineKeyboardButton(
        text='Meloman', callback_data='meloman')
    callback_button2 = telebot.types.InlineKeyboardButton(
        text='Marwin', callback_data='marwin')
    callback_button3 = telebot.types.InlineKeyboardButton(
        text='LCWaikiki', callback_data='lcwaikiki')
    callback_button4 = telebot.types.InlineKeyboardButton(
        text='Назад', callback_data='nazad')
    keyboard.add(callback_button1, callback_button2,
                 callback_button3, callback_button4)
    bot.send_message(
        message.chat.id, 'Сертификаты\nОдин сертификат стоит 5000тг', reply_markup=keyboard)


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

listR_rus = ['Кассовые операции', 'Оформление кредита/депозита',
             'Денежные переводы', 'Консультации']
listR_kaz = ['Кассалық операциялар', 'Несие/депозит өндеу',
             'Ақша аударымдары', 'Консультациялар']

listRLists = [listR_rus, listR_kaz]

listIIN = ['Напишите свой ИИН:', "ИИН-iздi жазыныз:"]

listBalans = ['Ваш баланс:', 'Сiздiн балансыныз:', ]
listuVas = [' у вас ', ' сізде ']
listRebenok = [' ребенок\nРебенку дается подарок от 6 до 17 лет!!!',
               ' балаңыз бар\nБалаға 6 жастан бастап 17 жасқа дейін подарок беріледі !!!', ' детей\nРебенку дается подарок от 6 до 17 лет!!!']
list3Bank = ['Согласны ли вы? ', 'Келiсеciз бе?']

listSupport = ['Если вы не согланы обратитесь по номеру: 87077012916',
               'Егер сiз келiспесенiз мына номiрге конырау шалыныз:87077012916']

bot.polling(none_stop=False)
