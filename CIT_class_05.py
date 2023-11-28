# Loop
# While Loop and loop break and continue
b = 10
while b>0:
    b = b-1
    if b == 3:
        break
    print('loop break:',b)
    print("\n")

c = 10
while c>0:
    c = c-1
    if c == 3:
        continue
    print('loop continue:',c)
    print("\n")

# For Loop Odd number
for i in range(1,11,2):
    print('For Loop is:',i)
    print("\n")

# For Loop Even number
for j in range(0,11,2):
    print('For Loop is:',j)
    print("\n")

# Print Star Pyramid
star = int(input('Enter Number: '))
k = star-1
for i in range(0, star):
    for j in range(0, k):
        print(end=' ')
    k = k - 1
    for j in range(0, i+1):
        print('* ', end='')
    print('\r')

# Print Star with * Pyramid
for z in range(1,8):
    print(z*'*')
    print("\n")

# Print Star revers Pyramid
for w in range(7,0,-1):
    print(w*'*')
    print("\n")

# Print Star revers Pyramid with reversed method
for a in reversed(range(1,8)):
    print(a*'*')
    print("\n")

# Table of any Number
val = int(input('Enter Value: '))
for i in range(10):
        i += 1
        result = val*i
        print(val, 'x', i, '=', result)

