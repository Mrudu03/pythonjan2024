mylist1 = [1, 11, 111, [11]]
print("mylist1       = ", mylist1)

mylist2 = [2, 22, 222]
print("mylist2       = ", mylist2)
print()


# list concatenation
newlist = mylist1 + mylist2
print("newlist       = ", newlist)
print("type(newlist) = ", type(newlist))
print()


print("commutative prop :", mylist1 + mylist2 == mylist2 + mylist1)
print("mylist1 + mylist2", mylist1 + mylist2)
print("mylist2 + mylist1", mylist2 + mylist1)


# Assignment: List repetition is commutative
print("To check if the list repitative is commutative")
mulList = mylist1 * 2
print("Multiplied list       = ", mulList)
print("type(mulList) = ", type(mulList))
print()