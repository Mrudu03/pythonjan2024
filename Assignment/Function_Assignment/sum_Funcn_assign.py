"""
Assignment
----------
1) write a function to mimick the sum() function.
    Caution: don't create function with same name

2) write a function to implement the following:
    - input: ((1,2), 3,4, [5, 6])
    - output: (1, 2, 3, 4, 5, 6)

    HINT: isinstance() - builtin function
          int(), float(), list(), tuple(), set()
          list.append(), list.extend
          list & tuple concatenation
"""
# print(f'type(int) is type(123)  :{type(int) is type(123)}')
print(f"isinstance(123, int)    :{isinstance(123, int)}")

print(f"isinstance(10.3, int)   :{isinstance(10.3, int)}")
print(f"isinstance(10.3, float) :{isinstance(10.3, float)}")

#write a function to mimick the sum() function.
  #  Caution: don't create function with same name

def check_sum(i):
    result = 0
    for element in i:
        result += element
    return result



result = check_sum([10, 20, 30])
print(f"result: {result}")

#write a function to implement the following:
 #   - input: ((1,2), 3,4, [5, 6])
  #  - output: (1, 2, 3, 4, 5, 6)

def tuple_elemnts(data):
    arr_data = []
    for item in data:
        if isinstance(item, (list, tuple)):
            arr_data.extend(tuple_elemnts(item))
        else:
            arr_data.append(item)
    return arr_data


input_data = ((1, 2), 3, 4, [5, 6])
output_data = tuple(tuple_elemnts(input_data))
print(f"output_data: {output_data}")