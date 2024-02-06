#!/usr/bin/python3
"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance
"""

balance = 0
initial_deposit = 1500
balance += initial_deposit

salary_credited = 3300

balance += salary_credited

online_perchases = 33.33

balance -= online_perchases

house_rent = 1500

balance -= house_rent

print("Final balance is:", balance)
print("house_rent:", house_rent)
print("online purchases:", online_perchases)
print("salary credited:", salary_credited)
print("Initial deposit:", initial_deposit)


