# Day 193 - Stack Using Two Queues
# DSA: Stack simulation with queues

from collections import deque

class StackWithQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, value):
        # Always push into q2, then move all from q1 to q2
        self.q2.append(value)
        while self.q1:
            self.q2.append(self.q1.popleft())
        # Swap references so q1 always holds stack order
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft() if self.q1 else None

    def top(self):
        return self.q1[0] if self.q1 else None

    def is_empty(self):
        return not self.q1


# Demo
s = StackWithQueues()
for v in [100, 200, 300]:
    s.push(v)
    print(f"Pushed {v}, top = {s.top()}")

print(f"Popped: {s.pop()}")
print(f"New top: {s.top()}")
print(f"Popped: {s.pop()}")
print(f"Empty? {s.is_empty()}")
