"""
list=[1,4,7,8,9,6,7,9,4,32,4,6,7]
for i in range(len(list)): #1
    for j in range(i+1,len(list)): #2
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]

print(list)

def sort(list):#[1,4,7]
    for i in range(len(list)): #length of item=2
        for j in range(i+1,len(list)): #i=0
            if list[i]<list[j]: #i=0<j=1
                list[i],list[j]=list[j],list[i]
    return list

print(sort([-1,-3,7,-2,8,-9,4]))

number=int(input("enter a number "))
if number>0:
    print("postive")
elif number<0:
    print("negative")
else:
    print("zero")

leap=int(input("enter a leap"))
if leap%100==0:
    if leap%400==0:
        print("this is leap year")
    else:
        print("this is not leap year")
else:
    if leap%4==0:
        print("this is leap year")
    else:
        print("this is not leap year")

prime=int(input("enter a number"))
factor=0

for i in range(1,prime+1):
    if prime%i==0:
        factor=factor+1
if factor==2:
    print("this is prime number")
else:
    print("this is not a prime number")

prime=int(input("enter a number given prime"))
factor=0
i=1
while i<=prime:
    if prime%i==0:
        factor=factor+1
    i=i+1
if factor==2:
    print("prime number")
else:
    print("not a prime number")

first=int(input("enter a number 1:"))
second=int(input("enter a number 2:"))
factor=0
for i in range(first,second+1):
   if i>1:
        for j in range(2,i):
           if i%j==0:
               break
        else:
            print(i)

number=int(input("enter a number"))
fac=1

for i in range(1,number+1):
    fac=fac*i
print(fac)

number=int(input("enter a given number"))
fac=1
if number<1:
    print("factorial is not a negative number")

elif number==0:
    print("factorial number 0 is equal to 1")

else:
    for i in range(1,number+1):
        fac=fac*i
    print(fac)

number=int(input("enter a given fibonacci series"))
first=0
second=1
third=0

for i in range(number):
    first=second
    second=third
    third=first+second
    print(third)

number=int(input("enter a number in while type"))
first=0
second=1
count=0

while count<=number:
    first=second
    second=count
    count=first+second
    print(count)

number=int(input("enter a number armstrong number")) #153
length=0
copy=number
sum=0
while copy!=0:
    length=length+1
    number=number//10
print(length)

while copy!=0:
    rem=copy%10
    sum=sum+(rem**length)
    copy=copy//10
print(sum)

number=int(input("enter a number armstrong check"))
original=number
len=0
sum=0
while original!=0:
    len=len+1
    original=original//10
print("this is length of number",len)

original=number

while (original!=0):
    rem=original%10
    sum=sum+(rem**len)
    original=original//10
print("this is value in add",sum)
if (sum==number):
    print("this is armstrong number")
else:
    print("not armstrong number")

number=int(input("enter a number"))
copy=number
length=0
sum=0

while copy!=0:
    length=length+1
    copy=copy//10
print(length)
copy=number
while copy!=0:
    rem=copy%10 #3
    sum=sum+(rem**length)
    copy=copy//10
print(sum)

for i in range(1,3):
    for j in range(1,5):
        print(j)
    print(i)

row=5
i=1
for i in range(row):
    for j in range(1,row-i):
        print(i,end="")
    print("")

list=[1,4,7,9,4,2,6,0,1]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
print(list)
list=list[-2]
print(list)
  
#user defined tuple create  
tuple=(1,2,3,4,5,"shri","sharma",True,False,1.00,2.00)
print(tuple)
print(type(tuple))
#inbuilt type tuple  
# name=tuple("shrikant","sharma","24","indore","mp")
# print(name)
# print(type(name))

number=10,20,30,40,50
print(number)
print(type(number))
#empty tuple
tuple_1=()
print(tuple_1)
print(type(tuple_1))

tuple_1="shrikant"
print(type(tuple_1))
tuple_2="shrikant",
print(type(tuple_2))

tuple=(10,20,30,40,50)
sum=0
for i in tuple:
    sum=sum+i
    sum=sum**2
print(sum)

tuple=(1,4,7,3,4,678,9,10,2,56,7,7)
length=len(tuple)
print("orginal length of tuple",length)

for i in range(0,length):
    for j in range(i+1,length):
        if tuple[i]<tuple[j]:
            tuple[i],tuple[j]=tuple[j],tuple[i]
print(tuple)

tuple=(1,2,3,4,5,6,7,88,9,0,0)
tuple_1=()

a=tuple.count(0)
print(a)

b=tuple.index(88)
print(b)

def tuple(tuple_1):

    print(tuple_1)

tuple(1,2,3,"shrikant","indore",1.00,True,False,1+2j)

tuple=(1,2,3,4,5,6,6,)
print("without item tuple",tuple)

tuple_1=(10,20,30,40,50,60)
print(tuple+tuple_1)

tuple=tuple+(7,)
print(tuple)

tuple=(100,200,300,400,500,600)
tuple_1=tuple[:3]+(250,)+tuple[:3]
print(tuple_1)

tuple=(1,2,3,4,5,6,7)
tuple_1=(2,4,8,9,10,13)

tuple_2=tuple+tuple_1
tuple_2=set(tuple_2)
print(tuple_2)

tuple=("1","2","3","6","8","9","3","10.13","15","17")
string=""
for i in tuple:
    string=string+i
print(string)

tuple=(1,3,1,10,12,15,17,73,82,495,)
print(tuple)

tuple_1=tuple[3]
print(tuple_1)

tuple_2=tuple[-4]
print(tuple_2)

tuple=(1,2,3,4,5,6,"india","america","russia")
tuple=list(tuple)
for i in tuple:
    if i[0]=="ukraine":
        print(i)

def code():

    pass
print(code)

_a=sara
print(a)
print(type(a))
"""
def func(number):
    for i in number:

        pass
        if i==
    