#Day 103 - Decimal Helper
from decimal import Decimal, ROUND_HALF_UP

price = Decimal("19.995")
tax = Decimal("0.18")

total = price * (1 + tax)
rounded = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print("Total:", total)
print("Rounded:", rounded)