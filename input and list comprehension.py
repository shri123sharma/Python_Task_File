"""
name=input("enter a name")

print("this is name",name)

val=input('enter a value')

print("this is",val)
print(type(val))

num1=input("enter a number1")
num2=input("enter a number2")
num3=input("enter a number3")

if num1>num2 and num1>num3:

    print("first number is",num1)

elif num2>num3 and num2>num1:

    print("second number is",num2)
else:
    print("third number is greater",num3)

a=input("enter a name")
b=input("enter a surname")

c=a+b
print(c)
# typecasting conversion
num1=int(input("enter a number"))
num2=int(input("enter a number"))

number=num1+num2
print(number)
print(type(num1))

num3=float(input("enter a number"))
num4=float(input("enter a number"))

number_1=num3*num4
print(number_1)
print(type(num4))
#multiple input in user
#if two method in used in multiple input in user
#split() method
#list comphrension 

#syntax:
#input().split(separtor,maxsplit)


x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()

#list comprehension
#list_1=[Expression for i in list_1 if i%2==0]

from ast import comprehension


list_1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

list_2=[]

for i in list_1:

    list_2.append(i+1)

print(list_2)

#with list compehenion
list_1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

list_2=[i+1 for i in list_1]
print(list_2)

#list comprehension syntax:
#list_2=[expresssion looping statement conditional statement]

list_1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

list_2=[]

for i in list_1:
    list_2.append(i+1)
    if i%2==0:
    
        print(i)

list_2=[i+1 for i in list_1 if i%2==0]
print(list_2)

# list comprehension
lst_1=[]

for i in range(20):
    if i%2==0:
        lst_1.append(i)
print(lst_1)

#with list comprehension

lst_1=[i for i in range(20) if i%2==0]
print(lst_1)

#list comprehension

list_1=[]

for i in range(20):

    if i%2==0:

        if i%3==0:

            list_1.append(i)
print(list_1)

# with list comprehension

list_1=[i for i in range(20) if i%2==0 if i%3==0]

#list comprehension
leap_year=int(input("enter a year"))

if leap_year%100==0:

    if leap_year%400==0:

        print("this is leap year")
    else:
        print("this is not leap year")

else:
    if leap_year%4==0:

        print("this is leap year")
    else:
        print("this is not leap year")

list_1=[1,2,3,4,4,5,6,7,7,8,8,9,9]
list_2=[]
for i in list_1:

    if i%2==0:
        list_2.append(i**2)
    else:
        print("invalid")

print(list_2)

list_1=[1,2,3,4,4,5,6,7,7,8,8,9,9]

list_2=[i**2 for i in list_1 if i%2==0]
print(list_2)
"""
#\n newline 
from ctypes.wintypes import PINT


a="my self shrikant\n sharma"
b="this is\n brand"
print(a)
print(b)

print("indore",end="88")
print("bhopal")

a="hello"

print(a,"how are","you")

print("hello",end="_")
print("how are you")

l=[1,2,3,4,5,6,7]
print(*l)

a="shrikant"
b="sharma"

print(a,end="Q")
print(b,end="S")

print("a","b","c",sep="")
print(8,10,2022,sep="-")
print('hello','hi',sep="",end="*")

print("value1:%,value2:%",100,200)
print("i love you{} and this is best{}".format("geeks","geeksforgeeks"))

string_1="hello how are you"
print("hi this is me")

print(string_1.center(40,"#"))
print(string_1.ljust(40,"_"))
print(string_1.rjust(40,"*"))

#arithmathic operators

a=10
b=20

#add
c=a+b
print(c)

c=a-b
print(c)

c=a*b
print(c)

c=a/b
print(c)

c=a%b
print(c)

c=a**b
print(c)

c=a//b
print(c)
# comparsion operators and relational operators

a=100
b=200

c=a>b
print(c)

c=a<b
print(c)

c=a==b
print(c)

c=a!=b
print(c)

c=a>=b
print(c)

c=a<=b
print(c)

a=100
b=200
c=300

if a>b and a>c:

    print("a is greater")
elif b>c and b>a:

    print("b is greater")
else:
    print("c is greater") 

a=10
b=10.00
c="shrikant"
d="sharma"
e=[1,2,3,4,5,6]
f=("shri","kant","sharma","21","indore")
g={"s","h","r","i","k","a","n","t"}
h={"1":"shrikant","2":"ajay","3":"risabh","4":"arun"}
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)

a=10
b=20

a+=b
print(a)

a-=b
print(a)

a*=b
print(a)

a/=b
print(a)

a//=b
print(a)

a,b=20,10

if a!=b:

    if a>b:
        print("first condition")

    else:
        print("wrong condition")
else:
    print("both condtion are wrong")



