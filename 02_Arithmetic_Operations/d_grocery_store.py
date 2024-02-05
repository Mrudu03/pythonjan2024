#!/usr/bin/python3
"""
Purpose: Grocery Store

    Item       cost
    ------------------------
    rice        10/kg
    wheat       34/kg

Algorithm
----------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items from the user(in run time)

NOTE: input()
        -> to get value in run-time
        -> will give any input as string only, to avoid injection attacks
"""
# cost of items
cost_of_rice = 10  # per kg
cost_of_wheat = 34  # per kg


# Quantities of Items
qty_of_rice = input("Enter Qty. of Rice  (in Kgs):")
qty_of_rice = int(qty_of_rice)
print("Qty of Rice  :", qty_of_rice, type(qty_of_rice))

"""
Enter Qty. of Rice  (in Kgs):3
Qty of Rice  : 3 <class 'str'>
@priyanka3prakash ➜ /workspaces/pythonJan2024/02_Arithmetic_Operations (class06) $ python d_grocery_store.py 
Enter Qty. of Rice  (in Kgs):2.3
Qty of Rice  : 2.3 <class 'str'>
@priyanka3prakash ➜ /workspaces/pythonJan2024/02_Arithmetic_Operations (class06) $ python d_gr
ocery_store.py 
Enter Qty. of Rice  (in Kgs):True
Qty of Rice  : True <class 'str'>
@priyanka3prakash ➜ /workspaces/pythonJan2024/02_Arithmetic_Operations (class06) $ python d_gr
ocery_store.py 
Enter Qty. of Rice  (in Kgs):32434234
Qty of Rice  : 32434234 <class 'str'>
@priyanka3prakash ➜ /workspaces/pythonJan2024/02_Arithmetic_Operations (class06) $ python d_gr
ocery_store.py 
Enter Qty. of Rice  (in Kgs):None
Qty of Rice  : None <class 'str'>
@priyanka3prakash ➜ /workspaces/pythonJan2024/02_Arithmetic_Operations (class06) $ 

"""

