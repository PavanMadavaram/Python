# Day 189 - Stack Helper

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)

    for i, h in enumerate(heights):
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    heights.pop()
    return max_area


sample = [1, 2, 3, 4, 5]
print("Max area:", largest_rectangle_area(sample))