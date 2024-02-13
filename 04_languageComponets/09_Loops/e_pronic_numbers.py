#!python -u
"""
Purpose: Display the pronic numbers.

 Pronic number is a number which is the product
 of two consecutive integers.
 Some pronic numbers: 2*3 = 6

3  - 1 * 3
4  - 2 * 2
5  - 1 * 5
6  - 2 * 3  PRONIC
10 - 2 * 5

break
    - keyword
    - to stop the loop

NOTE:
else block of for loop will be executed, when all
iterations of for loop are completed
"""

print("Generating pronic numbers between values")

Min, Max = input("Enter the range of numbers to generate pronic numbers (separated by a space): ").split()
Min = int(Min)
Max = int(Max)

for num in range(Min, Max + 1):
    is_pronic = False
    for i in range(Min, int(num**0.5) + 1):
        if i * (i + 1) == num:
            is_pronic = True
            break
    
    if is_pronic:
        print(f"{num:2} - {i:2} * {i+1:2}")


