#Day 97 - Test
from contextlib import nullcontext

with nullcontext(123) as x:
    print("Context test:", x == 123)
print("Day 97 test ok")