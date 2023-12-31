"""
Task 1

Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:

    |--my_project
        |--settings
        |--mainapp
        |--adminapp
        |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""


import os


# We can save .json
pattern = {
    "my_project": [
        "settings",
        "mainapp",
        "adminapp",
        "authapp"
    ]
}

for root, folders in pattern.items():
    if os.path.exists(root):
        print(f"{root.upper()} существует!")
    else:
        for folder in folders:
            current_dir = os.path.join(root, folder)
            if os.path.exists(current_dir):
                print(current_dir, "существует")
            else:
                os.makedirs(current_dir)
