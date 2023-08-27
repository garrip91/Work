# класс Auto:
class Auto:

    # конструктор класса Auto:
    def __init__(self, year):
        # инициализация свойств:
        self.year = year
    
    # создаём свойство года:
    @property
    def year(self):
        return self.__year
    
    # сеттер для создания свойств:
    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2019:
            self.__year = 2019
        else:
            self.__year = year
    
    def get_auto_year(self):
        return f"Автомобиль выпущен в {str(self.year)} году"


a = Auto(1999)
print(a.get_auto_year())
