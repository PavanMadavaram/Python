#Day 101 - statistics Module 
import statistics as stats

numbers = [10, 20, 20, 30, 40, 40, 40, 50]

print("Mean:", stats.mean(numbers))
print("Median:", stats.median(numbers))
print("Mode:", stats.mode(numbers))
print("Stdev:", round(stats.stdev(numbers), 2))