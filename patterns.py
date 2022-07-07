"""
row=5

for i in range(0,row):

    for j in range(0,i+1):

        print('*',end='')

    print(' ')

string="shrisasaksjshrijskjkshri"
length=len(string)
count=0
for i in range(len(string)):
    if string[i:i+4]=="shri":
        count=count+1
print(count)

list=[1,2,3,4,56,7,8]
list.append(100)
print(list)

list.clear()
print(list)

list=["shri","name","india"]
for i in list:
    for j in i:
        print(j)

tuple=(1,2,3,4,5,7)
a=tuple[0]
print(a)

b=tuple[0]="shrikant"
print(b)

def function():

    pass

print(function())

a=["shri","india","hello"]
b=["1","2","3","4","5"]

c=zip(a,b)
print(tuple(c))
d=zip(a,b)
print(set(d))
e=zip(a,b)
print(dict(e))

class Name(object):

    def __init__(self,fname,lname):

        self.fname=fname
        self.lname=lname

    def show(self):
        full_name=self.fname+self.lname
        print(full_name)
object=Name("shri","sharma")
object.show()

list=[1,2,3,4,5,5,6,7,7,7,8,99,9,55,4,4,33,2,2,2,]

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]

print(list)
print(list[::-1])

string="shrikant"
str_1=""
for i in string:
    str_1=i+str_1
print(str_1)

list=[1,2,3,4,5,6,6]
list_1=[]

for i in list:
    list_1=i+list_1

print(list_1)

list=[1,2,3,567,8,9]
pass
if list==8:

    break
    
elif list%2==0:
    continue
else:
    print("both are not execute")

list=[1,13,4,5,6,6,76,8,8,7,8,7,8,7,8,00,4234354,65,76,8,5,35577,5,46,]
slice=list[0:7:1]
slice_1=list[0:10:2]
slice_2=list[-7:-1:1]
a=list[::-3]
print(a)

import array

a=array.array("i",[1,2,3,4,5,6,7,8])
sum=0
for i in a:
    if i%2==0:
        print(a)
    else:
        if i%2!=0:
            sum=sum+i
print(sum)

number=int(input("enter a number is disarinum")) #175 
length=0

while number!=0:
    number=number//10
    length=length+1

print(length)
duplicate=int(input("enter a number"))
sum=0
len=length

number=duplicate
while duplicate>0:
    rem=duplicate%10
    sum=sum+int(rem**len)
    duplicate=duplicate//10
    len=len-1
print(sum)

if sum==number:
    print(sum,"this is disarinum number")
else:
    print(sum,"this is not disarinum number")

import array
arr_1=array.array("i",[1,2,3,4,5])
arr_2=array.array("i",len(arr_1))

for i in range(0,len(arr_1)):
    arr_2[i]=arr_1[i]

print("orginal arry")

for i in range(0,len(arr_1)):
    print(arr_1[i])

for i in range(0,len(arr_2)):
    print(arr_2[i])

#Initialize array     
arr1 = [1, 2, 3, 4, 5]     
     
#Create another array arr2 with size of arr1    
arr2 = [None] * len(arr1)   
     
#Copying all elements of one array into another    
for i in range(0, len(arr1)):    
    arr2[i] = arr1[i]     
     
#Displaying elements of array arr1     
print("Elements of original array: ")   
for i in range(0, len(arr1)):    
   print(arr1[i])    
     
print()   
     
#Displaying elements of array arr2     
print("Elements of new array: ")   
for i in range(0, len(arr2)):    
   print(arr2[i]) 

array1=[10,20,30,40,50]

array2=[None]*len(array1)

for i in range(0,len(array1)):
    array2[i]=array1[i]

print("orginal array")

for i in range(0,len(array1)):
    print(array1[i])

print("copy element in next array")
for i in range(0,len(array2)):
    print(array2[i])

import array #using module name
import array as arr #using alias name
from array import* #using this type in popular 

import array

# a=array.array("S",["name","age","district","state"])
a=array.array("i",[1,23,4,5,6,7,9])

for i in a:
    print(type(a))
    # print(isinstance(a, class_or_tuple))
    print(i)

import array as arr

a=arr.array("i",[10,20,30,405,50])
print(type(a))
print(a)

from array import*

a=array("i",[100,200,300,400,500])
print(a)
print(type(a))
print(a[0])

a[2]=30000
print(a)

import array as arr
b=array("b",[1,2,3,5,6,7,8,])
print(a)
print(type(a))
print(b[0])
print(b[-1])
print(b[-5:-2])

from array import*
a=array("d",[1.0,1.1,1.2,1.3])
print(a)
print(type(a))
print(a[0:3])
for i in a:
    print(i)
print(len(a))
# import array 
# c=array.array(typecode="u",["shri","india","name"])
# print(c)
# print(type(c))
# print(c[3])

import array

arr_1=array.array("d",[1.0,2.0,3.0,4.0,5.0])
print(type(arr_1))
print("orginal array",arr_1)
arr_1.append(6.0)
print("update value in append",arr_1)
arr_1.extend([10.0,11.0,15.0])
print("multiple item in store of array",arr_1)
arr_1.insert(1, 10000)
print("array in insert value in 1 postion",arr_1)

for i in arr_1:
    if i==[2]:
        r=arr_1.remove(i)
        print("remove element",r)

import array

a=array.array("i",[1,5,4,4,3,5,3,])
print(type(a))
print(a)
print(a.pop())
print(a.pop(1))
b=a.remove(5)
print(b)

print(a.count(4))
print(a.index(1))
print(a.reverse())

import re

string="this is me"
x=re.search("^this.*me$", string)

if x:
    print("yes it is matching")
else:
    print("No Match") 

import re
string="my name is shrikant sharma"
x=re.findall("a", string)
print(x) 

import re
str_1=shrikant is 24 and ajay is 25
        arun is 26 and sarika is 22
age=re.findall("\d{1,3}", string)
print(age)

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(1,6):
    for j in range(1,)

row=5 

for i in range(1,row+1):
    for j in range(0,i):
        print(i,end=" ")
    print("")

row=5

for i in range(1,row+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")
row=10
for i in range(1,row+1):
    for j in range(1,i+1):
        print("*",end="")
    print("")

row=5
for i in range(1,row+1):
    for j in range(row+1,i,-1):
        print(i,end="")
    print("")

row=5
col="8"
for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(col,end=" ")
    print("")

row=5
for i in range(1,row+1):
    for j in range(0,i):
        print((i*2-1),end=" ")
    print("")

row=5
k=2*row-2

for i in range(1,row+1):
    for j in range(1,k):
        print(end="")

    k=k-1

    for j in range(1,i+1):
        print("*",end="")
    print("")
"""

# row=6
# for i in range(1,row+1):
#     for j in range(row):
#         # import pdb;pdb.set_trace()
#         if i==1 or j==1 or i==5 or j==5 :
#             print("*",end=" ")
#         else:
#             if j==1:
#                 print("*",end=" ")
            
#     print("")
"""
row=5
k=0
for i in range(1,row+1):
    for s in range(1,(row-i)+1):
        print(end=" ")

    while k!=(2*i-1):
        print("* ",end="")
        k+=1
    print(" ")
"""
i=1
k=1
while i<=5:
    b=1
    while b<=5-i:
        print("",end=" ")
        b+=1

    j=1
    while j<=k:
        print("*",end="")
        j+=1
    
    k+=2
    print("")
    i+=1

i=5
k=9
while i>=1:
    b=1
    while b<=5-i:
        print("",end=" ")
        b-=1

    j=5
    while j<=k:
        print("*",end="")
        j-=1
    
    k-=2
    print("")
    i-=1
""""
#global 

x=100
y=200

def func():
    x=200
    y=300
    print("both are value add",x+y)

func()

print("both value are add",x+y)

a=100
print

string="my name is shrikant sharma"
string_1='this is me'

print(string)
print(type(string_1))
print(string[1])
print(string[-1])

# i="1"
# while i<=string:
#     print(i)
#     i=i+1

for i in string:
    print(i)
#for i in (len(string)):
#   print(i)
for i in range(1,len(string)):
    print(i)
if "is" in string:
    print(string)

print(string[11:19])
print(string[:20])
print(string[5:])
print(string[-6:-1])

str1="Get certified by completing a course today!"
print(str1)
print(type(str1))
print(str1.upper())
print(str1.lower())
print(str1.strip())
print(str1.replace("course", "blog"))

str2="Python has a set of built-in methods that you can use in strings."
age=23
list=[]
s=str2.split()
for i in s:
    if list.append(i):
        print(list)

print(str2.format(age))
print(str2.count("a"))
print(str2.count("in"))
print(str2.index("in"))
"""





    

   

    
