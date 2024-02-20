# Assignment
# 1. Prove that tuple concatenation is not commutative: t1 + t2 != t2 + t1
# 2. Prove that tuple repetition is commutative       : t1 * 3 == 3 * t1

print("Checking if tupple concatenation is commutative or not: ")

tup1 = (2,7)
tup2 = (3,6)

print(f"tuple 1 is: {tup1}")
print(f"tuple 2 is: {tup2}")

# tupple concatenation
newtup = tup1 + tup2
print("newtup       = ", newtup)
print("type(newtuple) = ", type(newtup))
print()

print("commutative prop :", tup1 + tup2 == tup2 + tup1)
print("tup1 + tup2", tup1 + tup2)
print("tup2 + tup1", tup2 + tup1)

# tupple multiplication
tupmul = tup1 * 6
print("tupmul       = ", tupmul)
print("type(tupmul) = ", type(tupmul))
print()

print("commutative prop :", tup1 * 6 == 6 * tup1)
print("tup1 * 6", tup1 * 6)
print("6 * tup1", 6 * tup1)


