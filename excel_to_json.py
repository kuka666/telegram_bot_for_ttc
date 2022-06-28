import pandas
import json
from datetime import date


def between_date_day(from_date, to_date):
    from_date = from_date.split(".")
    to_date = to_date.split(".")
    result_date = date(int(to_date[2]), int(to_date[1]), int(
        to_date[0])) - date(int(from_date[2]), int(from_date[1]), int(from_date[0]))
    return result_date.days

data = []
user_data = {'iin': '870228350076', 'fio': 'Альменов Берик Бахитжанович', 'email': 'b.almenov@ttc.kz',
             'balans': '0', 'count_deti': '2', 'dengi': 75000, 'meloman_count': 1, 'marwin_count': 1, 'lcwaikiki_count': 1}
print(user_data)
user_data.clear()
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
print(user_data)
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
