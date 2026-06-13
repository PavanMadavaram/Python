#Day 111 - bisect Module 
import bisect

scores = [45, 50, 60, 70, 85]

# Insert while keeping sorted order
bisect.insort(scores, 65)
bisect.insort(scores, 90)

print("Sorted scores:", scores)
print("Position for 68:", bisect.bisect(scores, 68))