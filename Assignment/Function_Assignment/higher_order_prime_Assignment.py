"""
Assignment:
----------
1) Try to get the prime numbers between 1208 and 4893
    HINTS: used-defined function to check primeness of a number
           filter()
"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Method 1: Using a loop and is_prime function
prime_numbers = []
for num in range(1208, 4894):
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)
