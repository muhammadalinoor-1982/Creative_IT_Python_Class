#Table of Any Number
val = int(input('Enter Value: '))
for i in range(10):
        i += 1
        result = val*i
        print(val, 'x', i, '=', result)

# Fibonacci Number 0,1,1,2,3,5,8,13....
FibList = [0,1]
def Fibonacci(n):
    if n<0:
        print('invalid input')
    elif n< len(FibList):
        return FibList[n]
    else:
        FibList.append(Fibonacci(n-1) + Fibonacci(n-2))
        return FibList[n]
n = int(input('Fibonacci Number is: '))
print(Fibonacci(n))

# Calculate Sqare Root
import math
number = float(input('Enter Number: '))
print(math.sqrt(number))