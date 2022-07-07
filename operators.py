"""
a=100
b=300

print(a+b)

name="shri"
sur="sharma"

print(name+sur)

#operators overloading in python __add__

class Parent():

    def __init__(self,a):

        self.a=a

    def __add__(self,o):

        return self.a+o.a

o1=Parent(1)
o2=Parent(2)

o3=Parent("hello")
o4=Parent("world")

print(o1+o2)
print(o3+o4)

class Parent():

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def __add__(self,other):

        return self.a+other.a,self.b+other.b

obj1=Parent(1,2)
obj2=Parent(10,20)

print(obj1+obj2)
#comparsion operators in overloading type
class A():

    def __init__(self,a):

        self.a=a
    def __gt__(self,other):

        if self.a>other.a:

            return True

        else:

            return False
obj1=A(1)
obj2=A(2)

if obj1>obj2:

    print("obj1 greater than obj2")

else:

    print("obj2 greater than obj1")
#overloading operators in equal and less than 

class Parent():

    def __init__(self,a):

        self.a=a
    def __lt__(self,other):

        if self.a<other.a:

            return "obj1 is less than obj2"
        else:

            return "obj1 is greater than oj2"

    def __eq__(self,other):

        if self.a==other.a:

            return "both are equal"
        else:

            return "both are not equal"
obj1=Parent(100)
obj2=Parent(200)

print(obj1<obj2)
print(obj1==obj2)
# any method in opertors
list_1=[1,2,3,4,5]
list_2=[1,2,4,6,7]

result=list_1==list_2
print(any(result))

list_1=[1,2,3,4,5]
list_2=[1,2,3,5,8]

result=list_1==list_2
print(all(result))
"""

#operators predefind function
import operator
a=100
b=200
c=a+b
print(c)

# add(),sub(),mul(),floordivsion(),exponents()
a=100
b=10

print("this is addition value in both",end="")
print(operator.add(a,b))

print("this is substraction",end="")
print(operator.sub(a,b))

print("this is multiply",end="")
print(operator.mul(a,b))

print("this is equal",end="")
print(operator.eq(a,b))

print("this is divsion",end="")
print(operator.floordiv(a,b))

c=100
d=222

if (operator.lt(a,b)):

    print("this is less than to other")

else:

    print("this is never less than other")

#opertors function in python

li=[1,3,5,7,9,11,13]

print("this is orginal list",end="")
for i in range(0,len(li)):

    print(li[i],end=" ")


li=[10,30,50,70,90,110,130]

operator.getitem(li,2)

print("this is modified function in li",end="")

for i in range(0,len(li)):

    print(li[i],end=" ")

#opeartors is and equal 

list_1=["banana","apple","cherry"]
list_1=["banana","cherry","apple"]
list_2=["apple","cherry","mango"]

print(list_1==list_2)
print(list_1 is list_1)
print(id(list_1))
print(id(list_1))

#membership oprators

list_1=[1,23,4,5,6,7]
list_2=[12121,1212,21,23,54,5,66]

# print(list_1 in list_2)
for item in list_1:

    if item in list_2:
        print("overlap")
else:
    print("not overlap")

list_1=[]
list_2=[]

for i in range(0,10):

    list_1.append(10*i)
    if i%3==0:
        list_2.append(i)
else:
    print(list_1)

list_1=[]
list_2=[]

for i in range(0,11):

    list_1.append(4*i)

print(list_1)

for i in range(0,10):

    list_2.append(list_1[i]%5==0)

print(list_2)
print(list_1[i])

list_1=[]
list_2=[]

for i in range(1,11):

    list_1.append(4*i-3)

print(list_1)

# for i in range(1,11):

    # list_2.append(list[i]%2==1)

# print(list_2)

a=1000
b=2000

print(operator.add(a,b))

a=10
b=20
print(operator.add(a,b))

a=1000
b=200

if operator.lt(a,b):

    print("this is never less than to a")
else:
    print("this is less than to b")