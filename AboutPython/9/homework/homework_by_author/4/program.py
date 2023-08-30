"""
Task 4

Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (bool).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, поехала (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 для TownCar и 40 для для WorkCar должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам и выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        print(f"{self.name} is going!")
    
    def stop(self):
        print(f"{self.name} is stoping!")
    
    def turn(self, direction):
        print(f"{self.name} is turning to {direction}!")
    
    def show_speed(self):
        print(f"Current speed: {self.speed}!")


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Warning! Your speed is more than max!")


class SportCar(Car):

    pass


class WorkCar(Car):

    def show_speed(self):
        print(f"Current speed: {self.speed}!")
        if self.speed > 40:
            print("Warning! Your speed is more than max!")


class PoliceCar(Car):

    pass


sport_car = SportCar(240, "Красная", "Спортивная машина", False)
town_car = TownCar(140, "Серая", "Городская машина", False)
work_car = WorkCar(90, "Жёлтая", "Рабочая машина", False)
police_car = PoliceCar(210, "Синяя", "Полицейская машина", True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn("left")
