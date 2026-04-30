#Day 81 - Test
import csv
import io
output = io.StringIO()
writer = csv.writer(output)
writer.writerow(['test', 1])
print("CSV test:", 'test,1' in output.getvalue())
print("Day 81 test ok")