#Day 54 - Advanced Exceptions 
try:
    num = int(input("Enter number: "))
    result = 10 / num
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Success:", result)
finally:
    print("Cleanup done")