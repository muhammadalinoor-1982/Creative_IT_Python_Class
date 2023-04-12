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

# For Loop star
for p in range(0,11,2):
    print('For Loop is:',p)
    print("\n")

# Print Star Pyramid
star = int(input("Enter number of star: "))
for k in range(star):
    for l in range(k+1):
        print("* ", end="")
    print("\n")

# Print Star revers Pyramid
for z in range(1,8):
    print(z*'*')
    print("\n")

# Print Star revers Pyramid
for w in range(7,0,-1):
    print(w*'*')
    print("\n")

# Print Star revers Pyramid
for a in reversed(range(7,0,-1)):
    print(a*'*')
    print("\n")
