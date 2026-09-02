# Day 186 - Stack Helper

def check_brackets(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack


expressions = ["{[()]}", "{[(])}", "((()))"]

for expression in expressions:
    print(expression, "->", check_brackets(expression))