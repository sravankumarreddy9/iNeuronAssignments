#Assignment3
#Task1
#Question no 1
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Not possible")

#Question no 2
subjects=["Americans ","Indians "]
verbs=["play ","watch "]
objects=["Baseball","Cricket "]
for i in subjects:
    for j in verbs:
        for k in objects:
            print(i+j+k)

#Question no 3
import numpy as np
x = np.array([1,2,3,4])
N=3
print(np.vander(x,N))
print(np.column_stack([x**(N-1-i) for i in range(N)]))
print(np.vander(x))
print(np.linalg.det(np.vander(x)))