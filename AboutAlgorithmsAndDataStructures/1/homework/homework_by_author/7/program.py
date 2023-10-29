"""
Task 7

По длинам трёх отрезков, введённых пользователем, определить возможность существования треугольника, составленного из этих отрезков.
Если такой треугольник существует, то определить является ли он разносторонним, равнобедредренным или равносторонним.
"""


try:
    PARAM_A = int(input("a:\n"))
    PARAM_B = int(input("b:\n"))
    PARAM_C = int(input("c:\n"))

    if (PARAM_A + PARAM_B <= PARAM_C) or (PARAM_A + PARAM_C <= PARAM_B) or (PARAM_B + PARAM_C <= PARAM_A):
        print("Треугольника не существует!")
    elif (PARAM_A != PARAM_B) and (PARAM_A != PARAM_C) and (PARAM_B != PARAM_C):
        print("Треугольник разносторонний!")
    elif PARAM_A == PARAM_B == PARAM_C:
        print("Треугольник равносторонний!")
    else:
        print("Треугольник равнобедренный!")

except ValueError:
    print("Вы вместо числа ввели строку (((. Исправьтесь")
