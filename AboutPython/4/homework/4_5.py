import sys
from utils import load_data
from datetime import datetime


def currency_rates_with_date(char_code=sys.argv[1]):
    
    needed_dicts_list = load_data()["ValCurs"]["Valute"]
    flag = None
    while flag == None:
        for valute in needed_dicts_list:
            if char_code == valute["CharCode"]:
                flag = True
                valute_value = float(valute['Value'].replace(",", "."))
                result_date = datetime.strptime(load_data()['ValCurs']['@Date'], '%d.%m.%Y').strftime('%Y-%m-%d')
                return f"{valute_value}, {result_date}"
            else:
                flag = False
    if flag == None:
        return None


#print(type(sys.argv))
#print(type(sys.argv[1]))
#print(sys.argv[1])
print(currency_rates_with_date())
