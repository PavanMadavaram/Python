#Day 41 - Decorators
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Time: {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.5)  # Shorter delay
    return a + b

print("Result:", slow_add(2, 3))

