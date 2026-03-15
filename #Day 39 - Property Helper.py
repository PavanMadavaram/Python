#Day 39 - Property Helper
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

r = Rectangle(4, 6)
print("Rectangle area:", r.area)
