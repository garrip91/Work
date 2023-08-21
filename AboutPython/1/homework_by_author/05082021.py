# type()

# a = 'qwe'
# b = 5

# var1 = ['qwe', 10, 'q', 'qe', 'q', 'e', 50]
# print(var1[1:])  # [start:stop:step]
# print(var1[:3])  # [start:stop:step]
# print(var1[::2])  # [start:stop:step]
# print(var1[1::2])  # [start:stop:step]
# print(var1[1:4:2])  # [start:stop:step]
# print(var1[::-1])  # [start:stop:step]
# print(var1[::-2])  # [start:stop:step]
# print(id(var1))
# var2 = ['123', 10]
# print(type(var) == list)
# print(isinstance(var, list))
# print(dir(var))
# var.append(100)
# var1.extend(var2)
# var1.append(var2)
# x = var1.pop()
# x = var1.pop(0)
# print(var1.count('q'))
# print(var1.index('q', 3))
# var1.insert(1, 'qweqwewq')
# var1.remove(10)
# var2 = list(reversed(var1))
# var2 = list(reversed(var1))
# print(id(var1))
# print(var2)


# a = [10, 20, 30]

# b = a.copy()
# b.append(100)
# print(id(a) == id(b))
# print(a is b)
# print(a)

# a = 258
# b = 258
# print(a == b)
# print(a is b)

# a = 5
# print(id(a))
# b = 5
# print(id(b))



var1 = ['декабрь', 'январь', 'февраль',]
# var1[0] = 'qwe'
# var1.sort()
# var2 = sorted(var1)
# print(var1)
# print(var2)
# print(ord('д'))
# print(ord('я'))

# var3 = ('декабрь', 'январь', 'февраль')
# print(var3)

# import sys
# var1 = ['декабрь', 'январь', 'февраль']
# print(sys.getsizeof(var1))
# var3 = ('декабрь', 'январь', 'февраль')
# print(sys.getsizeof(var3))


# import copy
# a = [10, 20, 30, [100, 200]]
#
# b = copy.deepcopy(a)
# b[3].append(300)
# # print(id(a) == id(b))
# # print(a is b)
# # print(a)
# print(a)


# print(chr(ord('a')-32))
# print(chr(98-32))
# print('qwe asd zxc ASDAS'.capitalize())
# print('qwe asd zxc ASDAS'.title())
# print('qwe asd zxc ASDAS'.lower())
# print('qwe asd zxc ASDAS'.upper())

# my_list = ['qwe', 'asd', 'zxc']
# print('_'.join(my_list))

# my_str = 'qwe_asd_zxc'
# my_str = 'Ivan Ivanov zxc asd zxc zx czx czx c'
# my_list = my_str.split()
# print(my_list[0], my_list[1])
# name, surname, *data = my_str.split()
# print(my_list[-2:])
# print(name, surname, data)

name, day, money = 'Ivan', 20000, 564.448545415416541
print('Имя:', name, 'Год:', day)
print('Имя: %s Год: %d' % (name, day))
print('Имя: {} Год: {}'.format(name, day))
print(f'Имя: {name:^15} Год: {day:02d} Деньги {money:.3f}')