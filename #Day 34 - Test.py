#Day 34 - Test
class Box:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

b = Box()
b.add("a")
print("Items:", b.items)
print("Day 34 test ok")
