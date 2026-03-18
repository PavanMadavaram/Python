#Day 42 - Generator Functions
def count_down(start):
    n = start
    while n > 0:
        yield n
        n -= 1

for num in count_down(5):
    print(num)
