"""
Task 3

Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или "руками" в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:

    |--my_project
        ...
        |--templates
        |    |--mainapp
    |   |    |    |--base.html
    |   |    |    |--index.html
        |    |--authapp
    |   |    |    |--base.html
    |   |    |    |--index.html

"""


import os
import shutil


my_dir = "task3" # save folder
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r"my_project" # search folder
files = []


for r, d, f in os.walk(folder):
    for file in f:
        if ".html" in file:
            files.append(os.path.join(r, file))
for path in files:
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
