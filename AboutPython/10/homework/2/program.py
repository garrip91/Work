class Cloth:

    def __init__(self):
        pass
    
    @property
    def fabric_consumption(self):
        pass


class Coat(Cloth):

    def __init__(self, V):
        self.v = V
    
    @property
    def fabric_consumption(self):
        return self.v / 6.5 + 0.5


class Costume(Cloth):

    def __init__(self, H):
        self.h = H
    
    @property
    def fabric_consumption(self):
        return 2 * self.h + 0.3


coat = Coat(56)
#print(coat.fabric_consumption())
print(coat.fabric_consumption)
