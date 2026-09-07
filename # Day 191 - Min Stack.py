# Day 191 - Min Stack
# DSA: Stack with constant-time minimum retrieval

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


# Demo
ms = MinStack()
for v in [3, 5, 2, 2, 7]:
    ms.push(v)
    print(f"Pushed {v}, min = {ms.get_min()}")

print(f"Top: {ms.top()}")
print(f"Popped: {ms.pop()}")
print(f"New min: {ms.get_min()}")