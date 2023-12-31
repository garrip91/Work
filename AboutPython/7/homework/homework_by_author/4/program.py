"""
Task 4

Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи - верхняя граница размера файла (пусть будет кратна 10), а значения - общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:

    {
        100: 15,
        1000: 3,
        10000: 7,
        100000: 2
    }

Тут 15 файлов размером не более 100 байт;
3 файла больше 100 и не больше 1000 байт...
Подсказка:
размер файла можно получить из атрибута .st_size объекта os.stat
"""


import os


files = []
for r, d, f in os.walk("./"):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = 0

for file in files:
    out_dict[10 ** len(str(file))] += 1

print(out_dict)
