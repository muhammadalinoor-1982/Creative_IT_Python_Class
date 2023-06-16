# Create a python file. Name like "my_function.py"
# Create a function in the "my_function.py". Example Below:

'''
n = int(input("Enter Value N: "))
m = int(input("Enter Value M: "))

def sum():
    p = n + m
    print("Sum value is: "
'''
# Save this file in the "Lib" folder of python base application folder
# Import This "my_function.py" in another python file like "function_test.py"
# Aliase the "my_function.py" file rename in the "function_test.py" Example Below:

# In the function_test.py
'''
import my_function as s           # Here "s" is a new name of "my_function"
'''

# Call the function from "my_function.py" of "sum()" in the "function_test.py" Example Below:

# In the "function_test.py"
'''
import my_function as s
s.sum()
'''

# _______________________________________________________________________________________________