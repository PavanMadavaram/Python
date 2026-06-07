#Day 106 - dataclasses Module 
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    age: int
    grade: float

s1 = Student("Aarav", 16, 91.5)
s2 = Student("Meera", 15, 94.0)

print(s1)
print(s2)