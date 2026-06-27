# Day 124 - contact book
from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    phone: str
    email: str

contacts = [
    Contact("Asha", "111-222", "asha@example.com"),
    Contact("Ravi", "333-444", "ravi@example.com"),
    Contact("Mina", "555-666", "mina@example.com"),
]

for c in contacts:
    print(f"{c.name} | {c.phone} | {c.email}")