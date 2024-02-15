#!/usr/bin/python
"""
Purpose: Calculating the average for the
    inputted numbers in run-time
"""

result = eval("1") #eval evaluates the results
print(f"{result =} {type(result)}")  # int


result = eval("123.23")
print(f"{result =} {type(result)}")  # float
#to evaluate something in run time we use eval
#the system automatically evaluates
# result = eval("123 23")
# SyntaxError: invalid syntax

result = eval("12 + 23/32 * 23")
print(f"{result =} {type(result)}")  # float
#eval also evaluates and takes in an expression
# result = eval('Apple')
# NameError: name 'Apple' is not defined. Did you mean: 'tuple'?

# result = eval("Apple")
# NameError: name 'Apple' is not defined. Did you mean: 'tuple'?

result = eval('"Apple"')
print(f"{result =} {type(result)}")  # str
# in order to evaluate a string we use quotes inside the single quotes
result = eval("'Apple'")
print(f"{result =} {type(result)}")  # str

Mango = 12
result = eval('Mango')
print(f"{result =} {type(result)}")  # int

result = eval("Mango")
print(f"{result =} {type(result)}")  # int


Apple = 12132
result = eval("Apple")
print(f"{result =} {type(result)}")  # int


# Assignment - calculate the avergae of numbers provided in runtime
# HINTS - while , input(), eval(), len(), sum()


numlist = []

while True:
    # Take input from the user
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input == "done":
        break
    elif user_input.isnumeric():
        number = eval(user_input)
        numlist.append(number)
    else:
        print("please enter a number")

numlen = len(numlist)
avg = round(sum(numlist)/numlen)
print(f"The list of nums is : {numlist}, and the avg of the numbers entered is : {avg}")









