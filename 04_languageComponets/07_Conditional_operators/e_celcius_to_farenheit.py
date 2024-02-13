#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit


farhenheit = (1.8 * celsius) + 32  # PEMDAS

Algorithm:
step 1: take celcius , clear and validate 
step 2: convert and give farhenheit
"""
tempC = float(input("Enter a temperature in celcius: ").strip())

farenheit = (1.8 * tempC) + 32

print(f"The {tempC}C when converted to farenheit is {farenheit}F")



