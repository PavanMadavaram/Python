#Day 108 - weakref Module 
import weakref

class Data:
    def __init__(self, value):
        self.value = value

obj = Data("hello")
ref = weakref.ref(obj)

print("Alive:", ref() is not None)
print("Value:", ref().value)

del obj
print("After delete:", ref())