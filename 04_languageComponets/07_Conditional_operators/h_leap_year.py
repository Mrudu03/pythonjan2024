#!/usr/bin/python3
"""
Purpose: Leap Year Checks

Algorithms
-----------
    if (year is not divisible by 4) then (it is a common year)
    else if (year is not divisible by 100) then (it is a leap year)
    else if (year is not divisible by 400) then (it is a common year)
    else (it is a leap year)

    Compute the leap years in this century
"""

y = int(input("please enter a year "))
if y % 4 != 0:
    print(f"This is not leap year: {y}")
elif y % 100 != 0:
    print(f"This is a leap year {y}")
elif y % 400 !=0:
    print(f"This is not a leap year: {y}")
else:
    print(f"This is a leap year {y}")
