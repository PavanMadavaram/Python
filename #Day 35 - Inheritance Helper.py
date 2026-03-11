#Day 35 - Inheritance Helper
class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def code(self):
        print(self.name, "is coding")

dev = Developer("Sai")
dev.code()
