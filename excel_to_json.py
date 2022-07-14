from enum import unique
import re
from isort import file
import pandas as pd
import json
from datetime import date
import excel2json
from regex import B, F
import requests
from conversiontools import ConversionClient
import csv
from deepdiff import DeepDiff
import excel2json
# def between_date_day(from_date, to_date):
#     from_date = from_date.split(".")
#     to_date = to_date.split(".")
#     result_date = date(int(to_date[2]), int(to_date[1]), int(
#         to_date[0])) - date(int(from_date[2]), int(from_date[1]), int(from_date[0]))
#     return result_date.days

# data = []
# user_data = {'iin': '870228350076', 'fio': 'Альменов Берик Бахитжанович', 'email': 'b.almenov@ttc.kz',
#              'balans': '0', 'count_deti': '2', 'dengi': 75000, 'meloman_count': 1, 'marwin_count': 1, 'lcwaikiki_count': 1}
# print(user_data)
# user_data.clear()
# user_data = {
#     'iin': '',
#     'fio': '',
#     'email': '',
#     'balans': '',
#     'count_deti': '',
#     'dengi': 0,
#     'meloman_count': 0,
#     'marwin_count': 0,
#     'lcwaikiki_count': 0
# }
# print(user_data)
# user_data1 = {'iin': '030804500801', 'fio': 'Куаныш Мансуров Галымжанович', 'email': 'k.mansurov@ttc.kz',
#              'balans': '0', 'count_deti': '1', 'dengi': 45000, 'meloman_count': 0, 'marwin_count': 0, 'lcwaikiki_count': 0}
# with open('result.json', 'w',encoding='utf8') as f:
#     f.write(json.dumps(data, ensure_ascii=False))

# with open('result.json', encoding='utf-8') as file:
#     data = json.load(file)
# # 2. Update json object
# data.append(user_data)
# print(data)
# # 3. Write json file
# with open('result.json', "w",encoding='utf8') as file:
#     file.write(json.dumps(data, ensure_ascii=False))
# with open('result.json', encoding='utf-8') as res:
#     check = json.load(res)

# print(check[0])


def change_number_to_emoji(word):
    strings = list(word)
    new_strings = []
    for string in strings:
        if(string == '0'):
            new_string = string.replace("0", "0️⃣")
            new_strings.append(new_string)
        if(string == '1'):
            new_string = string.replace("1", "1️⃣")
            new_strings.append(new_string)
        if(string == '2'):
            new_string = string.replace("2", "2️⃣")
            new_strings.append(new_string)
        if(string == '3'):
            new_string = string.replace("3", "3️⃣")
            new_strings.append(new_string)
        if(string == '4'):
            new_string = string.replace("4", "4️⃣")
            new_strings.append(new_string)
        if(string == '5'):
            new_string = string.replace("5", "5️⃣")
            new_strings.append(new_string)
        if(string == '6'):
            new_string = string.replace("6", "6️⃣")
            new_strings.append(new_string)
        if(string == '7'):
            new_string = string.replace("7", "7️⃣")
            new_strings.append(new_string)
        if(string == '8'):
            new_string = string.replace("8", "8️⃣")
            new_strings.append(new_string)
        if(string == '9'):
            new_string = string.replace("9", "9️⃣")
            new_strings.append(new_string)
    result = ''.join(new_strings)
    return(result)


def add_plus(kuka):
    global res
    res = kuka
    a = re.sub("[0-9]", "", res)
    b = "".join(c for c in res if c.isdecimal())
    b = str(int(b)+1)
    print(a, b)
# def save_data(user_data):
#     with open('result.json', encoding='utf-8') as file:
#         data = json.load(file)
#     minimal = 0
#     for txt in data:
#         if txt['phone_number'] == user_data['phone_number']:
#             data.pop(minimal)
#         else:
#             None
#         minimal = minimal + 1
#     data.append(user_data)
#     with open('result.json', "w", encoding='utf8') as file:
#         file.write(json.dumps(data, ensure_ascii=False))
# df_json = pd.read_json('all.json')
# df_json.to_excel('all.xlsx')

# def get_saved_person_for_excel():
#     with open('result.json', encoding='utf-8') as file:
#         data = json.load(file)
#     for i in data:
#         if i['save'] == True and i['sended'] == False:
#             result = {
#                 'ФИО Сотрудника': i['fio'],
#                 'ИИН Сотрудника': i['iin'],
#                 'Число детей': i['count_deti'],
#                 'Информация о Ребенке': i['comment'],
#                 'Денежная компенсация': i['dengi'],
#                 'Спортмастер сертификаты': i['sportmaster_count'],
#                 'Mechta сертификаты': i['mechta_count'],
#                 'LC Waikiki сертификаты': i['lcwaikiki_count']
#             }
#     with open('all.json', encoding='utf-8') as files:
#         data = json.load(files)
#     data.append(result)
#     with open('all.json', "w", encoding='utf8') as f:
#         f.write(json.dumps(data, ensure_ascii=False))

#     df_json = pd.read_json('all.json')
#     df_json.to_excel('all.xlsx')

# get_saved_person_for_excel()

# client = ConversionClient('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImI2ZmI4NjAzNDk2NjQ4MjJiMmZjYzQ1Y2NmODY0NWEwIiwiaWF0IjoxNjU3MjEzMDUyfQ.PHN_7SBLWyzvBfMk4sBOtk55tN_Z53dFbW3EIUmlucw')
# try:
#     client.convert('convert.json_objects_to_excel', 'all.json', 'all.xlsx', { 'excel_format': 'xlsx' })
# except Exception as error:
#     print(error)

# url = 'https://green.ttc.kz/node/enzp/api/'
# result = requests.request(
#     'GET', url, headers={}, data={}, verify=False)
# fio  = 'Альменов Берик Бахитжанович'
# if result.status_code == 200:
#     json_result = result.json()
#     for item in json_result:
#         if(item['fio'] == fio):
#             print(item['iin'])

# # Read excel document
# excel_data_df = pd.read_excel('svod.xlsx', sheet_name='Лист1')

# # Convert excel to string
# # (define orientation of document in this case from up to down)
# thisisjson = excel_data_df.to_json(orient='records')

# # Make the string into a list to be able to input in to a JSON-file
# thisisjson_dict = json.loads(thisisjson)

# # Define file to write to and 'w' for write option -> json.dump()
# # defining the list to write from and file to write to
# with open('kuka.json', 'w') as json_file:
#     json.dump(thisisjson_dict, json_file)


# user = []
# with open('lol.json', encoding='utf-8') as file:
#     data = json.load(file)
# a = 0
# for i in data:
#     if(i['ФИО'] != None):
#         user[a] = {
#             'name': i['ФИО'],
#             'name_reb': i['ФИО'],
#             'date': i['данные по ребенку']
#         }
#         a = a + 1
# print(user[1])

# with open('1.json', encoding='utf-8') as file:
#     stock = json.load(file)
# with open('2.json', encoding='utf-8') as f:
#     bot = json.loads(f.read())

# def sort_by_key(list):
#     return list['Сотрудник']
# def sort_by_fio(list):
#     return list['фио']
# print(sorted(stock, key=sort_by_key))
# with open('1.json', "w", encoding='utf8') as f:
#     f.write(json.dumps(sorted(stock, key=sort_by_key), ensure_ascii=False))
# with open('2.json', "w", encoding='utf8') as f:
#     f.write(json.dumps(sorted(bot, key=sort_by_fio), ensure_ascii=False))

# user_data = list()
# user_data1 = list()
# for i in stock:
#     user_data.append(i['Сотрудник'])
# for b in bot:
#     user_data1.append(b['фио'])

# if(user_data.sort()==user_data1.sort()):
#     print(user_data)

# with open('1.json', "w", encoding='utf8') as f:
#     f.write(json.dumps(user_data, ensure_ascii=False))
# with open('2.json', "w", encoding='utf8') as f:
#     f.write(json.dumps(user_data1, ensure_ascii=False))
# user_data = {
#     "iin": "870228350076",
#     "fio": "Альменов Берик Бахитжанович",
#     "phone_number": "77077012916",
#     "balans": "90000",
#     "count_deti": "",
#     "dengi": 0,
#     "sportmaster_count": {
#         "type_nominal": "",
#         "count_10000": 0,
#         "count_15000": 0,
#         "count_25000": 0
#     },
#     "mechta_count": {
#         "type_nominal": "",
#         "count_10000": 0,
#         "count_15000": 0,
#         "count_25000": 0
#     },
#     "lcwaikiki_count": {
#         "type_nominal": "",
#         "count_10000": 0,
#         "count_15000": 0,
#         "count_25000": 0
#     },
#     "dengi_count": {
#         "type_nominal": "",
#         "count_5000": 0,
#         "count_10000": 0,
#         "count_15000": 0,
#         "count_25000": 0
#     },
#     "lok": "",
#     "accept": True,
#     "save": True,
#     "lang": "Русский язык",
#     "sended": False,
#     "comment": [
#             {
#                 "ФИО Ребегнка": "Бахитжанов Арман Берикович",
#                 "Дата рождения ребенка": "04.09.2010",
#                 "Возраст": "12"
#             },
#         {
#                 "ФИО Ребегнка": "Бахитжанова Перизат Берикович",
#                 "Дата рождения ребенка": "05.10.2008",
#                 "Возраст": "13"
#         }
#     ]
# }

# print(user_data)

# with open('1.json', encoding='utf-8') as file:
#     stock = json.load(file)
# with open('2.json', encoding='utf-8') as f:
#     bot = json.loads(f.read())
# print(len(bot))

# if(stock[0].replace(" ","")!=bot[0].replace(" ","")):
#     print(bot)

a = 1
user_data = []
rod_data = []
counts = []
kuka = []

# ## ОТСЮДА 1
# with open('1.json', encoding='utf-8') as file:
#     bot = json.load(file)
# for i in bot :
#     if 'дата рождения' in i:
#         with open('2.json', encoding='utf-8') as files:
#             data = json.load(files)
#         data.append(i)
#         with open('2.json', 'w', encoding='utf-8') as f:
#             f.write(json.dumps(data, ensure_ascii=False))
# ## ДОСЮДА 1
# ОТСЮДА 2
# with open('1.json', encoding='utf-8') as file:
#     bot = json.load(file)
# with open('2.json', encoding='utf-8') as f:
#     data = json.loads(f.read())

# for i in data:
#     user_data.append(i)

# for b in bot:
#     if(b['№'] == str(a)):
#         a = a + 1
#         rod_data.append(b)

# for c in range(len(user_data)):
#     counts.append(user_data[c]['№'])

# with open('kuka.json', encoding='utf-8') as files:
#     kuka = json.load(files)
# print(len(kuka))
# for i in range(len(user_data)):
#     if(int(user_data[i]['№']) == int(counts[i])):
#         result = {
#             "ФИО": rod_data[int(counts[i])-1]['ФИО'],
#             "ФИО Ребенка": user_data[i]['ФИО'],
#             "Дата рождения Ребенка": user_data[i]['дата рождения'],
#             "Филиал": rod_data[int(counts[i])-1]['филиал'],
#             "ИИН": "",
#             "Телефон": ""
#         }
#         kuka.append(result)
# with open('kuka.json', "w", encoding='utf8') as f:
#     f.write(json.dumps(kuka, ensure_ascii=False))
# ОТСЮДА 2

# for data in range(user_data):
#     if(rod_data[int(counts[i])]['№'] == user_data[int(data)]['№']):
#         rod_data[0]['филиал'] = user_data[0]
# print(rod_data)
# baby = []
# for i in range(len(user_data)):
#     if(user_data[i]['№'] == counts[i]):
#         baby.append({"ФИО Ребенка": user_data[i]['ФИО']})
# print(baby)
# rod_data[int(data)-1]['филиал'] = 0
# print(rod_data)

# for a in range(235):
#     if(user_data[a]['№'] == )
#     a = a +1
# if((int(i['№']) == int(a)) ):
#     i['Дети'] = { "ФИО": user_data['ФИО'],
#         "дата рождения ": user_data['дата рождения '],
#         "лет": user_data['лет'],
#         "дней": user_data['дней'],
#         "ребенок": user_data['ребенок']}
# print(i)
# a = a +1

with open('kuka.json', encoding='utf-8') as files:
    kuka = json.load(files)
with open('contact.json', encoding='utf-8') as f:
    contact = json.load(f)
kuka_json = []
contact_json = []
for i in kuka:
    kuka_json.append(i)
for b in contact:
    contact_json.append(b)
c = 0
strip_contact_json = []
problem_contact_json = []

# print(contact_json)
with open('u.json', encoding='utf-8') as files:
    data = json.load(files)
print(len(data))
# for b in range(len(contact_json)):
#     for i in range(len(kuka_json)):
#         if(kuka_json[i]['ФИО'].replace(" ", "")==contact_json[b]['ФИО'].replace(" ", "")):
#             all = {
#                 "ФИО": kuka_json[i]['ФИО'],
#                 "ФИО Ребенка": kuka_json[i]['ФИО Ребенка'],
#                 "Дата рождения Ребенка": kuka_json[i]['Дата рождения Ребенка'],
#                 "Филиал": kuka_json[i]['Филиал'],
#                 "ИИН": contact_json[b]['ИНН'],
#                 "Телефон": contact_json[b]['Телефон']
#             }      
#             data.append(all)

# with open('u.json', "w", encoding='utf8') as f:
#     f.write(json.dumps(data, ensure_ascii=False))


# for b in range(len(contact_json)):
#     strip_contact_json.append(contact_json[b]['ФИО'].replace(" ",""))

# for i in range(len(kuka_json)):
#     if kuka_json[i]['ФИО'].replace(" ","") in strip_contact_json:
#         kuka = {
#             "ФИО": kuka_json[i]['ФИО'],
#             "ФИО Ребенка": kuka_json[i]['ФИО Ребенка'],
#             "Дата рождения Ребенка": kuka_json[i]['ФИО Ребенка'],
#             "Филиал": "Цент. аппарат",
#             "ИИН": "",
#             "Телефон": ""
#         }
#     else:
#         problem_contact_json.append(kuka_json[i]['ФИО'])

# print(str(len(kuka_json)) + " " + str(c))

# sam_list = list(set(problem_contact_json))

# print(sam_list)
# print(len(sam_list))

# unique = { each['ФИО'] : each for each in kuka }.values()

# for i in unique:
#     result = {
#         "ФИО": i['ФИО']
#     }
#     names.append(result)
# with open('names.json', "w", encoding='utf8') as f:
#     f.write(json.dumps(names, ensure_ascii=False))
# client = ConversionClient(
#     'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImI2ZmI4NjAzNDk2NjQ4MjJiMmZjYzQ1Y2NmODY0NWEwIiwiaWF0IjoxNjU3MjEzMDUyfQ.PHN_7SBLWyzvBfMk4sBOtk55tN_Z53dFbW3EIUmlucw')
# try:
#     client.convert('convert.json_objects_to_excel',
#                     'names.json', 'names.xlsx', {'excel_format': 'xlsx'})
# except Exception as error:
#     print(error)

# with open('kuka.json', encoding='utf-8') as files:
#     kuka = json.load(files)

# print(len(kuka))

# with open('kuka.json', encoding='utf-8') as file:
#     kuka = json.load(file)
# with open('contact.json', encoding='utf-8') as f:
#     contact = json.loads(f.read())
# kuka_json = []
# contact_json = []
# for i in kuka:
#     kuka_json.append(i)
# for b in contact:
#     contact_json.append(b)
# c = 0
# for i in kuka_json:
#     for a in contact_json:
#         if(kuka_json[i]['ФИО'] == contact_json[a]['ФИО']):
#             c = c+1
#             print(c)

# print(str(len(kuka_json)) + " " + str(c))
