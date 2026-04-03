#Day 58 - Helper
data = [10, 20, 30]
if (total := sum(data)) > 50:
    print("Total is large:", total)

# List comp with walrus
matched = [x for x in range(10) if (y := x * 2) > 10]
print("Matched:", matched)
