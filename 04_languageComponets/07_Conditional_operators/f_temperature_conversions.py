#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
default should be celcius

HINTS: .strip(), indexing to get to know celecium or farhentient, 
    extract the temprature, adn then convert 
"""

temp = input("Enter the temperature in celcius or Farenheit: ").strip()
if temp[-1].lower() == 'c':
    tempC = float(temp[:-1])
    tempF = round((1.8 * tempC) + 32, 2)
    print(f"The temperature converted from {tempC}C to farenheit is {tempF}F")
elif temp[-1].lower() == 'f':
    tempF = float(temp[:-1])
    tempC = round(((tempF - 32)/1.8), 2)
    print(f"The temperature converted from {tempF}F to celcius is {tempC}C")


