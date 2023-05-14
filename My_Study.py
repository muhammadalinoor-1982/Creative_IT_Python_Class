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

# Given an integer n, the task is to find the sum of the series 1^1 + 2^2 + 3^3 + ….. + n^n using recursion.
n = int(input('Insert value of n: '))
def sum(n):
    if n == 1:
        return 1
    else:
        return pow(n, n) + sum(n - 1)
print(sum(n))

# You have been given a series (1*1) + (2*2) + (3*3) + (4*4) + (5*5) + … + (n*n), find out the sum of the series till nth term
n = int(input('Enter value of N: '))
def serise(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (i * i)
    return sum
print(serise(n)) 

# Given a positive integer n and the task is to find sum of series 1 + 2 + 2 + 3 + 3 + 3 + . . . + n. 
n = int(input('Enter Value of N: '))
def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i * i
    return sum
print(sumOfSeries(n))

# Given a positive integer n and the task is to find the sum of series 1*2*3 + 2*3*4 + 4*5*6 + . . .+ n*(n+1)*(n+2 
n = int(input('Enter the value of N: '))
def mulSeries(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i * (i + 1) *  (i + 2)
        i += 1
    return sum
print(mulSeries(n))

# You have been given a series 1/1! + 2/2! + 3/3! + 4/4! +…….+ n/n!, find out the sum of the series till nth term.
n = int(input('Enter the value of N: '))
def sumSeries(n):
    sum = 0
    fact = 1
    for i in range(1, n+1):
        fact *= i
        sum += i / fact
    return sum
print(sumSeries(n))

# Python Program for Find sum of Series with n-th term as n^2 – (n-1)^2.
n = int(input('Enter Value of N: '))
mod = 999
def findSum(n):
    return ((n % mod) * (n % mod)) % mod
print(findSum(n))

# Python Program to find Sum of the series 1*3 + 3*5 + …..
n = int(input('Enter value of N: '))
def SumSeries(n):
    sum = 0
    for i in range(n):
        sum += (2 * i + 1) * (2 * i + 3)  
    return sum
print(SumSeries(n)) 

# Recursive program to find the Sum of the series 1 – 1/2 + 1/3 – 1/4 … 1/N.
def sumOfSeries(i, n, s) :
 
    # Base case
    if i>n :
        return s
 
    # Recursive case
    else :
 
        # If we are currently looking
        # at the even number
        if i % 2 == 0 :
            s-= 1 / i
 
        # If we are currently looking
        # at the odd number
        else :
            s+= 1 / i
        return sumOfSeries(i + 1, n, s)
 
# Driver code
if __name__ == "__main__":
    print(sumOfSeries(1, 3, 0))

# Traverse the whole linked list and count the no. of nodes. 
# Now traverse the list again till count/2 and return the node at count/2. 
# Python program for the above approach
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class NodeOperation:
    # Function to add a new node
    def pushNode(self, head_ref, data_val):
 
        # Allocate node and put in the data
        new_node = Node(data_val)
 
        # Link the old list of the new node
        new_node.next = head_ref
 
        # move the head to point to the new node
        head_ref = new_node
        return head_ref
 
    # A utility function to print a given linked list
    def printNode(self, head):
        while (head != None):
            print('%d->' % head.data, end="")
            head = head.next
        print("NULL")
 
    ''' Utility Function to find length of linked list '''
 
    def getLen(self, head):
        temp = head
        len = 0
 
        while (temp != None):
            len += 1
            temp = temp.next
 
        return len
 
    def printMiddle(self, head):
        if head != None:
            # find length
            len = self.getLen(head)
            temp = head
 
            # traverse till we reached half of length
            midIdx = len // 2
            while midIdx != 0:
                temp = temp.next
                midIdx -= 1
 
            # temp will be storing middle element
            print('The middle element is: ', temp.data)
 
 
# Driver Code
head = None
temp = NodeOperation()
head = temp.pushNode(head, 5)
head = temp.pushNode(head, 4)
head = temp.pushNode(head, 3)
head = temp.pushNode(head, 2)
head = temp.pushNode(head, 1)
temp.printNode(head)
temp.printMiddle(head)


