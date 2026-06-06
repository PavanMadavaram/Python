#Day 105 - Enum Helper
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"

print("Status:", Status.RUNNING)
print("Value:", Status.RUNNING.value)