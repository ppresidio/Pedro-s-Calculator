"""
    Name: calculator.py
    Author: Pedro Paulo de Jesus Presidio
    Created: 4.4.2024
    Purpose: A utilty module with commonly used functions
"""

import utils

#create the menu for the user
print(utils.title("Pedro best Calculator program"))
print(utils.title("Select operation:"))
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#method for adding
def add(x, y):
    return x + y

#method for subtraction
def subtract(x, y):
    return x - y

#method for multiplciation
def multiply(x, y):
    return x * y

#method for division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

#loop to receive number, and check user choice
while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))

        elif choice == '2':
            print("Result:", subtract(num1, num2))

        elif choice == '3':
            print("Result:", multiply(num1, num2))

        elif choice == '4':
            print("Result:", divide(num1, num2))
        
        break
    else:
        print("Invalid input")
