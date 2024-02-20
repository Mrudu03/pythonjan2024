# assignment - apply enumerate function on each of these

person_details = {
    "name": "Narendra Modi",
    "age": 67,
    "salary": 2_00_000,
    "role": "CM of Gujarat",
    "role": "PM of India",  # latest will be stored

}
print(person_details)

print("\n Iterating over the dictionary using enumerate ")

for index, each in enumerate(person_details):
    print(each)
    print(f"Index: {index}, Item : {each}")
    
print("\n person_details.keys()")
for index, each in enumerate(person_details.keys()):
    print(f"Index: {index}, Key : {each}")

print("\n person_details.values()")
for index, each in enumerate(person_details.values()):
    print(f"Index: {index}, Values : {each}")


print("\n person_details.items()")
for index, each in enumerate(person_details.items()):
    print(f"Index: {index}, Items : {each}")

print("\n person_details.items()")
for index, (each_key, each_value) in enumerate(person_details.items()):
    print(f"Index : {index} item :  {each_key}\t{each_value}")

