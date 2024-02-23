"""
Assignment: mimick sum() builtin function with
 a. user-defined function
 b. using reduce
"""

from functools import reduce

def user_sum(list1):
    result = 0
    for element in list1:
        result += element
    return result


result = user_sum([10, 20, 30])
print(f"result: {result}")


#using reduce

result_reduce = reduce(lambda x, y: x + y, [10, 20, 30])
print(f"result_reduce: {result_reduce}")