"""
def demo():
    "just print the stement"
    print("welcome")

demo()

def demo_1():
    "addding the two value"
    a=10
    b=20
    c=a+b

    print(c)
demo_1()

def demo_2():
    "substration both value"
    num_1=32323232
    num_2=3232323232

    c=num_1-num_2
    return c
print(demo_2())

def demo_3():
    "eligiable of vote"
    p_1=int(input("enter a age1"))
    p5_2=int(input("enter a age2"))
    p_3=int(input("enter a age3"))

    if p_1>p_2 and p_1>p_3:
        print("first person in greater",p_1)
        if p_1>=18:
            print("first person in age in greater and vote")
    
    elif p_2>p_3 and p_2>p_1:
        print("second person in greater")
        if p_2>=18:
            print("eligiable of vote")
    else:
        print("third is greater")
        if p_3>=18:
            print("eligiable of vote only third person")
demo_3()

def multiply():
    "both are value in multiply"
    a=int(input("enter a  value1"))
    b=int(input("enter a value2"))

    c=a*b
    return c
print(multiply())

from typing import Concatenate
from django.db import connection


def index(a,b):
    "add the both argument"
    return a+b
c=int(input("enter a number 1:"))
d=int(input("enter a number 2;"))

print(index(c,d))

def number(x):
    "even and odd number check"
    if x%2==0:
        return("even")
    else:
        return("odd")

print(number(129))

def leapyear():
    year=int(input("enter a year:"))
    if year%100==0:
        if year%400==0:
            print("this year is leap year")
        else:
            print("not leap year")
    else:
        if year%4==0:
            print("this year is leap year")
        else:
            print("not leap year")

leapyear()

def A_operator():
    str_1=str(input("write a message"))
    str_2=str(input("write a second message"))

    concatenate=str_1+str_2
    print(concatenate)
    repitation=str_1*3+str_2*3
    print(repitation)
A_operator()

def list():
    list_1=[1,2,3,4,5,6,7,7,8,9]
    
    for i in list_1:
        list_2=[]
        if i==6:
            list_2.append(i)
            continue
    
print("one item in add to empty list")
list()

def add(a,b):
    c=1222
    d=32323

    print(a+b+c+d)

add(10,20)  

def list(list_1,list_2):

    print(list_1+list_2)
list([10,20,30,40,"indore","india",True,False],[1,2,3,4,5,6,6,54545,4,5,4545,54])

def msg(write="this world"):
    print("hello"+write)

msg("welcome to world")
msg()

def write(name,msg="happy new year"):
    print(name+msg)

write("shrikant")
write("shubham","happy birthday")

def demo(str_1):
    str_2=str_1[0]
    return str_2

print(demo("shrikant"))

def demo_1(str_1):
    str_2=str_1.upper()
    return str_2

print(demo_1("sharma"))

def demo_2(num):
    square=num**2
    cube=num**3

    return (square,cube)
print(demo_2(10))

def demo_3(name="shrikant",age=24):
    return("ajay",25)

print(demo_3())

def demo_4(fname):
    print(fname+"welocome to this world")

demo_4("shri")
demo_4("ajay")

def demo_5(fname="sourabh"):
    print(fname+"hello")
demo_5()
demo_5("shrikant")
demo_5("ajay")

def country(city="indore"):

    print("im form this"+city)

country("bhopal")
country("jabalpur")
country()
country("jaipur")

def index_1(firstname,lastname):
    return (firstname+lastname)

print(index_1(firstname="geeks",lastname="practise"))
print(index_1(lastname="system",firstname="os"))

def func(name):
    msg=name+"welcome"
    return msg

name=input("enter a name?")
print(func(name))

def simple_interest(p,r,t):
    return(p*t*r/100)
p=int(input("enter a principal value"))
r=int(input("enter a rate of amount"))
t=int(input("enter a time duration"))

print(simple_interest(p,r,t))

def add(a,b):
    return a+b
print(add(10,23232323))

def add(a,b,c,d):
    return a+b+c+d
a=int(input("number1"))
b=int(input("number2"))
c=int(input("number3"))
d=int(input("number4"))

print(add(a,b,c,d))

def substract(*args):
    for i in args:
        print(i)
substract("hello","this","is","my","world")

def list_1(*args):
    for i in args:
        if i==10:
            break
        print(i)
list_1(100,90,80,70,60,10,40,30,20)

y=20
def add():
    x=10

    return x+y
print(add())

def greet(name,age):
    "both are concetenate"
    return name,age

print(greet("shrikant",24))

def greet_1(name,msg="welcome to my company"):
    "default argument"
    return ("hello"+name+""+msg)

print(greet_1("risabh"))
print(greet_1("ajay","how are you"))

def greet_2(*name1):
    "arbitary object"
    print(name1)

greet_2("shubham","risabh","sourabh")

def greet():
    a=10
    b=20
    return a+b

print(greet_1())

def greet_1():
    a=100
    b=20
    return a-b

print(greet())

def factorial(n):

    "this is recursive function call again again"

    if n==1:
        return 1
    else:
        return(n*factorial(n-1))

print(factorial(5))

def greet(x,y):

    var=2*(x+y)
    return var

print(greet(100,200))
a=3
var1=greet(a,2+a)
print(var1)

var2=greet(1000,2000)
print(var2)

def fahrenheit(celcius):
    "convert the fahrenheit to celcius"
    return(celcius*9/5+32)

print(fahrenheit(100))

def demo(list_1=[1,2,3,4,5]):
    "append the value in string format"
    list_1.append("shri")
    return list_1

print(demo())
print(demo())
print(demo())
print(demo.__defaults__[0])

def spanner(bag=None):
    if bag is None:
        bag=[]
        bag.append("spam")
        print(bag)

for i in range(5):
    print(spanner())

print(spanner.__defaults__)

def string_1():
    "this is docstring"
    a=200
    b=300
    return a+b

print(string_1.__doc__)
print(string_1())

def no_return(x,y):
    x+y

var=no_return(10,20)
print(var)

def no_return(x,y):
    c=x+y
    return c

var=no_return(10,20)
print(var)

def fibonaccni():
    x=int(input("enter a number"))
    if x<0:
        return 1
    old,new=0,1

    while True:
        if new<x:
            old,new=new,old+new
        else:
            if new==x:
                new=old+new
                return(old,new)
print(fibonaccni())

def local():
    name="shrikant"
    last_name="sharma"
    return name+last_name

print(local())

def local_1():
    name="risabh"
    n=name.capitalize()
    print(n)

    age="21212121"
    a=age.endswith("1")
    print(a)

print(local_1())

def age():
    user_1=int(input("enter a age1:"))
    user_2=int(input("enter a age2:"))
    user_3=int(input("enter a age3:"))

    if user_1>user_2 and user_1>user_3:
        print("first person is",user_1)

    elif user_2>user_3 and user_2>user_1:
        print("second person is",user_2)
    else:
        print("third person is",user_3)

age()

def aribitary(name,*value):
    name=111
    return (name+sum(value))

print(aribitary(100,200,300,400))

x=abs(3+5j)
print(x)

y=abs(-12.00)
print(y)

z=abs(-3323232)
print(z)

list_1=[2121212,2,21,2,3,3,4,23233,3,3,11313,131,3131,313,131,31,1,313,]
x=all(list_1)
print(x)

string_1=ascii("my name is sh\/`r`i/k\an@t")
print(string_1)

list_1=ascii([1,2,3,45,6,7,7,8,8,9,9])
print(list_1)

bool_1=bool("shrikant")
print(bool_1)

fruit=("banana","cherry","mango","pinnapple",1)
x=enumerate(fruit)
print(x)

x=20
y=30
print(id(x))
print(id(y))

def demo(city):
    city=city+["indore","bhopal",""]
    print(city)
location=["jaipur","bilaspur"]
demo(location)

def demo_1(city):
    print(city)
    city+=["india","nepal","srilanka"]
    print(city)
location=["america","japan","russia","britian"]
demo(location)

def demo_2(*x):
    print(x)
demo_2([10,20,30,40,40,50,50])

def demo_3(fruits,*item):
    print(fruits,item)
demo_3("mango")
demo_3("mango","daal","chawal","arahar",)

def demo_4(x,y,z):
    print(x,y,z)

p=(10,20,30)
demo_4(*p)

def index(**args):
    print(args)
index()

def index_1(**args):
    print(args)

index_1(name="shrikant",age=24,location="indore",country="india")

import numpy
a=[1,2,33,4,4]
numpy.mean(a)
print(a)

from glob import glob


a=10
b=20
def myfun():
    c=10
    d=20
    print(a+b)
    print(c+d)
myfun()
print("global variable",a*b)

name="shrikant"
age="24"
def myfun_1():
    global name
    global age
    print(name+age)

myfun_1()

i=20
def myfun_2():
    i=20
    i=i+1
    print(i)
myfun_2()

age_1=int(input("enter a number1"))
age_2=int(input("enter a number2"))
age_3=int(input("enter a number3"))

def greater():
    if age_1>age_2 and age_1>age_3:
        print("first person is greater",age_1)

    elif age_2>age_3 and age_2>age_1:
        print("second is greater",age_2)
    else:
        print("third person is greater",age_3)

greater()

a=10
b=20
def add():
    print(a)
    print(b)
    print(a+b)

add()
print(a)
print(b)

def substration(e):
    c=100
    d=50
    print(c)
    print(d)
    print(c-d-e)
substration(1000)

from re import I


def add():

    a=100
    b=200

    return a+b
print(add()) 

def add(x,y):

    return x+y

print(add(10,20))

a=int(input("enter a number1"))
b=int(input("enter a number2"))
c=int(input("enter a number3"))

def greater():

    if a>b and a>c:

        print("a is greater",a)
    elif b>c and b>a:

        print("b is greater",b)
    else:

        print("c is greater",c)
greater()

def message(person,msg='happy new year'):

    "function message"

    return msg,person
print(message('risabh'))
print(message("ajay"))
print(message("arun"))
print(message("sourabh"))
print(message("arvind"))

def iterate(*argv):

    for i in argv:

        print(i)
iterate("shrikant","ajay","arun","sarika","risabh")

def index(**kwargs):

    for i in kwargs:

        print(i)

index(first='shrikant',second='ajay',third='arun')

def add(**kwargs):

    "this is docstring in after a function called "

    for key,value in kwargs.items():

        print(key,value)
print(add.__doc__)
print(add(first='hello',second="hii",third='niceone'))

list=[]
for i in range(0,11):

    list.append(i*15)

print(list)

n=int(input("enter a number"))
i=0

while i<n:

    i=i*15

    print(i)

for i in range(1,11):

    a=i*2

    print(a)

n=10
i=1

while i<10:
    
    n=i*15
    print(n)
    i+=1   

from ast import Yield


def demo():

    a=100
    b=200
    c=a+b
    return c
print(demo())

def evenodd(x):

    if x%2==0:

        print("this even number")
    else:
        print("this is odd number")
evenodd(11)

def demo_1(a,b=100):

    "this is docstring"

    c=a+b
    return c
print(demo_1(1000))

def demo_2(firstname,lastname):
    "keyword argument"

    name=firstname+lastname
    return name
print(demo_2(lastname='sharma',firstname='shrikant'))

def demo_3(*argvs):

    "docstring in non keyword argument"

    for i in argvs:

        print(i)
demo_3("hello",'this is me','how are you')

def evenodd(x):

    "even and odd number check"

    if x%2==0:
        print("this is even number")
    else:

        print("this is odd number")
evenodd(100) 

def square(num):

    "this is square value "

    return num**2

print(square(100))

def cube(x):return x*x*x
print(cube(3))

# cube= lambda x : return x*x*x
# print(cube(2))

def add():

    a=100
    b=200

    def multi():

        return a*b

    print(multi())
add()

def demo(a,b,c,d):

    "four parameters"

    return a,b,c,d

print(demo('shrikant','sarika','risabh','deepika',))

def demo_1(*args):

    "multiple argument"

    return args

print(demo_1('sarika','shrikant','risabh','deepika','gaytri','ajay','sourabh'))

def item(product,*args):

    "multiple argument"

    print('first argument',product)

    for i in args:

        print("other argument",i)

item("computer",'mouse','keyboard','datacable')

def dict(**kwargs):

    "this is multiple argument"

    for key,value in kwargs.items():

        print(key,value)

dict(first='shrikant',second='sharma')

def add(a,b):

    yield a
    yield b

    for i in add(a,b):
        print(i)
result=(add(10,20))
print(type(result))

def square_num():
    i=1

    while True:

        yield i*i
        i=i+1
for i in square_num():

    if i>100:
        break
    print(i)

def center(a,b,c):

    # a=int(input("enter a num1"))
    # b=int(input("enter a num2"))
    # c=int(input("enter a num3"))

    if a>b and a>c:

        yield a
    elif b>c and b>a:

        yield b
    else:
        yield c

result=center(10,20,34)
print(type(result))
print(next(result))
print(next(result))

from re import A
def square():

    yield 1
    yield 2
    yield 3

for i in square():

    print(i)

def value():

    yield 1
    yield "shrikant"
    yield [1,2,3,4,5,6,7]

    x=value()

    print(x.next())
    print(x.next())
    print(x.next())

def fib(limit):

    a,b=0,1

    while a<limit:

        yield a
        a,b=b,a+b

x=fib(5)
print(type(x))

print(next(x))
print(x.next())
print(x.next())
print(x.next())
print(x.next())
"""
s="this is python langauage"

string=lambda s:print(s)
print(string)