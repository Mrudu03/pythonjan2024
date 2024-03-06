"""
exercises on recursions:
--------------------------
1. Write a recursive function to reverse a list
        input:  [1, 2, 3, 3, 4, 5]
        output: [5, 4, 3, 3, 2, 1]
    Methods: recursions, reversed(), values[::-1]
2. Write a recursive function to compute the fibonacci series
        0, 1, 1, 2, 3, 5, 8, ....
        HINT: unpacking
"""
def reverse_list(lst):
    if not lst:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

input_list = [1, 2, 3, 3, 4, 5]
output_list = reverse_list(input_list)
print(f"Input List: {input_list}")
print(f"Reversed List: {output_list}")

print("Fibonacci series")
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = fibonacci(n - 1)
        return fib_series + [fib_series[-2] + fib_series[-1]]

fibonacci_count = 10
fib_series = fibonacci(fibonacci_count)
print(f"Fibonacci Series (up to {fibonacci_count} terms): {fib_series}")
