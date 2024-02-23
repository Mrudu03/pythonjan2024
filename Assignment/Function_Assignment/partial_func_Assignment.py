"""
Assignments
------------
1) Develop a calculator software which does +, -, *, / operations
    Then, make use of partial functions to optimize your solution.
"""

import functools

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise print("Invalid, Cannot divide by zero.")
    
add_5 = functools.partial(add, 5)
subtract_10 = functools.partial(subtract, y=10)
multiply_by_3 = functools.partial(multiply, y=3)
divide_by_2 = functools.partial(divide, y=2)

assert add_5(7) == add(5, 7)
assert subtract_10(15) == subtract(15, 10)
assert multiply_by_3(8) == multiply(8, 3)
assert divide_by_2(20) == divide(20, 2)

print(f"Addition: {add_5(7)}")
print(f"Subtraction: {subtract_10(15)}")
print(f"Multiplication: {multiply_by_3(8)}")
print(f"Division: {divide_by_2(20)}")

