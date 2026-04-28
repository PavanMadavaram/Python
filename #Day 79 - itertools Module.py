#Day 79 - itertools Module 
import itertools

# Infinite counter
for num in itertools.count(10):
    print(num, end=' ')
    if num >= 15: break
print()

# Combinations
letters = 'ABC'
print("Combinations:", list(itertools.combinations(letters, 2)))