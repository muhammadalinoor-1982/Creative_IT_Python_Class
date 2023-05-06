""" 1. Suppose you are building a simple calculator program in Python that takes two input
numbers from the user and performs addition, subtraction, multiplication, or division
based on the user's choice. However, the user inputs are being received as strings, 
so you need to convert them to the appropriate numeric data type before performing 
any calculations.

Write a Python program that does the following:

Takes two input numbers (as strings) from the user.
Prompts the user to select an operation (+, -, *, /).
Converts the input numbers to the appropriate data type (int or float) using type casting.
Performs the selected operation on the input numbers.
Prints the result of the operation.

Enter the first number: 3
Enter the second number: 4.5
Select an operation (+, -, *, /): *
The result is: 13.5 """

# Answer:
numOne = str(input('Enter the first number: '))
numTwo = str(input('Enter the second number: '))
operator = input('Select an operation (+, -, *, /): ')

num1 = float(numOne)
num2 = float(numTwo)

def calculate(num1, num2, operator):
    if operator == '+':
        addition = num1 + num2
        print('Result of addition is: ', addition)
    elif operator == '-':
        substruction = num1 - num2
        print('Result of substruction is: ', substruction)
    elif operator == '*':
        multiplication = num1 * num2
        print('Result of multiplication is: ', multiplication)
    elif operator == '/':
        divition = num1 / num2
        print('Result of divition is: ', divition)
    else:
        print('invalid input')

calculate(num1, num2, operator)
# _______________________________________________________________________

""" 2.Suppose you are building a program that calculates the total cost of an online shopping cart, including tax 
and shipping charges. The program should ask the user for the total cost of the items in the cart, and then calculate
 the tax and shipping charges based on the following rules:

If the total cost is less than $50, there is no tax and the shipping charge is $5.
If the total cost is between $50 and $100, the tax is 10% of the total cost and the shipping charge is $10.
If the total cost is greater than $100, the tax is 15% of the total cost and the shipping charge is free.
Write a Python program that does the following:

Prompts the user for the total cost of the items in the shopping cart.
Calculates the tax and shipping charges based on the rules above using if-else statements.
Calculates the total cost including tax and shipping.
Prints the total cost including tax and shipping.
Here's an example of what the program output might look like:

Enter the total cost of the items in your shopping cart: 75.50
Your tax is $7.55 and your shipping charge is $10.00.
Your total cost including tax and shipping is $93.05. """

# Answer:
cost = float(input("Enter the total cost of the items in your shopping cart: "))
if cost < 50:
    tax = 0
    shipping_charge = 5
# elif cost < 100:
elif cost >= 50 and cost <= 100:
    tax = 10
    # tax = cost * 0.1
    shipping_charge = 10
else:
    # tax = cost * 0.15
    tax = 15
    shipping_charge = 0
print('Your tax is $', tax, ' and your shipping charge is $', shipping_charge)
total = cost + tax + shipping_charge
print("Your total cost including tax and shipping is $", total)
# _______________________________________________________________________________

""" 3.Suppose you are building a program that calculates the average of a list of numbers. The program should ask the 
user for the number of items in the list, and then prompt the user to enter each item in the list. Once all of the items 
have been entered, the program should calculate the average of the list using a for loop.

Write a Python program that does the following:

Prompts the user for the number of items in the list.
Uses a for loop to prompt the user to enter each item in the list.
Calculates the average of the list using a for loop.
Prints the average of the list.
Here's an example of what the program output might look like:

How many items are in the list? 5
Enter item 1: 10
Enter item 2: 15
Enter item 3: 20
Enter item 4: 25
Enter item 5: 30
The average of the list is 20.0. """

# Answer:
items = int(input("How many items are in the list? "))
numbers = []
for i in range(items):
    number = float(input("Enter item {}: ".format(i+1)))
    numbers.append(number)
sum = 0
for number in numbers:
    sum += number
average = sum / len(numbers)
print("The average of the list is:", average)
# ________________________________________________________________

""" 4.Suppose you are building a program that calculates the area and perimeter of a rectangle. The program should ask the user 
for the length and width of the rectangle, and then calculate and print the area and perimeter using two separate functions.

Write a Python program that does the following:

Defines a function named calculate_area that takes the length and width of a rectangle as parameters and returns the area of the rectangle.
Defines a function named calculate_perimeter that takes the length and width of a rectangle as parameters and returns the perimeter of 
the rectangle.
Prompts the user for the length and width of the rectangle.
Calls the calculate_area function with the user's input and prints the result.
Calls the calculate_perimeter function with the user's input and prints the result.
Here's an example of what the program output might look like:

Enter the length of the rectangle: 5
Enter the width of the rectangle: 10
The area of the rectangle is 50.
The perimeter of the rectangle is 30.
 """

# Answer:
def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print('The area of the rectangle is',area)
print('The perimeter of the rectangle is ',perimeter)
# _______________________________________________________________________


