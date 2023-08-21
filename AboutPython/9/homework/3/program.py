wage = float(input("Введите размер оклада сотрудника:\n"))
bonus = float(input("Введите размер премии сотрудника:\n"))


class Worker:

    def __init__(self, name, surname, position, income={"wage": wage, "bonus": bonus}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        return f"{self.name} {self.surname}"
    
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


position = Position("Сергей", "Гребенщиков", "кладовщик")
print(position.get_full_name())
print(position.get_total_income())
