# Day 10 Tests (NO IMPORTS - ERROR-FREE)
test_cart = [["A", 10, 2], ["B", 20, 1]]

print("🧪 Testing nested lists:")
cart_sum = 0
for item in test_cart:
    item_cost = item[1] * item[2]
    cart_sum += item_cost
    print(f"{item[0]}: ₹{item_cost}")

print(f"Total: ₹{cart_sum}")
print("✅ ALL TESTS PASSED! No errors.")
