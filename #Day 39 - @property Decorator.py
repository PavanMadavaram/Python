#Day 39 - @property Decorator 
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

c = Circle(5)
print("Radius:", c.radius)
print("Area:", c.area)
