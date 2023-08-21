import random


# choice
#result_list.append(" ".join([random.choice(lst) for lst in lists]))

def get_jokes(dont_repeat_flag:bool, n:int=1) -> list:
    """
        Возвращает n шуток, сформированных из трёх случайных слов,
        взятых из трёх списков (по одному из каждого)
        Обязательно укажите хотите ли Вы чтобы слова повторялись или нет!
        Если хотите, то передайте функции при её вызове dont_repeat_flag=False,
        а если не хотите, то передайте функции dont_repeat_flag=True
    """
    
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["весёлый", "яркий", "зелёный", "утопичный", "мягкий"]

    lists = [nouns, adverbs, adjectives]
    
    #result_list = [random.choice(lst) for lst in lists]

    result_list = []
    for i in range(n):
        #for lst in lists:
        #    pre_list = []
        #    if not dont_repeat_flag:
        #        pre_list.extend([random.choice(lst) for lst in lists])
        #        #pre_list.extend([random.choice(lst) for lst in lst])
        #        result_list.append(" ".join(pre_list))
        #    #else:
        #    #    result_list.append(random.choice(lst))
        #    #    lst.remove(result_list[-1])
        pre_list = []
        if dont_repeat_flag:
            pre_list.extend([random.choice(lst) for lst in lists])
            result_list.append(" ".join(pre_list))
            for item in pre_list:
                try:
                    nouns.remove(item)
                except ValueError:
                    pass
                try:
                    adverbs.remove(item)
                except ValueError:
                    pass
                try:
                    adjectives.remove(item)
                except ValueError:
                    pass
        else:
            pre_list.extend([random.choice(lst) for lst in lists])
            result_list.append(" ".join(pre_list))

    return f"{pre_list}\n{result_list}\n{nouns}\n{adverbs}\n{adjectives}"


#print(get_jokes.__doc__)
print(get_jokes(dont_repeat_flag=False, n=3))
