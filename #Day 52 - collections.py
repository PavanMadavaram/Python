#Day 52 - collections.defaultdict 
from collections import defaultdict

# Default value for missing keys
dd = defaultdict(int)
dd['a'] += 1
dd['b'] += 2
print("Default dict:", dict(dd))