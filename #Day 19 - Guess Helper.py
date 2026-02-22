#Day 19 - Guess Helper
import random

def generate_secret():
    return random.randint(1, 20)

print("New secret:", generate_secret())
