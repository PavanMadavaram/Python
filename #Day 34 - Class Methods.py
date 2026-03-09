#Day 34 - Class Methods
class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1

c = Counter()
c.inc()
c.inc()
print("Counter:", c.value)
