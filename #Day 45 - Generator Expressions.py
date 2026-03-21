#Day 45 - Generator Expressions
# Like list comp but memory efficient
squares = (x**2 for x in range(5))  # Note: ()
print("Squares:", list(squares))
