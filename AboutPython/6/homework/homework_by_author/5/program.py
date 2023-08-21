"""
Task 5

**(вместо 4). Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имена обоих исходных файлов и имя выходного файла.
Проверить работу скрипта.
"""


import sys
from itertools import zip_longest


users, hobby, out = sys.argv[1:]
with open(file=out, mode="w", encoding="utf-8") as f:
    with open(file=users, mode="r", encoding="utf-8") as users:
        with open(file=hobby, mode="r", encoding="utf-8") as hobby:
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for line in hobby)

            if num_lines_users < num_lines_hobby:
                exit(1)
            
            users.seek(0)
            hobby.seek(0)
            for line_user, line_user_hobby in zip_longest(users, hobby):
                f.write(f"{line_user.strip()}: "
                        f"{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n")
