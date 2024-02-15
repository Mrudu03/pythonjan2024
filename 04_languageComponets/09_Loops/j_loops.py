#!/usr/bin/python
"""
Purpose:
    break     - breaks the complete loop
	continue  - skip the current loop
	pass      - will do nothing. it is like a todo
	sys.exit  - will exit the script execution
"""

import sys


students = ["akram", "trusha", "bhavana", "jaya", "chaitra"]
roll =  range(70, 80, 1)

# assignment - try the same using for loop

print("Using for loop for break")
class1 = []
for s in students:
    if s == "jaya":
        break
    else:
        class1.append(s)

print(f"The new class is : {class1}") #The new class is : ['akram', 'trusha', 'bhavana']

print()
print("Using for loop for continue")
class1 = []
for s in students:
    if s == "jaya":
        continue
    else:
        class1.append(s)
print(f"The new class is : {class1}")

print()
roll1 =[]
print("Using for loop for pass")
for i in roll:
    if i % 2 == 0:
        roll1.append(i)
    else:
        pass
print(f"The even numbers are :  {roll1}")
        
print()
print("Using for loop for sys.exit(0)")


roll1 =[]
for i in roll:
    if i % 2 == 0:
        sys.exit(0)
    else:
        roll1.append(i)
print(f"The even numbers are :  {roll1}")