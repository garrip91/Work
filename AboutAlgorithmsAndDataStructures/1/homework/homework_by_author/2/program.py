"""
Task 2

Выполнить логические побитовые операции "И", "ИЛИ" и другие над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на 2 знака.

Подсказка: это стандартные операции, которые осуществляются с помощью стандартных операторов.
Попробуйте найти каких именно.


Ещё в помощь:

Первые логические операции можно выполнить, используя знания таблиц истинности (из алгебры логики).

Логическое умножение "И":
101
110
----
100
Двоичное число 100 - это десятичное число 4.

Логическое сложение "ИЛИ":
101
110
---
111 - это число 7.

Исключающее "ИЛИ":
101
110
----
011 - это число 3.


При побитовом (логическом) сдвиге числа 5 (дв. 101) влево на 2 знака получаем число 10100 (дес. 20).
При таком сдвиге уходящий бит исчезает, не влияя на оставшиеся биты, а на месте появившегося бита записывается бит 0.

При сдвиге вправо получаем 101 >> 001, но т.к. начальные (незначащие) нули отбрасываются, то остаётся 1.
"""


NUM_A = 5
NUM_B = 6

print(f"Даны числа {NUM_A} и {NUM_B}")

# Логическое "И":
print("Логическое 'И': '0101' & '0110' = '0100', т.е. 4")
print(f"Логическое 'И': {NUM_A}&{NUM_B} = {NUM_A & NUM_B}")

# Логическое "ИЛИ":
print("Логическое 'ИЛИ': '0101' | '0110' = '111', т.е. 7")
print(f"Логическое 'ИЛИ': {NUM_A}|{NUM_B} = {NUM_A | NUM_B}")

# Логическое "ИСКЛЮЧАЮЩЕЕ ИЛИ":
print("Побитовое 'XOR': '0101' ^ '0110' = '011', т.е. 3")
print(f"Логическое 'ИСКЛЮЧАЮЩЕЕ ИЛИ': {NUM_A}^{NUM_B} = {NUM_A ^ NUM_B}")

# Логическое "ОТРИЦАНИЕ":
print("Побитовое 'НЕ': ~'00000101' = '11111010', т.е. -6")
print(f"Логическое 'ОТРИЦАНИЕ': ~{NUM_A} = {~NUM_A}")

# Логическое "СДВИГ ВЛЕВО":
print("Побитовое 'СДВИГ ВЛЕВО': '101' << 2 = '10100', т.е. 20 (5 * 2 ** 2)")
print(f"'СДВИГ ВЛЕВО' на 2 знака: {NUM_A} << 2 = {NUM_A<<2}")

# Логическое "СДВИГ ВПРАВО":
print("Побитовое 'СДВИГ ВПРАВО': '101' >> 2 = '001', т.е. 1 (5 // (2 ** 2))")
print(f"'СДВИГ ВПРАВО' на 2 знака: {NUM_A} >> 2 = {NUM_A>>2}")
