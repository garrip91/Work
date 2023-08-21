class Auto:

    def __init__(self):
        print("Автомобиль заведён")
        self.auto_name = "Mazda"
        self._auto_year = 2019
        self.__auto_model = "CX9"


a = Auto()
print(a.auto_name)
#print(a._Auto__auto_model)
print(a.auto_model)
