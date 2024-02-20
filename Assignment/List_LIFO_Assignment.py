"""
Assignment
----------
1) implement the stack mechanism - LIFO
Take the values in run time
   1. push   - add an element
   2. pop    - delete last element
   3. status - stack size

-       -
|       |
|       |
---------
HINT: list.pop(), list.append(), len()

2) implement the queue mechanism - FIFO
Take the values in run time
   1. push   - add an element
   2. pop    - delete last element
   3. status - queue size
    --------
 ->         ->
    --------
HINT: list.insert(), list.pop(), len()
"""


mylist = []

while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Status")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        value = input("enter the value into the list: ")
        mylist.append(value)
        print(f"{value} pushed to the stack.")
    
    elif choice == '2':
         if mylist:
            popped_item = mylist.pop()
            print(f"{popped_item} popped from the stack.")
         else:
             print("Stack is empty. Cannot pop.")
    
    elif choice == '3':
         if mylist:
            print(f"Stack size: {len(mylist)}")
            print("Stack elements:", mylist)
         else:
             print("Stack is empty.")

    elif choice == '4':
         print("Exiting the stack program.")
         print("Your stack is : ", mylist)
         break
    
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

        