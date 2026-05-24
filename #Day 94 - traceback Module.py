#Day 94 - traceback Module 
import traceback

def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
    print(result)
except Exception as e:
    print("An error occurred:")
    traceback.print_exc()