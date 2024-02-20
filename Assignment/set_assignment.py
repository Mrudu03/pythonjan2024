# Assignment
#  1. Try adding a string to both set.add & set.update &
#  observe the difference
#  'tomoto'

myset = {1,2,6,8,(8,9),7}

print(f"My sets is: {myset}")

# Using set.add

myset.add("tomoto")

print(f"My sets after using myset.add: {myset}")

#using set.update

myset.update("tomoto")

print(f"My sets after using myset.update: {myset}")