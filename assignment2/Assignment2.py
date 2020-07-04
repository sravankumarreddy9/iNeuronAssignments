#Assignment 2
#Task 1
#question no 1
def myreduce(func, seq):
    result = seq[0]
    for item in seq[1:]:
        result = func(result, item)

    return result
def sum(x,y):
    return x+y
print (str(myreduce(sum, [34,4,5])))

#question no 2
def myfilter(func, seq):
 result = []
 for item in seq:
  if func(item):
   result.append(item)
 return result

def isgreater(x):
    if(x>=3):
        return True
    else:
        return False
print(str(myfilter(isgreater,[23,4,-1,-5,4])))

#question no 3
str = "acadgild"
str = str.upper()
l=[]
for i in str:
    l.append(i)
print(l)
l = ['x','y','z']
result = []
for i in l:
    for num in range(1,5):
        result.append(i*num)
print(result)
k = ['x','y','z']
result=[]
for num in range(1,5):
    for i in k:
        result.append(i*num)
print(result)
nums=[2,3,4]
result = []
for i in nums:
    for num in range(0,3):
        result.append([i+num])
print(result)
nums = [2,3,4,5]
result = [[i+num for i in nums] for num in range(0,4)]
print(result)

nums=[1,2,3]
result=[]
for i in nums:
    for j in nums:
        result.append((i,j))
print(result)

#question no 3
l= ["space", "titan", "marvel heros", "dc"]
max=''
for i in range(0, len(l)):
    if(len(max)<len(l[i])):
        max = l[i]
print(max)

#Task 2
import cmath
#Question no 1
class areaoftriangle:
    def __init__(self, a, b, c):
        self.a=float(a)
        self.b=float(b)
        self.c=float(c)
a=float(input("a= "))
b=float(input("b= "))
c=float(input("c= "))

class triangle(areaoftriangle):
    def __init__(self, a, b, c):
        super().__init__(a,b,c)

    def get_area(self):
        s =(a + b + c)/2
        return (s*(s-a)*(s-b)*(s-c)) ** 0.5
t = triangle(a,b,c)
print(t.get_area())

#Question no 2
def filter_long_words(inputList,inputInteger):

    l = []
    for i in range(len(inputList)):
        if len(inputList[i]) > inputInteger:
            l.append(inputList[i])
    return l
words = ['space','The avengers', 'dc']
wordlen = 5
print (str(filter_long_words(words,wordlen)))

#Question no 3
words = ['space','The avengers', 'dc']
l = []
for i in range(len(words)):
    l.append(len(words[i]))
print ("List of words:"+str(words))
print ("List of wordlength:"+str(l))

#Question no 4

def isVowel(char):
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u' or char=='A' or char =='E' or char =='I' or char=='O' or char=='U':
        return "True"
    else:
        return "False"
char= input("enter a alphabet")
if isVowel(char)=="True":
    print("alphabet is vowel")
else:
    print("alphabet is not vowel")