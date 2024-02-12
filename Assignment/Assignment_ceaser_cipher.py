# Assignment
# -------------
# caesar cipher
# ------------------  + 3
# A B C D E F G H I J     Y Z
# 0 1 2 3 4 5 6 7
# D E F


# Ex: egg => hjj
#    bindu => elqg
#    Yash  => bd..

# ASSUMPTION: Ignore case -sensitivity
# HINTS: ord(), chr(), %


input_str = input("Enter the string: ").lower()  # Make sure to call lower() to convert the input to lowercase
shift = int(input("Enter the character shift (as an integer): "))  # Convert the shift to an integer

new_str = ""
for char in input_str:
    if char.isalpha():  # Check if the character is alphabetic
        ascii_code = ord(char)
        new_code = ascii_code + shift
        new_letter = chr(new_code)

        new_str += new_letter
    else:
        new_str += char  # If the character is not alphabetic, keep it unchanged

print("The original string is:", input_str)
print("The new converted string is:", new_str)