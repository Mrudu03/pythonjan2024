'''
Assignment: Generate even numbers between 45 & 137
# loop values between limits, test eveness for each number
# and display, if it is even

# TIP - range, if condition within it, print function
'''
values = range(45,137,1)
list1 = []

for n in values:
    if n % 2 == 0:
        list1.append(n)
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

print(f"{list1} are the list of even numbers")


        
