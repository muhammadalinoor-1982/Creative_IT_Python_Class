# pactice function

# Creating a Function
# In Python a function is defined using the def keyword
# Calling a Function
print('Calling a Function:')
def test():
    print('my name is aupu')
test()
print('\n')

# Calling a Function using arguments
print('Calling a Function using arguments:')
def args(money):
    print(money + 'how much many')
args('text ')
args('apple ')
args('coin ')
args('money ')
print('\n')

# Calling a Function using multiple arguments
print('Calling a Function using multiple arguments')
def mularg(male, female):
    print(male + ' ' + female)
mularg('aupu','aunu')
print('\n')

# Arbitrary Arguments, *args
# If the number of arguments is unknown, add a * before the parameter name:
print('Arbitary Arguments')
def arbt(*tab):
    print('somany tabs are here: ' + tab[2])  #which tab you want to print
arbt('root', 'main', 'sub')
print('\n')

# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
print('Arguments with the key = value syntax: ')
def argk(one, two, three):
    print('print the specific value: ' + two)
argk(one = 'ek', two = 'dui', three = 'tin')
print('\n')

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
print('Arbitrary Keyword Arguments, **kwargs: ')
def kwarbt(**candidate):
    print('candidate are: ' + candidate['cand_2'])
kwarbt(cand_1 = 'raja', cand_2 = 'rani')
print('\n')

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
print('Default Parameter Value: ')
def defparam(country = 'Bangladesh'):
    print('i am from ' + country)
defparam('india')
defparam()
defparam('feni')
print('\n')

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
print('Passing a List as an Argument: ')
def passlistarg(newmerica):
    for x in newmerica:
        print(x)
num = ['one', 'two', 'three']
passlistarg(num)
print('\n')

# Return Values
# To let a function return a value, use the return statement:
print('Return Values: ')
def revlu(x):
    return 10 * x
print(revlu(3))
print(revlu(2))
print(revlu(7))
print('\n')

# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
print('The pass Statement: ')
def passt():
    pass
print('\n')

# tri_recursion() 
print('Tri Recursion: ')
def tri_recursion(a):
    if(a > 0):
        result = a + tri_recursion(a - 1)
        print(result)
    else:
        result = 0
    return result
print('\n \n Recursion example Result: ')
tri_recursion(7)
print('\n')



    
