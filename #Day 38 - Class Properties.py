#Day 38 - Class Properties 
class Student:
    school = "RGMC"  # Class property

    def __init__(self, name):
        self.name = name

s1 = Student("Sai")
s2 = Student("Ram")
print("School:", s1.school)
print("School:", s2.school)
