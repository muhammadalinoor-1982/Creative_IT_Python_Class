# Create a Simple Calculator using Nested If
operation = int(input("Enter your operations Value:[1 to 4]"))
First_Value = float(input('Enter First Value: '))
Second_Value = float(input('Enter Second Value: '))

if operation == 1:
    calculate = First_Value + Second_Value
    print("Result = ", calculate)

elif operation == 2:
    calculate = First_Value - Second_Value
    print("Result = ", calculate)

elif operation == 3:
    calculate = First_Value * Second_Value
    print("Result = ", calculate)

elif operation == 4: # To get quotient with decimal value
    calculate = First_Value / Second_Value
    print("Result = ", calculate)

elif operation == 5:
    exit()
else:
    print("Wrong input..!!")
    