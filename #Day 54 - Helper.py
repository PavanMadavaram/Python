#Day 54 - Helper
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

print(safe_divide(10, 0))