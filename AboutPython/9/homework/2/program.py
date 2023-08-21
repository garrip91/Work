class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def mass_of_asphalt(self):
        return self._length * self._width


road = Road(7, 8)
print(road.mass_of_asphalt())
