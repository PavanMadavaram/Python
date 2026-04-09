#Day 63 - os Helper
import os

files = [f for f in os.listdir(".") if f.endswith(".py")]
print("Python files:", len(files))