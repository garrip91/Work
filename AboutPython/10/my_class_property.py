class MyClass:

    def __init__(self, param_1, param_2):
        self.param_1 = param_1
        self.param_2 = param_2
    
    @property
    def my_method(self):
        return f"Параметры, переданные в класс: {self.param_1}, {self.param_2}"


mc = MyClass("text_1", "text_2")

#print(mc.my_method())
print(mc.my_method)
