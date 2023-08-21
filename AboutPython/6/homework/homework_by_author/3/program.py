"""
Task 3

Есть два файла: в одном хранятся Ф.И.О. пользователей сайта, а в другом - данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка - один пользователь, разделитель между значениями - запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи - Ф.И.О., значения - данные о хобби. Сохранить словарь в файл. Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с Ф.И.О., задаём в словаре значение None, если наоборот, выходим из скрипта с кодом "1".
При решении задачи считать, что объём данных в файлах во много раз меньше объёма ОЗУ.

Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Пётр,Петрович

Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
"""


from itertools import zip_longest
import json


out_dict = {}
with open(file="users.csv", mode="r", encoding="utf-8") as users:
    with open(file="hobby.csv", mode="r", encoding="utf-8") as hobby:
        num_lines_users = sum(1 for line in users)
        num_lines_hobby = sum(1 for line in hobby)

        if num_lines_users < num_lines_hobby:
            exit(1)
        
        users.seek(0)
        hobby.seek(0)
        for line_user, line_user_hobby in zip_longest(users, hobby):
            out_dict[line_user.strip()] = line_user_hobby.strip() if \
                line_user_hobby is not None else line_user_hobby

with open(file="task3.json", mode="w", encoding="utf-8") as f:
    json.dump(out_dict, f, ensure_ascii=False)
print(out_dict)
