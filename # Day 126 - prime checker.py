# Day 126 - prime checker

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [2, 3, 4, 17, 20, 29]
for n in nums:
    print(n, is_prime(n))