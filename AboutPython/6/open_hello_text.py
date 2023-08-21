# with open(file="hello.txt", mode="r", encoding="utf-8") as file_1:
#     for line in file_1:
#         print(line)

# txt = """Пробуем записать в файл текст. Используем метод write()"""
# with open(file="write_method.txt", mode="w", encoding="utf-8") as f:
#     f.write(txt)

# txt_lines = ["Пробуем записать в файл текст.", "Используем метод .writelines()"]
# with open(file="writelines_method.txt", mode="w", encoding="utf-8") as f:
#     f.writelines(txt_lines)

# txt = '''Пробуем дозаписать в файл текст. Режим доступа "a"'''
# with open(file="append_text.txt", mode="a", encoding="utf-8") as f:
#     f.write(txt)

# with open(file="hello_2.txt", mode="r", encoding="utf-8") as f:
#     print(f.tell())
#     line = f.readline()
#     while line:
#         print(line.strip(), f.tell(), sep="\n")
#         line = f.readline()

with open(file="hello_2.txt", mode="r", encoding="utf-8") as f:
    f.seek(39)
    print(f.readline().strip())
    f.seek(142)
    print(f.readline().strip())
