#Day 97 - Context Helper
from contextlib import suppress

with suppress(ZeroDivisionError):
    print(10 / 0)

print("No crash due to suppress")