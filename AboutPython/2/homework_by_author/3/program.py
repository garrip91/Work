my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

idx = 0
while idx < len(my_list):
    if my_list[idx].isdigit():
        my_list.insert(idx, '"')
        my_list[idx + 1] = f'{int(my_list[idx + 1]):02}'
        my_list.insert(idx + 2, '"')
        idx += 2
    elif (my_list[idx].startswith('+') or my_list[idx].startswith('-')) and my_list[idx][1:].isdigit():
        my_list.insert(idx, '"')
        my_list[idx + 1] = f'{my_list[idx + 1][0]}{int(my_list[idx + 1]):02}'
        my_list.insert(idx + 2, '"')
        idx += 2
    idx += 1

out_info = ' '.join(my_list) # to perfect out go to task 2
print(out_info)
