# Program make a simple calculator
# importing datetime
from datetime import datetime

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers1

def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

import csv

with open('data.csv', mode='w') as data:
    data_writer = csv.writer(data, delimiter=',', quotechar='"')
    data_writer.writerow(["First Number", "Sign", "Second Number", "" , "result","Date and Time"])

while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4/5): ")

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))


            if choice == '1':
                result = add(num1, num2)
                choice = "+"

            elif choice == '2':
                result = subtract(num1,num2)
                choice = "-"

            elif choice == '3':
                result = multiply(num1,num2)
                choice = "x"

            elif choice == '4':
                result = divide(num1, num2)
                choice = "/"

            print(num1, choice, num2, "=", result)

            y = f'{datetime.now():%Y-%m-%d %H:%M:%S%z}'

            # importing data.csv file
            import csv

            with open('data.csv', mode='a') as data:
                data_writer = csv.writer(data, delimiter=',', quotechar='"')
                data_writer.writerow([num1, choice, num2,"=", result, y])

        elif choice == '5':
            break


else:
            print("invalid number")
        # write num1, num2, choice, current date time to the csv file

