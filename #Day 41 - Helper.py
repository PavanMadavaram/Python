#Day 41 - Helper
def debug(func):
    def wrapper(*args):
        print(f"Calling {func.__name__} with {args}")
        return func(*args)
    return wrapper

@debug
def multiply(x, y):
    return x * y

print("Result:", multiply(4, 5))
