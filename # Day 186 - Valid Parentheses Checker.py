# Day 186 - Valid Parentheses Checker
# DSA: Stack

def is_valid_parentheses(text: str) -> bool:
    matching = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
 
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in matching:
            if not stack or stack.pop() != matching[char]: 
                return False
 
    return len(stack) == 0 

 
samples = ["()", "()[]{}", "(]", "([{}])", "((())"] 

for sample in samples:
    result = "✅ Valid" if is_valid_parentheses(sample) else "❌ Invalid"
    print(f"{sample}: {result}")
