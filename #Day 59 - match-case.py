#Day 59 - match-case 
def process_value(value):
    match value:
        case int(x) if x > 0:
            return f"Positive integer: {x}"
        case str(s) if len(s) > 3:
            return f"Long string: {s}"
        case [1, 2, *rest]:
            return f"List starts with 1,2: {rest}"
        case _:
            return "Unknown type"

print(process_value(42))
print(process_value("hello"))
print(process_value([1, 2, 3, 4]))