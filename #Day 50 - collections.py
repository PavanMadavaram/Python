#Day 50 - collections.Counter 
from collections import Counter

grades = ['A', 'B', 'A', 'C', 'B', 'A']
count = Counter(grades)
print("Grade counts:", count)
print("Most common:", count.most_common(2))
