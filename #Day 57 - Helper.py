#Day 57 - Helper
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    stock: int

phone = Product("iPhone", 80000, 10)
print(phone)