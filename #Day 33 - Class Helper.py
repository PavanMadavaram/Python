#Day 33 - Class Helper
class Car:
    def __init__(self, brand):
        self.brand = brand

def print_car(car):
    print("Car brand:", car.brand)

mycar = Car("Tesla")
print_car(mycar)
