# Task3
# Реализовать склонение слова "процент" для чисел до 20.
# Например, задаём число 5 - получаем "5 процентов", задаём число 2 -
# получаем "2 процента". Вывести все склонения для проверки.


percent = int(input("Введите число процента:\n"))
if percent == 1:
    word = "процент"
elif percent <=4:
    word = "процента"
else:
    word= "процентов"

print(percent, word)