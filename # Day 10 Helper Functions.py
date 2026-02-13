# Day 10 Helper (ERROR-FREE)
def cart_total(cart):
    total = 0
    for item in cart:
        total += item[1] * item[2]
    return total

def show_cart(cart):
    print("\n📦 Your Cart:")
    for item in cart:
        print(f"  {item[0]}: ₹{item[1]} × {item[2]}")

# Hyderabad Grocery Demo
grocery = [["Rice", 80, 5], ["Dal", 120, 2]]
show_cart(grocery)
print(f"Bill: ₹{cart_total(grocery)}")
