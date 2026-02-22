#Day 19 - Number Guessing
import random

secret = random.randint(1, 10)
guess = 7

if guess == secret:
    print("Correct!")
elif guess < secret:
    print("Too low!")
else:
    print("Too high!")
print("Secret was", secret)
