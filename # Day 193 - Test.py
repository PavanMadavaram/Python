# Day 193 - Test

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

    def top(self):
        return self.q1[0] if self.q1 else None


s = StackWithQueues()
s.push(1)
s.push(2)
s.push(3)

assert s.top() == 3
assert s.pop() == 3
assert s.pop() == 2
s.push(4)
assert s.pop() == 4
assert s.pop() == 1

print("Day 193 test ok")
