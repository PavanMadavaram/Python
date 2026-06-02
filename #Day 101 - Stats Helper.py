#Day 101 - Stats Helper
import statistics as stats

data = [2, 4, 6, 8, 10]
print("Population variance:", stats.pvariance(data))
print("Population stdev:", round(stats.pstdev(data), 2))