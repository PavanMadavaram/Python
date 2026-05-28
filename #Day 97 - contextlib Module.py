#Day 97 - contextlib Module 
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with managed_file("day97.txt", "w") as f:
    f.write("Hello from context manager")

print("File written safely")