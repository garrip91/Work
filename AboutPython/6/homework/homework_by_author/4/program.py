"""
Task 4

*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно создавать такие большие файлы, это просто задел на будущее проекта).
Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединённые данные в новый файл (users_hobby.txt).
Хобби пишем через двоеточие и пробел после Ф.И.О.:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Пётр,Петрович: горные лыжи
"""


from itertools import zip_longest


with open(file="task4.txt", mode="w", encoding="utf-8") as f:
    with open(file="users.csv", mode="r", encoding="utf-8") as users:
        with open(file="hobby.csv", mode="r", encoding="utf-8") as hobby:
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for line in hobby)
            
            if num_lines_users < num_lines_hobby:
                exit(1)
            
            users.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobby):
                f.write(f"{line_user.strip()}: "
                        f"{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n")
