"""
Task 3

Реализовать базовый класс Worker (работник), в котором определить атрибуты: name (имя), surname (фамилия), position (должность), income (доход).
Последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например: {"wage": wage, "bonus": bouns}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени работника (get_full_name) и дохода с учётом премии (get_total_income).
Проверить работу примера на реальных данных (создать зкземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income["wage"]
        self._income_bonus = income["bonus"]


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname} {self.position}"
    
    def get_total_income(self):
        return self._income_wage + self._income_bonus


position = Position("Ivan", "Ivanov", "senjor", {"wage": 150000, "bonus": 50000})
print(position.get_full_name())
print(position.get_total_income())
