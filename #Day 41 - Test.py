#Day 41 - Test 
def simple_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@simple_decorator
def hello():
    print("Hello")

hello()
print("Day 41 test ok")
