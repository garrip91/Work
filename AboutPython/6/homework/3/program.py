import pandas as pd
from pandas import DataFrame
from utils import create_csv_files



with open(file="users_hobbies_dict.txt", mode="w", encoding="utf-8") as f:
    
    users = pd.read_csv("users.csv").fillna("None")
    hobbies = pd.read_csv("hobby.csv").fillna("None")

    users_list = [", ".join([data_1_j for data_1_j in data_1_i if type(data_1_j) != float][1:]).replace(",", "") for data_1_i in users.values.tolist()]
    hobbies_list = [", ".join([data_2_j for data_2_j in data_2_i if type(data_2_j) != float][1:]) for data_2_i in hobbies.values.tolist()]
    users_hobbies_dict = dict(zip(users_list, hobbies_list))

    f.write(str(users_hobbies_dict))


""" users = pd.read_csv("users.csv").fillna("None")
hobbies = pd.read_csv("hobby.csv").fillna("None")
users_list = [", ".join([data_1_j for data_1_j in data_1_i if type(data_1_j) != float][1:]).replace(",", "") for data_1_i in users.values.tolist()]
hobbies_list = [", ".join([data_2_j for data_2_j in data_2_i if type(data_2_j) != float][1:]) for data_2_i in hobbies.values.tolist()]
print(hobbies_list) """
