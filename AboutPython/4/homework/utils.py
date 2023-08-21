# -*- coding: utf-8 -*-
from requests import get, utils
import json
import xmltodict
from datetime import datetime


def dump_data():

    response = get("http://www.cbr.ru/scripts/XML_daily.asp")
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)

    with open(file="parsed_data.json", mode="w", encoding="utf-8") as file:
        json.dump(xmltodict.parse(content), file, ensure_ascii=False, indent=4)


def load_data():
    
    with open(file="parsed_data.json", mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def currency_rates_without_date(currency_numcode=None):
    
    needed_dicts_list = load_data()["ValCurs"]["Valute"]
    flag = None
    while flag == None:
        for valute in needed_dicts_list:
            if currency_numcode == valute["NumCode"]:
                flag = True
                return f"{valute['Nominal']} {valute['Name']} - это {valute['Value']} руб."
            else:
                flag = False
    if flag == None:
        return None


def currency_rates_with_date(currency_numcode=None):
    
    needed_dicts_list = load_data()["ValCurs"]["Valute"]
    flag = None
    while flag == None:
        for valute in needed_dicts_list:
            if currency_numcode == valute["NumCode"]:
                flag = True
                return f"По состоянию на {datetime.strptime(load_data()['ValCurs']['@Date'], '%d.%m.%Y').strftime('%d.%m.%Y')} {valute['Nominal']} {valute['Name']} - это {valute['Value']} руб."
            else:
                flag = False
    if flag == None:
        return None
