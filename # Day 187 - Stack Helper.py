# Day 187 - Stack Helper

def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for index, temperature in enumerate(temperatures):
        while stack and temperature > temperatures[stack[-1]]:
            previous_index = stack.pop()
            result[previous_index] = index - previous_index

        stack.append(index)

    return result


sample = [30, 40, 50, 60]
print("Result:", daily_temperatures(sample))