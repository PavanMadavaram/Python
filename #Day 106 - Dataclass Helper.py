#Day 106 - Dataclass Helper
from dataclasses import dataclass, asdict

@dataclass
class Product:
    name: str
    price: float
    stock: int = 0

p = Product("Notebook", 49.99, 12)
print(asdict(p))