# Random Practice
mark = float(input('Enter Marks: '))
if mark >= 90 and mark <= 100:
    print('Grade point average GPA: A+')
elif mark >= 79 and mark <= 89:
    print('Grade point average GPA: A')
elif mark >= 69 and mark < 79:
    print('Grade point average GPA: A-')
elif mark >= 59 and mark < 69:
    print('Grade point average GPA: B')
elif mark >= 49 and mark < 59:
    print('Grade point average GPA: C')
elif mark >= 39 and mark < 49:
    print('Grade point average GPA: D')
elif mark >= 33 and mark < 39:
    print('Grade point average GPA: E')
elif mark < 33:
    print('GPA: F Failed')
else:
    print('Invalid input')

