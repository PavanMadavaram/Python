# Day 192 - Queue Using Two Stacks
# DSA: Queue simulation with stacks

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

    def peek(self):
        self._shift()
        return self.outbox[-1] if self.outbox else None

    def is_empty(self):
        return not self.inbox and not self.outbox


# Demo
q = QueueWithStacks()
for v in [10, 20, 30]:
    q.enqueue(v)
    print(f"Enqueued {v}, front = {q.peek()}")

print(f"Dequeued: {q.dequeue()}")
print(f"New front: {q.peek()}")
print(f"Dequeued: {q.dequeue()}")
print(f"Empty? {q.is_empty()}")