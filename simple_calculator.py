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

# This function divides two numbers
def divide(x, y):
    return x / y

# Test whether input is a valid num
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")

import csv

# with open('data.csv', mode='w') as data:
#     data_writer = csv.writer(data, delimiter=',', quotechar='"')
#     data_writer.writerow(["First Number", "Sign", "Second Number", "result","Date and Time"])

while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4/5): ")
        
        # Check if choice is one of the four options
        if (choice == '1' or choice == '2' or choice == '3' or choice == '4'):
            print("check")
            while True: 
                num1 = input("Enter first number: ")
                if (isfloat(num1)):
                    num1 = float(num1)
                    break
                else:
                    print("Invalid input! Input must be a valid number!")
                    
            while True:
                num2 = input("Enter second number: ")
                if (isfloat(num2)):
                    num2 = float(num2)
                    break
                else:
                    print("Invalid input! Input must be a valid number!")


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
                data_writer.writerow([str(num1)+" "+choice+" "+str(num2)+" ""="+" "+str(result), y])

        elif choice == '5':
            print("exited")
            break
    
        else:
            print("Please select 1 of the 5 given options!")
        # write num1, num2, choice, current date time to the csv file

