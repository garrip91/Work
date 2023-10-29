"""
Task 9

Вводятся три разных числа.
Найти то, которое среднее по значению (не самое большее и не самое меньшее).

Подсказка:
Можно добавить проверку, что введены равные числа.
"""


import sys


try:
    NUM_1 = int(input("Число 1:\n"))
    NUM_2 = int(input("Число 2:\n"))
    NUM_3 = int(input("Число 3:\n"))

    if NUM_1 == NUM_2 == NUM_3:
        print("Введены одинаковые числа!")
        sys.exit(1)
    
    if (NUM_2 < NUM_1 < NUM_3) or (NUM_3 < NUM_1 < NUM_2):
        print(f"Среднее: {NUM_1}")
    elif (NUM_1 < NUM_2 < NUM_3) or (NUM_3 < NUM_2 < NUM_1):
        print(f"Среднее: {NUM_2}")
    else:
        print(f"Среднее: {NUM_3}")

except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
