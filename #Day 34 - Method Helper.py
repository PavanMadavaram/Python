#Day 34 - Method Helper
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello {self.name}"

g = Greeter("Python")
print(g.greet())
