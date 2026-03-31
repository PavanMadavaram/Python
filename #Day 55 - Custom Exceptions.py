#Day 55 - Custom Exceptions 
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError("Age must be 0-150")
    print("Valid age:", age)

try:
    check_age(-5)
except InvalidAgeError as e:
    print("Error:", e)