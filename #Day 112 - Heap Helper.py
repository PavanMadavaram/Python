#Day 112 - Heap Helper
import heapq

scores = [40, 80, 60, 90, 70]
top3 = heapq.nlargest(3, scores)

print("Top 3 scores:", top3)
print("Smallest 2:", heapq.nsmallest(2, scores))