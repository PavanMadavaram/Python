# Day 127 - library catalog
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    available: bool = True

books = [
    Book("Python Basics", "A. Rao"),
    Book("Data Structures", "M. Chen", False),
    Book("Algorithms", "S. Patel"),
]

for book in books:
    status = "Available" if book.available else "Checked out"
    print(f"{book.title} by {book.author} - {status}")