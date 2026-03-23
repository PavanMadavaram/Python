#Day 47 - args & kwargs
def sum_all(*args):
    return sum(args)

print("Sum:", sum_all(1, 2, 3, 4, 5))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Sai", age=23, city="Hyderabad")
