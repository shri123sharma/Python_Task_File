"""
list=[1,20,20,10,10,3,4,5,6]

for i in range(0,len(list)):

    for j in range(i+1,len(list)):

        print(j)
    
print(i)

list_2=[10,20,30,40,50]

sum=0

for i in list_2:

    sum=sum+i
print(sum)

def sum_list(items):

    sum=0

    for i in items:

        sum=sum+i

    return sum
print(sum_list([1,2,3,4]))

def add(a,b):

    return a+b

print(add(10,29))

def multiply(list):

    multi=1

    for i in list:

        multi=multi*i

    return multi
print(multiply([10,20,30,40]))

def substract(items):

    sub=1

    for i in items:

        sub=sub-i
    return sub

print(substract([100,200,3000,4000,5000]))

def max_num_list(list):
    max=list[0] #1
    for i in list:
        if i>max:
            max=i
    return max
print(max_num_list([1,2,3]))
    
list=[1,2,3,4,4]
max=list[0]
print(max)

list=[1,2,3,4,5,6,7]
list_1=[]

for i in range(0,len(list)):

   list_1.append(i**2)

print(list_1)

list_1=[i**2 for i in range(0,len(list))]
print(list_1)

list=[10,20,30,40,50]
list_1=[]
for i in range(0,len(list)):
    list_1.append(i**2)
    if i%2==0:
        print(list_1)

list_1=[]
for i in range(20):
    if i%3==0:

        list_1.append(i**2)

print(list_1)

list_1=[i**2 for i in range(20) if i%2==0]
print(list_1)

def ticket():

    "eligiable candidate"

    a=int(input("enter a number first"))
    b=int(input("enter a number second"))
    c=int(input("enter a number third"))

    if a>b and a>c:
 
        print("first is greater",a)

    elif b>c and b>a:

        print("second is greater",b)

    else:

        print("third is greater",c)

ticket()

def compare(a,b,c):

    "comparsion in function"

    if a>b and a>c:

        print("first is greater",a)

    elif b>a and b>c:

        print("second is greater",b)

    else:
        print("third is greater",c)

compare(10,20,30)

def add(x):

    if x%2==0:

        print(x)
    else:
        print("this is else block")
add(2)

def exponent(x,y=20):

    "exponent content"

    return x+y

print(exponent(10))

def message(msg,person):

    "keyword aegument"

    print(msg,person)

message(msg="hello",person="ajay")
message(person="risabh",msg='hii')

from re import X
from tkinter import Y


def odd():

    list=[1,2,3,4,5,6,6,7]

    for i in list:
        if i%3==0:
            print(i)
print(odd())

def marks():

    student=int(input("enter a marks"))

    if student>0 and student<=33:
        print("your are fail in this exam")

    elif student>33 and student<=40:

        print("your grade is D")
    elif student>40 and student<=50:
        print("your grade is C")

    elif student>50 and student<=70:

        print("your grade is B")
    elif student>70 and student<=85:

        print("your grade is A")
    else:
        print("your Grade is A+")
marks()

def message(name,msg="happy diwali"):

    "this is message for all"

    return name+msg

print(message("shrikant","happy new year"))

def multiple(*x):

    "multile item in collection"
    for i in x:

        print(i)

multiple('shrikant','ajay','arun')

def multiple_pair(**kwargs):

    "this is colection in pair form"

    for keys,values in kwargs.items():

        print(keys,values)

multiple_pair(first='hello',second='hii',third='welcome')

def both(*args,**kwargs):

    print("first is",args)
    print("second is",kwargs)

both('ajay','risabh',first='hi',second='hello',third='welcome')

def simple_add():

    yield 1
    yield 2
    yield 3

for i in simple_add():

    print(i)
simple_add()

def add(a,b):

    yield a+b
    
print(add(10,20))

def object():

    yield 1
    yield 2
    yield 3

x=object()

print(x.next())
print(x.next())
print(x.next())

def value():

    yield 1
    yield "shrikant"
    yield [1,2,3,4,5,6,7]

    x=value()

    print(x.next())
    print(x.next())
    
    print(x.next())

list=[1,2,3,4]

print(lambda list:list)

tuple=(100,200,3000,400)

a=lambda tuple:tuple

print(a(tuple))
# print(tuple)

def cube(x):

    return x*x*x

print(cube(7))

b=lambda y:y*y*y
print(b(5))

list=[1,3,5,6,7,88,323]
list_1=[]

c=lambda list:list.pop()
print(c)

list_1.append(c)
print(list_1)

a=lambda a,b:a+b
print(a(10,20))

b=lambda c,d:c-d
print(b(100,40))

list=[10,20,30,]
c=lambda list:print(list.append(100))
print(c(list))

list=[2,5,8,13,15,18,20,21,22,14,19,37,33]

filtered=filter(lambda x:x%2==0,a)
print(list(filtered))

list=[2,5,8,13,15,18,20,21,22,14,19,37,33]

filtered=map(lambda x:x%2==0,a)
print(list(filtered))

from itertools import chain
from re import S


def add():

    a=100
    b=200

    return a+b
print(add())

a=100
b=200
def add():
    x="shrikant"
    print(a+b)
    print(x)
add()
print(a-b)
print(a**b)

a="how are you"

def msg():
    global s
    s=" i'm fine"
    return s+a
print(msg())
print(a)

a=100
b=200

def add():

    print(a+b)
add()
a=200
b=300

def add():

    global a

    a=a+5
    return a
print(add())

def add():

    a=100

    def change():
        global a
        y=100
        return a+y
    print(change())
   
print(add())

def msg(text):

    return text.upper()

print(msg("hello"))

object=msg
print(object("welcome"))

def add(a,b):

    return a+b

print(add(10,20))

object=add
print(object(100,200))

def square(num):
    for i in range(num):
        if i**2:
            return i
print(square(10))
obj=square
print(obj(100))

def add(text):

    return text.upper()

def multi(text):

    return text.lower()

def greet(func):

    obj=func("welcome to this world")
    print(obj)

greet(add)
greet(multi) 

def create(x):
    def adder(y):
        return x+y
    return adder

obj=create(20)
print(obj(10))

a=100
b=200

c=a+b
print(c)

def add(a,b):

    c=a+b
    print(c)
add(10,20)

class add:

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def sys(self):

        print(self.a+self.b)

obj=add(100,20)
obj.sys()

a=100
b=101

if a%2==0:

    print("prime no")

else:
    print("not a prime no")

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

year=2012

if ((year%400==0)or(year%100!=0)and(year%4==0)):

    print("this is leap year")

else:

    print("this is not leap year")

num=int(input("enter a number"))

count=0
i=1

while i<=num:

    if num%i==0:
        count+=1
    i+=1
if (count==2):

    print("this is prime number")
else:
    print("this is not prime number")

num=8

if num>1:

    for i in range(2,num):
        if num%i==0:
            print("this is not prime number")
            break
    else:
        print("this is prime number")
else:
    print("this is not prime number")

def check(num):

    if num>0:

        print("this is postive number")
    elif num<0:

        print("this is negative number")

    else:

        print("this is zero number")
check(-1)

a=float(input("first number"))
b=float(input("second number"))
c=float(input("third number"))

s=a+b+c/2

a=(s*(s-a)*(s-b)*(s-c))*0.5
print(a)

def triangle():

    a=float(input("first side of area"))
    b=float(input("second side of area"))
    c=float(input("third side of area"))

    s=a+b+c/2

    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print("this is area of triangle",area)
triangle()

class triangle():

    def __init__(self):
        self.a=float(input("enter a first value"))
        self.b=float(input("enter a second value"))
        self.c=float(input("enter a third value"))

    def result(self):

        s=self.a+self.b+self.c/2

        area=(s*(s-a)*(s-b)*(s-c))**0.5

        print("this is area of trainagle",area)

obj=triangle()
obj.result()

import math
def triangle(a,b,c):

    s=(a+b+c)/2

    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("area of triangle",area)
triangle(8,9,10)

class triangle(object):

    def __init__(self,a,b,c):

        self.a=a
        self.b=b
        self.c=c

class area(triangle):

    def method(self):

        s=(self.a+self.b+self.c)/2

        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

object=area(8,9,10)
print("this is area of triangle",object.method())

a=float(input("enter a number 1"))
b=float(input("enter a number 2"))

area=(a*b)/2
print("this is area",area)
a=100
b=200
c=300

d=a+b+c
area=a
width=b
height=c

awh=area+width+height
print(awh)

import random
n=random.random()
print(n)

n=random.randint(0, 100)
print(n)

import random 

list_1=[]
for i in range(0,10):

    n=random.randint(1, 20)
    list_1.append(n)
print(list_1)

import random

tuple=[]
for i in range(1,20):

    n=random.randint(0, 10)
    tuple.append(n)
print(tuple)

import random

list_1=random.sample(range(0,10),4)
print(list_1)

kilometer=float(input("enter a speed of car in kilometer unit"))

miles=kilometer*0.62137

print("this is kilometer converted in miles",miles)

def kilo(a):

    miles=a*0.62137
    return miles
print(kilo(20))

miles=float(input("enter a miles in car unit"))

kilometer=miles/0.62137

print("this is miles to kilometer",kilometer)

degree_c=float(input("enter a temperature in degree celsius"))

fahrenheit=(degree_c*1.8)+32

print("this is converted to celsius to fahrenheit",fahrenheit)

def fahrenheit(a):

    f=(a*1.8)+32
    return f
print(fahrenheit(50))

class fahrenheit(object):

    def __init__(self,a):

        self.a=a
class celsius(fahrenheit):

    def method(self):

        f=(self.a*1.8)+32
        return f
obj=celsius(34)
print("this is degree celsius to farenheit",obj.method())

def celsius(a):

    c=(a-32)/1.8
    return c
print(celsius(93.2))

def reverse(string):

    str_1=""

    for i in string:

        str_1=i+str_1
    return str_1
print(reverse("shrikant"))

def reverse(string):

    str_1=""
    count=len(string)
    while count>0:

        str_1=str_1+string[count-1]
        count=count-1
    return str_1
print(reverse("ajay"))

def reverse(string):

    str_1=string[::-1]

    return str_1
print(reverse("arun"))

str_1="my name is shrikant sharma"

str_2=str_1[::-1]

print(str_2)

def reverse(str):

    str_1="".join(reversed(str))

    return str_1
print(reverse("risabh"))

def list(a):

    list_1=[]

    for i in a:
    
        list_1.append(i[::-1])
        
    print(list_1)
list([1,23,4,5])

a=float(input("enter a first value"))
b=float(input("enter a second value"))
c=float(input("enter a third value"))

perimeter=a+b+c
s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5
print("this is perimeter of triangle",perimeter)
print("this is area of triangle",area)

a=100
b=200
c=300

#first swap variable
area=a
width=b
center=c

#second swap variable
age=area
weight=width
systeam=center

#adding the element of swap variable
add=age+weight+systeam
substract=add-weight-systeam
multi=add*weight*systeam
divide=add/weight/systeam

#add print function in this operation
print(add)
print(substract)
print(multi)
print(divide)

import random
n=random.random()
print(n)

n1=random.random()
print(n1)

p=random.randint(10, 20)
print(p)

k=random.sample((10,60), 2)
print(k)

def kilometer(unit):

    conversion_ratio=0.62137

    kilometer=unit*conversion_ratio

    return kilometer 
print(kilometer(10))

def miles(unit):

    conversion_ratio=0.62137
    miles=unit/conversion_ratio
    return miles
print(miles(10))

def fahrenheit(unit):

    degree_celsius=(unit*1.8)+32
    return degree_celsius
print(fahrenheit(34))

celsius=float(input("enter temperture in degree celsius"))

fahrenheit=(celsius*1.8)+32

print(fahrenheit)

def degree_celssius(unit):

    fahrenheit=(unit/1.8)-32
    return fahrenheit
print(degree_celssius(93.2))

def reverse(string):

    string_1=""
    for i in string:
        string_1=i+string_1
    return string_1
print(reverse("india"))

country="india is best country"
i=country[1:]+country[0]
print(i)

s=country[::1]+country[1:5]
print(s)

c=country[:4:]+country[4]
print(c)

def reverse(s):

    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+(s[0])
s="shri"
print("this is reverse string in",end="")
print(reverse(s))

name="shrikantsharma"
reverse=name[-5:-1:]
print(reverse)

def reverse(string):

    string=string[::-1]
    return string
print(reverse("shrikant"))

def reverse(string):

    string_1="".join(reversed(string))
    return string_1

print(reverse("hello"))

def check_no(a):

    if a>0:
        print("positive number")
    
    elif a<0:

        print("negative number")

    else:
        print("zero number")
a=int(input("enter a number"))
check_no(a)

class check_no(object):

    def __init__(self,a):

        self.a=int(input("enter a number"))

    def method(self):
        if self.a>0:
            print("postive number")

        elif self.a<0:

            print("negative number")

        else:

            print("zero number")
object=check_no(10)
object.method()

number=10

if number%2==0:

    print("even number")
else:
    print("odd number")

year=int(input("plaese enter a year"))

if year%100==0:
    if year%400==0:
        print("leap year")

    else:
        print("not leap year")
else:
    if year%4==0:
        print("leap year")
    else:
        print("not leap year")

list=[1,2,3,4,5,6,78]
print("original list",list)

first=list[0]
list[0]=list[6]
list[6]=first
second=list[1]
list[1]=list[5]
list[5]=second
third=list[2]
list[2]=list[4]
list[4]=third
print(list)

list=[1,2,3,4,5,6,7,8,9,10,19]
size=len(list)
half=int(size/2)

for i in range(half):
    temp=list[i]
    list[i]=list[size-i-1]
    list[size-i-1]=temp

print(list)

list=[]
size=int(input("enter a size of list"))
for i in range(size):
    number=int(input("enter a number"))
    list.append(number)
half=int(size/2)
print("this is original list",list)
for j in range(half):
    first=list[j]
    list[j]=list[size-j-1]
    list[size-j-1]=first

print("reverse list",list)

number=int(input("enter a number"))#11
factor=0
i=1

while i<=number:

    if number%i==0:
        factor=factor+1
    i=i+1
if factor==2:
    print(" this is prime number")
else:
    print("this is not a prime number")

def prime(number):#11
    factor=0

    for i in range(1,number+1):

        if number%i==0:
            factor=factor+1

    if factor==2:

        return 0 #false
    else:
        return 1 #true
number=int(input("enter a number"))
obj=prime(number)

if obj==0:

    print("prime number")
else:
    print("not a prime number")

def reverse(string):

    str_1=""

    for i in string:

        str_1=i+str_1
    print(str_1)
reverse("ajay")

list=[1,2,3,4,5]
reverse=list[0]
list[0]=list[4]
list[4]=reverse

print(list)

list=[1,2,3,4,5,6,7,8,9,10]

size=len(list)
half=int(size/2)

for i in range(half):

    reverse=list[i]
    list[i]=list[size-i-1]
    list[size-i-1]=reverse

print(list)

leap_year=int(input("enter a year"))

if leap_year%100==0:
    if leap_year%400==0:

        print("this year leap year")
    else:
        print("year is not a leap year")

else:
    if leap_year%4==0:
        print("this year leap year")
    else:
        print("year is not a leap year")

number=int(input("enter a number")) #37
count=0

for i in range(1,number+1):

    if number%i==0:
        count=count+1
if count==2:

    print("this is prime number")

else:

    print("this is not a prime number")

number=23
factor=0
i=1

while i<=number:

    if number%i==0:

        factor+=1

    i+=1
if factor==2:

    print("prime number")
else:
    print("not a prime number")

lower_value=int(input("enter a lowerrange value"))
upper_value=int(input("enter a upperrange value"))

for value in range(lower_value,upper_value+1):

    factor=0
    for j in range(lower_value,upper_value+1):

        if value%j==0:

            factor+=1
if factor==2:

    print("this is prime number",j)
else:

    print("this is not prime number")

lower=20
upper=30

for number in range(lower,upper+1):

    if number>1:

        for i in range(2,number):

            if number%i==0:
                break
        else:
            print(number)

number=int(input("enter a number"))

factorial=1

while number>0:

    factorial=factorial*number
    number=number-1
print("factorial in given value",factorial)

array=[1,2,3,4,5,6,]
print(type(array))

a=int(input("enter a number first"))
b=int(input("enter a number second"))
c=int(input("enter a number third"))

perimeter=a+b+c

s=(a+b+c)/2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print(area)
list=[1,2,3,4,5,6,7]

first=list[0]
list[0]=list[6]
list[6]=first

print(list)
kilometer=int(input("enter a value of unit in kilometer"))
miles=int(input("enter a value of unit in miles"))

conversion_ratio=0.62136

kilometer=miles/0.62136
miles=kilometer*0.62136

print("this is kilometer",kilometer)
print("this is miles",miles)

def fahrenheit(unit):

    celcius=(unit-32)/1.8
    return celcius

print(fahrenheit(93.2))
number=int(input("enter a number"))

if number>0:
    print("postive number")
elif number<0:
    print("negative number")
else:
    print("zero number")

def even_odd(number):

    if number%2==0:

        print("this number is even number")
    else:
        print("this is odd number")
even_odd(13)

class even_odd():

    def __init__(self,a):

        self.a=a

    def check(self):

        if self.a%2==0:
            print("even number class")
        else: 
            print("odd number class")
object=even_odd(15)
object.check()
a=1.23
b=int(a)
print(b)

def leap_year(year):
    if year%100==0:
        if year%400==0:
            print("function leap year")
        else:
            print("functio not leap year")

    else:
        if year%4==0:
            print("function leap year")
        else:
            print("function not leap year")

year=int(input("check if this year in leap or not"))
leap_year(year)

number=int(input("enter a number check if prime or not"))
factor=0
i=1

while number>=i:

    if number%i==0:

        factor+=1
    i=i+1
if factor==2:
    print("this number is prime number")
else:
    print("this is not a prime number")

def prime(number):

    for i in range(1,number+1):

        if number%i==0:
            factor=factor+1
if (factor==2):
    print("this prime number")
else:
    print("this is not a prime number")
prime(13)

def prime(number):#13

    if number>1:

        for i in range(2,int(number/2)+1):
            if number%i==0:
                print("not a prime number",number)
                break
        else:
            print("this is prime number",number)
    else:
        print("not a prime number",number)
number=int(input("enter a number check prime or not"))
prime(number)

number=int(input("enter a number"))
factorial=1
if number<0:

    print("factorial is not a negative number")

elif number==0:

    print("this is factorial number in 0 and 1 equal")

else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("this number factorial is",factorial)

number=int(input("enter a number check factorial"))

factorial=1
while number>0:
    factorial=factorial*number
    number=number-1
print("this is factorial value",factorial)
"""
li=[1,2,3,4,5,6]
li.insert(7,"shri")
print(li)

number=int(input("enter a number"))

for i in range(1,11):
    table=number*i
    print(table)

def multipication(num):

    for i in range(1,11):

        table=num*i
        print(table)
multipication(3)


    

    





















    

    