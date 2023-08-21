my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

new_list = []
for elem in my_list:
    if elem.isdigit():
        new_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        new_list.extend(['"', f'{elem[0]}{int(elem[1:]):02}', '"'])
    else:
        new_list.append(elem)

out_info = ' '.join(new_list)
print(out_info)

# to perfect out (delete whitespaces):
# find indexes with " symbol:
symbol_idxs = []
for idx, letter in enumerate(out_info):
    if letter == '"':
        symbol_idxs.append(idx)

# some logic to find delete indexes:
for idx in range(len(symbol_idxs)):
    if idx % 2 == 0:
        symbol_idxs[idx] = symbol_idxs[idx] + 1
    else:
        symbol_idxs[idx] = symbol_idxs[idx] - 1

# delete indexes from original string:
for del_idx in reversed(symbol_idxs):
    out_info = out_info[:del_idx] + out_info[del_idx+1:]
