# Day 187 - Daily Temperatures
# DSA: Monotonic Stack

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # Stores indices with unresolved temperatures

    for current_day, current_temp in enumerate(temperatures):
        while stack and current_temp > temperatures[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = current_day - previous_day

        stack.append(current_day)

    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer = daily_temperatures(temperatures)

print("Temperatures:", temperatures)
print("Days until warmer temperature:", answer)