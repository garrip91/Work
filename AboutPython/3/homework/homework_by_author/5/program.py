# Task 5
"""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трёх случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["весёлый", "яркий", "зелёный", "утопичный", "мягкий"]

Например:
>>> get_jokes(2)
["лес завтра зелёный", "город вчера весёлый"]

Документировать код функции.
Сможете ли Вы добавить ещё один аргумент - флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли Вы сделать аргументы именованными?
"""


import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["весёлый", "яркий", "зелёный", "утопичный", "мягкий"]


def get_jokes(num):
    """Function to return jokes. num (int) - count of jokes """
    joke_list = []
    for i in range(num):
        cur_nouns = random.choice(nouns)
        cur_adverbs = random.choice(adverbs)
        cur_adjectives = random.choice(adjectives)
        joke_list.append(f"{cur_nouns} {cur_adverbs} {cur_adjectives}")
    return joke_list


def get_jokes_adv(num, repeats=True):

    joke_list = []

    if not repeats:
        if num > min(len(nouns), len(adverbs), len(adjectives)):
            return "No way"
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for i in range(num):
                joke_list.append(f"{nouns[i]} {adverbs[i]} {adjectives[i]}")
    else:
        for i in range(num):
            cur_nouns = random.choice(nouns)
            cur_adverbs = random.choice(adverbs)
            cur_adjctives = random.choice(adjectives)
            joke_list.append(f"{cur_nouns} {cur_adverbs} {cur_adjctives}")
    return joke_list


#print(get_jokes(1))
#print(get_jokes(2))

print(get_jokes_adv(4, False))
print(get_jokes_adv(5, False))
print(get_jokes_adv(6, False))
