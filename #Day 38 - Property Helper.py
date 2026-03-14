#Day 38 - Property Helper
class Counter:
    count = 0  # Class property

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print("Total objects:", Counter.count)
