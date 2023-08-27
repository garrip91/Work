class One:

    def __init__(self, param_1="One_param_1", param_2="One_param_2", param_3="One_param_3"):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
        return self.param_1, self.param_2, self.param_3
    
    def method(self):
        return "Метод класса One"


class Two(One):

    def __init__(self, param_1="Two_param_1", param_2="Two_param_2", param_3="Two_param_3"):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
        return self.param_1, self.param_2, self.param_3
    
    def method(self):
        return "Метод класса Two"


class Three(Two):

    def __init__(self, param_1="Three_param_1", param_2="Three_param_2", param_3="Three_param_3"):
        #self.param_1 = param_1
        #self.param_2 = param_2
        #self.param_3 = param_3
        #super().__init__(param_1, param_2, param_3)
        #print(self.param_1, self.param_2, self.param_3)
        pass
        
    def some_method(self):    
        return super().method()


three = Three()
print(three.some_method())
