"""
Task 8

Определить является ли год, введённый пользователем, високосным или невисокосным.

Подсказка:
Год является високосным в двух случаях: либо он кратен числу 4, но при этом не кратен числу 100, либо кратен числу 400.

Попробуйте решить задачу двумя способами:
1. Обычное ветвление
2. Тернарный оператор

P.S.:
Тернарные операторы, также известные как условные выражения, представляют собой операторы, которые оценивают что-либо на основе условия, являющегося истинным или ложным.
Он был добавлен в Python версии, начиная с 2.5, и просто позволяет протестировать условие в одной строке, заменяя многострочное if-else, делая код компактным.
"""


def func_1(year):
    """Вариант № 1"""
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print(f"Год {year} - високосный!")
    else:
        print(f"Год {year} - невисокосный!")

def func_2(year):
    """Вариант № 2"""
    answer = "високосный" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "невисокосный"
    print(f"Год {year} - {answer}!")


try:
    YEAR = int(input("Введите год:\n"))
    func_1(YEAR)
    func_2(YEAR)

except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
