class Phone:

    def __init__(self, model_name):
        self.phone_name = model_name
        self.__serial_number = 298329843
        self._loading()
    
    def get_serial_number(self):
        return self.__serial_number
    
    def call(self):
        print("calling...")
    
    def _loading(self):
        print(f"{self.phone_name} loading...")


class SmartPhone(Phone):

    def sms(self):
        print("smsing...")
    
    def email(self):
        print("emailing...")


class IPhone(SmartPhone):

    def __init__(self, model_name):
        super().__init__(model_name)
        print("show Apple logo")
    
    def player(self):
        print("music")
    
    def browser(self):
        print("browser")
    
    def sms(self):
        print("Imessage sending...")
        super().sms()


class Player:

    def player_method(self):
        print("Родительский класс метода Player")
    
    def qwe(self):
        print("Player_qwe")


class Navigator:

    def navigator_method(self):
        print("Родительский класс метода Navigator")
    
    def qwe(self):
        print("Navigator_qwe")


class MPhone(Player, Navigator):

    def mphone_method(self):
        print("MPhone")


class Auto:

    def auto_start(self, p1, p2):
        if isinstance(p1, int) and isinstance(p2, int):
            print(p1 + p2)
        else:
            print(None)


a = Auto()
a.auto_start(10, "20")
a.auto_start(10, 20)
