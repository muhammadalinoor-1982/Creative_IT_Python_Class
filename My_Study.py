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

# Bubble Sort
def bubblesort(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i+1]:
                swapped = True
                elements[i], elements[i+1] = elements[i+1], elements[i]
        if not swapped:
            return
elements = [7,25,3,100,65,13,125,4,90,15,13,0]

print('Unsorted Elments: ', elements)
bubblesort(elements)
print('Sorted Elements: ', elements)

# Python program to count words in a sentence
# print(len(input('Please Enter your string: ').split()))
speech = 'my name is aupu'
res = len(speech.split())
print(res)