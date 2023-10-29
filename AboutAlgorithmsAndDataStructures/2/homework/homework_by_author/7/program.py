"""
Task 7

Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""


def cycle_method(numb):
    """Цикл"""

    s = 0
    for i in range(1, numb+1):
        s += i
        m = numb * (numb + 1) // 2
    print(f"Равенство: {s == m}")


try:
    NUMB = int(input("Введите число:\n"))
    cycle_method(NUMB)
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")