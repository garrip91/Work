import pandas as pd


def create_csv_files():

    columns_1 = ["Surname", "Name", "Patronymic"]
    columns_2 = ["Hobby_1", "Hobby_2"]

    data_1 = [
        ["Иванов", "Иван", "Иванович"],
        ["Петров", "Пётр", "Петрович"]
    ]
    data_2 = [
        ["Скалолазание", "Охота"],
        ["Горные лыжи", None]
    ]

    df_1 = pd.DataFrame(data_1, columns=columns_1)
    df_1.to_csv(r"/home/garrip91/Programming/GitHub/Work/AboutPython/6/homework/3/users.csv")
    df_2 = pd.DataFrame(data_2, columns=columns_2)
    df_2.to_csv(r"/home/garrip91/Programming/GitHub/Work/AboutPython/6/homework/3/hobby.csv")
