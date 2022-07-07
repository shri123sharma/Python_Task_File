"""
number=int(input("enter a number"))
copy=number
rev=0 #1,12,121,1221

while number>0: #122
    rem=number%10 #1 #2 #2 #1
    rev=rev*10+rem
    number=number//10 #1221//10 #122
print(rev)

if copy==rev:
    print("this is palindrome")
else:
    print("this is not palindrome")

list=[1,34,7,7,7,6433,4,6,7,8]
list_1=[]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            list[j],list[i]=list[i],list[j]
print(list)
#for i in list.pop():
a=list[::-1]
print(a)

import turtle
pen=turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(130)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

heart()
pen.ht()

list=[1,2,3,4,5,6,7,8,9,10]
max=list[0]

for i in list:
    if i>max:
        max=i

print(max)

list=[1,2,3,4,5,6,77,-3]

min=list[0]

for i in list:
    if i<max:
        max=i
print(max)

list=[1,4,7,9,2,4,6,8,11,14,17,18,13]
#third largest value and print it

for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]

print(list[::-1])
print("decending order list",list)

print("third largest value",list[2])

number=int(input("enter a number:")) #16461
duplicate=number
rev=0
while number>0:
    rem=number%10
    rev=rev*10+rem
    number=number//10
if duplicate==rev:
    print("this is palindrome number")
else:
    print("this not palindrome")

number=int(input("enter a number"))
factor=0
i=1
while i<=number:

    if number%i==0:
        factor=factor+1
    i=i+1
if factor==2:
    print("this is prime number")
else:
    print("this is not a prime nummber")

number=int(input("enter a number:"))
factor=0

for i in range(1,number+1):
    if number%i==0:
        factor=factor+1

if factor==2:
    print("prime number")
else:
    print("not a prime number")

number=int(input("enter a number in factorial"))
fac=1
if number<0:
    print("factorial in not allow negative")
elif number==0:
    print("factorial number in 0 is equal to 1")
else:
    for i in range(1,number+1):
        fac=fac*i
    print("this is factorial",fac)

number=int(input("enter a number in factorial"))
fac=1

while number>0:
    fac=fac*number
    number=number-1
print(fac)

number=int(input("enter a number"))
multi=1

for i in range(1,11):

    multi=number*i
    print(multi)

number=int(input("enter a number"))
first=0
second=1
count=0

for i in range(1,number+1):
    first=second
    second=count
    count=first+second
    print(count)

number=int(input("enter a number is armstrong")) #407
duplicate=number
sum=0

while duplicate>0:
    rem=duplicate%10
    sum=sum+(rem**3)
    duplicate=duplicate//10
print(sum)
if sum==number:
    print("this is armstrong ")
else:
    print("not armstrong number")
"""




    






