class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def go(self):
        return f"Машина поехала"

    def stop(self):
        return f"Машина остановилась"

    def turn_direction(self):
        return f"Машина повернула (куда-то)"
    
    def show_speed(self):
        return self.speed


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return "Вы превышаете предельно допустимую для данного транспортного средства скорость (60)!"
        else:
            return "Всё в порядке!"


class SportCar(Car):

    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return "Вы превышаете предельно допустимую для данного транспортного средства скорость (40)!"
        else:
            return "Всё в порядке!"


class PoliceCar(Car):

    pass


town_car = TownCar(40, "green", "Town_Car", False)
sport_car = SportCar(60, "red", "Sport_Car", False)
work_car = WorkCar(40, "brown", "Work_Car", False)
print(town_car.show_speed())
print(sport_car.show_speed())
print(work_car.show_speed())
