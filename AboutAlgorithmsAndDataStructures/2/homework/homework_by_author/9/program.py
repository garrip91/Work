"""
Task 9

Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.

Пример:
Введите количество чисел: 2
Введите очередное число: 23
Введите очередное число: 2
Наибольшее число по сумме цифр: 23, сумма его цифр: 5
"""


def cycle_method(quant):
    """Цикл"""

    steps = 0
    max_sum = 0
    for _ in range(0, quant):
        try:
            numb = input("Введите очередное число:\n")
            summ = 0
            for i in numb:
                summ += int(i)
            if summ > max_sum:
                max_sum = summ
                highest_numb = numb
            steps += 1
        except ValueError:
            print("Вы вместо числа ввели строку (((. Исправьтесь")
    
    return f"Наибольшее число по сумме цифр: {highest_numb}, сумма его цифр: {max_sum}"


try:
    QUANT = int(input("Введите количество чисел:\n"))
    print(cycle_method(QUANT))
except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
