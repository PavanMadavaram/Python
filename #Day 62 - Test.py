#Day 62 - Test
import csv
import io

test_data = io.StringIO("test,1\n")
reader = csv.reader(test_data)
print("CSV test:", list(reader))
print("Day 62 test ok")