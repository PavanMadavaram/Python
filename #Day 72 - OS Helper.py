#Day 72 - OS Helper
import os

# File operations
if os.path.exists('test.txt'):
    os.remove('test.txt')
print("Path exists:", os.path.exists('day72.py'))