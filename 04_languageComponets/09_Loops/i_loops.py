#!/usr/bin/python3
"""
Purpose: Loops
    break     - breaks the complete loop
    continue  - skip the current loop
    pass      - will do nothing. it is like a todo
    sys.exit  - will exit the script execution

"""

i = 0
while i <= 7:
    i += 1
    print(i, end=", ")

print()
print("\n importance of break")
i = 0
while i <= 7:
    i += 1
    if i %2 == 0:
        break
    print(i, end=", ")

print()
print("\n importance of continue")
i = 0
while i <= 7:
    i += 1
    if i %2 == 0:
        continue
    print(i, end=", ")


print("\n importance of pass")
i = 0
while i <= 7:
    i += 1
    if i % 2 == 0:
        pass  # It acts as a placeholder
    #pass is used for a place holder where some logic needs to be added
    #or TBD code we write pass as a dummy code
    print(i, end=", ")


class MyClass:
    pass #TBD


def myfunc():
    pass #TBD

# ======================================
import sys 
print("\nimportance of sys.exit")
i = 0
while i < 7:
    i += 1
    if i % 2 == 0:
        sys.exit(0)
    print(i, end=", ")


# exit code 0 - successful/normal termination
# exit code non-zero - abnormal termination
print("next statement")