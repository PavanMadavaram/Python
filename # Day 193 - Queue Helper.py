# Day 193 - Queue Helper

from collections import deque

class StackWithQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, value):
        self.q2.append(value)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft() if self.q1 else None


s = StackWithQueues()
for v in [5, 15, 25]:
    s.push(v)

print("Popped:", s.pop())
print("Popped:", s.pop())