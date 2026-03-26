#Day 50 - Helper
from collections import Counter

text = "hello world"
letter_count = Counter(text)
print("Letters:", letter_count)
print("Top 3:", letter_count.most_common(3))
