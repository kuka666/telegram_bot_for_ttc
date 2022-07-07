import re
import pandas as pd
import json
from datetime import date
import excel2json
from conversiontools import ConversionClient
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
            new_string = string.replace("9","9️⃣")
            new_strings.append(new_string)
    result =''.join(new_strings)
    return(result)

def add_plus(kuka):
    global res
    res = kuka
    a = re.sub("[0-9]", "", res)
    b = "".join(c for c in res if  c.isdecimal())
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