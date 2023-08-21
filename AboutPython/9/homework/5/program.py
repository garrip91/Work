class Stationery:

    def __init__(self, title):
        self.title = title
    
    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):

    def draw(self):
        return "Запуск отрисовки ручкой"


class Pencil(Stationery):

    def draw(self):
        return "Запуск отрисовки карандашом"


class Handle(Stationery):

    def draw(self):
        return "Запуск отрисовки маркером"


pen = Pen("ручка")
pencil = Pencil("карандаш")
handle = Handle("маркер")
print(pen.draw())
print(pencil.draw())
print(handle.draw())
