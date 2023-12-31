"""
Task 2

*(вместо 1) Найти IP-адрес спамера и кол-во отправленных им запросов по данным файла логов из предыдущего задания.
Примечание: спамер - это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых превышает объём ОЗУ компьютера.
"""


with open(file="nginx_logs.txt", mode="r", encoding="utf-8") as f:
    data = []
    spam_dict = {}
    for line in f:
        splitted = line.split()
        data.append((splitted[0], splitted[5].replace('"', ''), splitted[6]))
        spam_dict.setdefault(splitted[0], 0)
        spam_dict[splitted[0]] += 1

spam_dict = sorted(spam_dict.items(), key=lambda x: x[1], reverse=True)
print(spam_dict[:5]) # Not only one spamer
