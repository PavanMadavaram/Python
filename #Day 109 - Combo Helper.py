#Day 109 - Combo Helper
import itertools

items = ["A", "B", "C"]
print("Permutations:", list(itertools.permutations(items)))
print("Product:", list(itertools.product(items, repeat=2)))