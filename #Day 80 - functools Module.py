#Day 80 - functools Module 
from functools import cache, reduce, partial

# Cache (memoization)
@cache
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print("Fib 30:", fib(30))

# Reduce
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print("Product:", product)
