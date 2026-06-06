#Day 105 - Test
from enum import Enum

class Level(Enum):
    LOW = 1
    HIGH = 2

print("Enum test:", Level.LOW.name == "LOW")
print("Day 105 test ok")