#Day 51 - Helper
from collections import namedtuple

Student = namedtuple('Student', 'name rollno marks')
sai = Student('Sai', 101, 85)
print(f"Student: {sai.name} got {sai.marks}%")
