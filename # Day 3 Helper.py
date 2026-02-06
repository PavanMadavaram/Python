# Day 3 Helper
def is_even(num):
    return num % 2 == 0

def check_number(num):
    if is_even(num):
        return "EVEN"
    return "ODD"

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(f"{n} is {check_number(n)}")
