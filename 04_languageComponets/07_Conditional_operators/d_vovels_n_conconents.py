#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithms:
-------
step1 : take input in runtime
            clean -- strip()
Step2:  len(character) should not be greater than 1
step3: isalpha()
step4 : is it vowel or not

NOTE: logic should accomodate both upper and lower characters
"""
vovels = ['a','e','i','o','u']
letter = input("Enter a charecter to check : ").strip()

if len(letter) > 1:
    print("Please enter a single charecter")
else:
    if letter.isalpha():
        letter = letter.lower()
        if letter in vovels:
            print(f"{letter}: is a Vovel")
        else:
            print(f"{letter}: is a Consonent")
    else:
        print("Please enter a letter")


