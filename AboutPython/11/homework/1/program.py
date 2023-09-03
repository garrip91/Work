#from datetime import datetime
import datetime


class DateClass:
    
    def __init__(self, day_month_year: str):
        self.day_month_year = day_month_year
    
    @classmethod
    def get_day_month_year(cls, obj):
        date_list = [int(n) for n in obj.day_month_year.split("-")]
        d = date_list[0]
        m = date_list[1]
        y = date_list[2]
        return y, m, d
    
    @staticmethod
    def is_date_valid(day_month_year: str):
        #return return datetime(*inp).date()
        return datetime.date(*day_month_year)


dc = DateClass("34-05-2023")
for_func = DateClass.get_day_month_year(dc)
#print(for_func)
check_staticmethod = DateClass.is_date_valid(for_func)
print(check_staticmethod)

#print(datetime.date(*[2023, 2, 28]))
