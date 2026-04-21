#Day 72 - os Module 
import os

# Current directory
print("Current dir:", os.getcwd())
print("Files:", os.listdir('.'))

# Environment
print("Username:", os.getenv('USER', 'Unknown'))