lst = [57.8, 46.51, 97, 98.58, 65.89, 69.88, 85.13, 45.30, 25.06, 81.3, 7.32, 11.83, 50.60, 1.2, 11.69, 55.43, 3, 33.42, 35.10, 63.96]

str_lst = [f"{str(i)[:str(i).find('.')]} руб. {str(i)[str(i).find('.')+1:]} коп." for i in lst]

str_lst = []
for i in lst:
    if type(i) == int and i < 10:
        str_lst.append(f"0{i} руб 00 коп")
    elif type(i) == int and i >= 10:
        str_lst.append(f"{i} руб 00 коп")
    else:
        if int(str(i).split(".")[0]) < 10 and int(str(i).split(".")[1]) < 10:
            str_lst.append(f"0{str(i).split('.')[0]} руб 0{str(i).split('.')[1]} коп")
        elif int(str(i).split(".")[0]) < 10 and int(str(i).split(".")[1]) >= 10:
            str_lst.append(f"0{str(i).split('.')[0]} руб {str(i).split('.')[1]} коп")
        elif int(str(i).split(".")[0]) >= 10 and int(str(i).split(".")[1]) < 10:
            str_lst.append(f"{str(i).split('.')[0]} руб 0{str(i).split('.')[1]} коп")
        else:
            str_lst.append(f"{str(i).split('.')[0]} руб {str(i).split('.')[1]} коп")

#print(", ".join(str_lst))

print(sorted(lst))

new_sort = sorted(lst, reverse=True)
print(new_sort)

the_dearest = new_sort[:5]
print(the_dearest)