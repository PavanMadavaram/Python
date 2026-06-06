#Day 105 - enum Module 
from enum import Enum, auto

class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print("Colors:")
for color in Color:
    print(color.name, color.value)