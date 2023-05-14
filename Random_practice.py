# Random Practice
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