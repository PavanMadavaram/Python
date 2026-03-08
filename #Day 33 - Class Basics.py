#Day 33 - Class Basics
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Pavan", 23)
print("Person:", p1.name, p1.age)
