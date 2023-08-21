lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+05', 'градусов']
result = [i for i in lst]

result_list = []
for i in lst:
    if i.strip("+").strip("-").isdigit():
        if len(i) == 1:
            result_list.extend(['"', f'0{i}', '"'])
        else:
            result_list.extend(['"', i, '"'])
    else:
        result_list.append(i)
#print(result_list)

new_result_list = []
for i in result_list:
    if i.strip("+").strip("-").isdigit():
        new_result_list.append(f'"{i}"')
    elif i == '"':
        continue
    else:
        new_result_list.append(i)

#print(new_result_list)

print(" ".join(new_result_list))
