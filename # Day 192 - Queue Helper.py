# Day 192 - Queue Helper

class QueueWithStacks:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, value):
        self.inbox.append(value)

    def _shift(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def dequeue(self):
        self._shift()
        return self.outbox.pop() if self.outbox else None


q = QueueWithStacks()
for v in [5, 15, 25]:
    q.enqueue(v)

print("Dequeued:", q.dequeue())
print("Dequeued:", q.dequeue())