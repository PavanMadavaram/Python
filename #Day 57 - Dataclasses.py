#Day 57 - Dataclasses 
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: int
    salary: float

emp = Employee("Sai", 101, 50000)
print(emp)
print("Salary:", emp.salary)