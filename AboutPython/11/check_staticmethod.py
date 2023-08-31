class MyClass:

    @staticmethod
    def on_sum_1(param_1, param_2):
        return param_1 + param_2
    
    def on_sum_2(self, param_1, param_2):
        return param_1 + param_2
    
    def on_sum_3(self, param_1, param_2):
        return MyClass.on_sum_1(param_1, param_2)


#print(MyClass.on_sum_1(20, 30))

ms = MyClass()
print(ms.on_sum_1(20, 30))
