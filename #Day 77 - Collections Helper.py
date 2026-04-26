#Day 77 - Collections Helper
from collections import deque

# Deque
d = deque([1, 2, 3])
d.appendleft(0)
d.pop()
print("Deque:", list(d))