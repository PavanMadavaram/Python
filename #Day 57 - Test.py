#Day 57 - Test
from dataclasses import dataclass

@dataclass
class Test:
    value: int

t = Test(42)
print("Dataclass:", t)
print("Day 57 test ok")