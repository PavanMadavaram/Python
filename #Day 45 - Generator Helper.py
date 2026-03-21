#Day 45 - Generator Helper
evens = (n for n in range(10) if n % 2 == 0)
print("Even numbers:", list(evens))
