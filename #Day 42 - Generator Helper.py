#Day 42 - Generator Helper
def even_numbers(limit):
    n = 0
    while n <= limit:
        if n % 2 == 0:
            yield n
        n += 1

print("Evens:", list(even_numbers(10)))
