#Day 23 - Try Except
try:
    number = int("abc")
    print("Number:", number)
except ValueError:
    print("Not a valid number!")
