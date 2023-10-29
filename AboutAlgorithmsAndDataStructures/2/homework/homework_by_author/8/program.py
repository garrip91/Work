"""
Task 8

Посчитать сколько раз встречается определённая цифра в введённой последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

Пример:
Сколько будет чисел? 2
Какую цифру считать? 3
Число 1: 223
Число 2: 21
Было введено 1 цифр "3"
"""


def cycle_method(n, b):
    count = 0
    for i in range(1, n + 1):
        try:
            m = int(input(f"Число {str(i)}: "))
            while m > 0:
                if m % 10 == b:
                    count += 1
                m = m // 10
        except ValueError:
            print("Вы вместо числа ввели строку (((. Исправьтесь")
    print(f"Было введено {count} цифр '{b}'")


try:
    N = int(input("Сколько будет чисел?:\n"))
    B = int(input("Какую цифру считать?:\n"))
    cycle_method(N, B)
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
