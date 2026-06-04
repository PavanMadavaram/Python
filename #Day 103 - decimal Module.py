#Day 103 - decimal Module 
from decimal import Decimal, getcontext

getcontext().prec = 6

a = Decimal("1.1")
b = Decimal("2.2")
c = Decimal("3.3")

print("A + B:", a + b)
print("B + C:", b + c)
print("Exact sum:", Decimal("0.1") + Decimal("0.2"))