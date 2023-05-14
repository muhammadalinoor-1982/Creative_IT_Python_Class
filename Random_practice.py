# Random Practice
# Program to find the sum of a Series 1 + 1/2^2 + 1/3^3 + …..+ 1/n^n
n = int(input('Enter the value of N: '))
def serSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1 / pow(i, i)
    return sum
print(round(serSum(n),5)) 
