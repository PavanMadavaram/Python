#Day 53 - collections.deque 
from collections import deque

# Fast append/pop from both ends
d = deque([1, 2, 3])
d.appendleft(0)
d.pop()
print("Deque:", list(d))