#Day 80 - Functools Helper
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
print("2^2 =", square(2))
print("5^2 =", square(5))
