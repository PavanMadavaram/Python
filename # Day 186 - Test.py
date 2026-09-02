# Day 186 - Test

def is_valid_parentheses(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack


tests = {
    "()[]{}": True,
    "([{}])": True,
    "(]": False,
    "(((": False,
    "": True,
}

for expression, expected in tests.items():
    assert is_valid_parentheses(expression) == expected

print("Day 186 test ok")