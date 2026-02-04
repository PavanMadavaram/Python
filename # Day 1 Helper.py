# Day 1 Helper
def personal_info():
    return {
        "name": "Pavan",
        "age": 22,
        "city": "Hyderabad"
    }

def print_info(data):
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"City: {data['city']}")

if __name__ == "__main__":
    info = personal_info()
    print_info(info)
