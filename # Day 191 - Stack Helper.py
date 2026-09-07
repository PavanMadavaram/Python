# Day 191 - Stack Helper

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

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


ms = MinStack()
for v in [10, 3, 7, 1]:
    ms.push(v)

print("Current min:", ms.get_min())
print("Popped:", ms.pop())
print("New min:", ms.get_min())