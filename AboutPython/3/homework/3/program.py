names = ["Александр", "Алексей", "Анатолий", "Андрей", "Антон", "Аркадий", "Арсений", "Артём", "Артур", "Борис", "Вадим", "Валентин", "Валерий", "Василий", "Виктор", "Виталий", "Владимир", "Владислав", "Вячеслав", "Георгий", "Глеб", "Григорий", "Даниил", "Денис", "Дмитрий", "Евгений", "Егор", "Иван", "Игорь", "Илья", "Кирилл", "Константин", "Лев", "Леонид", "Максим", "Марк", "Матвей", "Михаил", "Никита", "Николай", "Олег", "Павел", "Пётр", "Роман", "Руслан", "Сергей", "Степан", "Тимур", "Фёдор", "Юрий", "Ян", "Ярослав"]


#def thesaurus(names=names):
def thesaurus(*names):
 
    first_letters_list = []
    for name in names:
        if name[0] in first_letters_list:
            continue
        else:
            first_letters_list.append(name[0])
    
    result_dict = dict()
    for first_letter in first_letters_list:
        names_sublist = []
        for name in names:
            if name[0] == first_letter:
                names_sublist.append(name)
        result_dict[first_letter] = names_sublist
    
    return result_dict


print(thesaurus("dfg", "edg", "dcvb"))
