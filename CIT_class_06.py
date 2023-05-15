# Creative IT Class #06 Topic: Function Date: 12/04/2023

def a(s):
    print(s)
a('This is Aupu Chowdhury')

def add(a,b):
    print(a+b)
add(10,20)

def addd(a,b = 20):
    print(a+b)
addd(30)

def ad(a,b = 20):
    print(a+b)
ad(20, 80)

# calculator using function
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
num1 = float(input('insert num1: '))
num2 = float(input('insert num2: '))
operator = input('insert operator: ')

calculate(num1, num2, operator)
