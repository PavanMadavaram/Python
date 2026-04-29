#Day 80 - Test
from functools import cache
@cache
def test(n): return n * 2
print("Functools test:", test(3) == 6)
print("Day 80 test ok")
