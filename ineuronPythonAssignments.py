# Python assignment
# Task 1
# 2nd question
lower = 2000
upper = 3200
for i in range(lower, upper+1):
    if not (i%7) and (i%5):
        print(i)

# 3rd question

str1 = str(input("Enter first name"))
str2 = str(input("Enter second name"))
print("before reversing")
str = str1 + " " + str2
print(str)
print("After reversing")
print(str2+ " " + str1)

# 4th question

PI = 3.14
dia = 12
r = dia/2
v = 4/3 * PI * (r**3)
print(v)

# Task 2
# 1 Question no 1

l = []
n = int(input("How many numbers you want to enter"))
for i in range(0, n):
    lst = int(input())
    l.append(lst)
print(l)

# 2 Question no 2
n=5
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

# 3 Question no 3
s = str(input("Enter a string"))
print(s[::-1])

# 4 Question no 4
print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t and to secure to all its citizens")