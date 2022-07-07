"""
def list(item):
    sum=0

    for i in item:
        
        sum=sum+i
    
        print(sum)

list([1,2,3,4,5])

class list(object):

    def __init__(self,item):

        self.item=item

    def add(self):
        sum=0
        for i in self.item:
            sum=sum+i
        print(sum)
object=list([10,20,-30,-60])
object.add()

def list(item):
    multi=1
    for i in item:
        multi=multi*i
    print(multi)
list([1,2,3,4,5,6])

list=[1,2,-3,4,10]
max=list[0]
for i in list:
    print(i)
    if i>max:
        max=i
print(max)

list=[434,55,5,6,6,6575,75]
min=list[0]
for i in list:
    if i<min:
        min=i
print(min)

list=["shrs","xyz","sahs",'5555']
count=0
for i in list:
    if len(i)>1 and i[0]==i[-1]:
        count=count+1
print(count)

list=[1,2,3,3,5,3]
repeat=0
for i in list:
    if i==3:
        repeat+=1
    print(repeat)

list=[(1,2),(2,3),(3,3),(4,5),(5,6)]
count=0
for i in list:
    if len(i)>1 and i[0]==i[-1]:
        count=count+1
print(count)

list=[10,3,4,45,55,5,5,454]
sum=0
for i in list:
    sum=sum+i
print(sum)

list=[1,2,43,5,545,5,6,464,4,4545,5,]
multi=1
for i in list:
    multi=multi*i
print(multi)

list=[1,2,2,3424,43,44,4,4,4344,434,3]
max=list[0]
for i in list:
    if i>max:
        max=i
print(max)

list=[21121,21,2,21,212,12,1243,5,67,7,]
min=list[0]
for i in list:
    if i<min:
        min=i
print("list minimum value is",min)

string="shrikant"
str_1=""
for i in string:
    str_1=i+str_1
print(str_1)

list=[1,33,44,4,4,53,34,34,34,34,4,343,3232]
first=list[0]
list[0]=list[12]
list[12]=first
print("replace to first and last items",list)

list=[1,2,3,45,5,464,6,6,56,7,5,757]
length=len(list)
half=int(length/2)
for i in range(half):
    first=list[i]
    list[i]=list[length-i-1]
    list[length-i-1]=first
print(list)

list=[12,3,3,554,545]
list_1=list[::-1]
print(list_1)

num=int(input("enter a number"))
factor=0
for i in range(1,num+1):
    if num%i==0:

        factor=factor+1
if factor==2:

    print("this is prime number")
else:
    print("this is not a prime number")

number=7
factor=0
i=1
while i<=number:
    if number%i==0:
        factor=factor+1

    i=i+1
if (factor==2):
    print("prime number")
else:
    print("not prime number") 

number=int(input("please enter a number"))
fac=1
for i in range(1,number+1):
    fac=fac*i
print("this is factorial value",fac)

number=int(input("which number in add and check factorial"))
fac=1

while number>0:
    fac=fac*number
    number=number-1
print("Now a factorial in given value",fac)

table=int(input("enter a number in given table"))
for i in range(1,11):
    multi=table*i
    print("this is table",multi)

def table(number):

    for i in range(1,11):

        multi=number*i
    return multi
print(table(3))

list=['shrikant','2424','indii','aba','cbc','ada']
length=len(list)
count=0
for i in list:
    if len(i)>1 and i[0]==i[-1]:
        count=count+1
print(count)

number=int(input("enter a number in factorial"))
fac=1
if number<0:
    print("factorial is not a negative number")

elif number==0:

    print("factorial number is 0 and 1 are same")
else:
    for i in range (1,number+1):
        fac=fac*i
    print(fac)

number=int(input("enter a given number"))
first=0
second=1
count=0

for i in range(1,number+1):
    first=second
    second=count
    count=first+second

    print(count)

def fibo(num):
    first=0
    second=1
    count=0

    while count<=num:
        first=second #1
        second=count #0
        count=first+second #0+1=1 #first time loop
        print(count)
fibo(5)

class fibo(object):

    def __init__(self,first,second,count):
        self.first=first
        self.second=second
        self.count=count

    def series(self):
        for i in range(0,11):
            self.first=self.second
            self.second=self.count
            self.count=self.first+self.second

            print(self.count)
object=fibo(0,1,0)
object.series()

list=[1,2,3,4,5,6,]
list_1=[]
for i in list:
    list_1.append(i**i)
print(list_1)

list=[i**i for i in list]
print(list)

dict={i:i**i for i in range(1,11)}
print(dict)

number=int(input("enter a number"))
sum=0
total=0
for i in range(1,number+1):
    sum=sum+i
    total=total+i
print(total)

def natural(number):
    sum=0
    total=0
    for i in range(1,number+1):
        sum=sum+i #1
        total=total+i
    return total
number=int(input("enter a number"))
print(natural(number))

number=int(input("enter a given number"))
first=0
second=1
count=0

for i in range(1,number+1):
    first=second
    second=count
    count=first+second

    print(count)

fun=lambda a,b:a+b
a=fun(10,20)
print(a)

number=int(input("enter a number is given value")) #153

orginal=number
sum=0

while number>0:
    sum=sum+(number%10)*(number%10)*(number%10)
    number=number//10

if orginal==sum:
    print("this is armstrong number")

else:
    print("Not armstrong number")

number=int(input("enter a armstrong number"))
orginal=number
sum=0
while number>0:
    
    sum=sum+(number%10)*(number%10)*(number%10)
    number=number//10
print(sum)
if orginal==sum:
    print("if this value is armstrong")
else:
    print("if not armstorng number")

number=1634
orginal=number
sum=0

while number>0:
    sum=sum+(number%10)*(number%10)*(number%10)*(number%10)
    number=number//10
if orginal==sum:
    print("armstrong number")
else:
    print("not armstrong number")

def arm(number):
    orginal=number
    sum=0
    while number>0:
        sum=sum+(number%10)*(number%10)*(number%10)
        number=number//10
    if orginal==sum:
        print("this value is armstrong num")
    else:
        print("this is not armstrong number")
arm(407)

number=143
sum=0
while number>0:
    sum=sum+(number%10)
    number=number//10
print(sum)

list=[1,2,3,4,5,6,]
sum=0
total=0
for i in list:
    sum=sum+i
print(sum)

first=int(input("enter a number first"))
last=int(input("enter a number last"))

for i in range(first,last+1):
    number=i
    orginal=number
    sum=0
    while number>0:
        sum=sum+(number%10)*(number%10)*(number%10)
        number=number//10
        if number==sum:
            print(number)

number=int(input("enter a number"))
count=0

for i in range(1,number+1):
    if number%i==0:
        count=count+1
if count==2:
    print("this is prime number")
else:
    print("this is not a prime number")

number=int(input("enter a number in given factorial"))
fac=1

while number>0:
    fac=fac*number
    number=number-1
print(fac)

number=int(input("enter a number"))
first=0
second=1
count=0

while number>count:
    first=second
    second=count
    count=first+second
    print(count)

list=[1,2,2,2,23,4,4,5,6,7,77,7,87]
list_1=[]

for i in list:
    if i not in list_1:
        list_1.append(i)
print(list_1)

list_1=[1,2,3,4,4,5,6,7]
list_2=[2,2,2,4,4,4,56,656,23232,]

for i in list_1:
    for j in list_2:
        if i==j:
            print(i,end=",")
list=[1,23,4,5,5,6,7,7,8]
list_1=list*2
print(list_1)

x=lambda a,b:a+b
print(x(30,60))

y=lambda a,b:a**b
print(y(2,5))

z=lambda x,y:x%y
print(z(100,21))

multi=lambda a,b:a*b
print(multi(10,20))

list=[1,2,2,3,3,3,4,4,5,5,6,6,77,8]
lst=list(map(lambda x:x**2 ,list))
print(lst)

list=["1","2","3","4","5","6","6"]
str_1=""
for i in list:
    str_1=str_1+i
print(str_1)

list=[1,2,3,4,5,5,6,6,7]
dict={}
for i in list:
    dict=dict+i
print(dict)

list=["a","b","c","d","e","f"]
x=({i:j for i,j in enumerate(list,100)})
print(x)

tuple=('shri','ajay','arun','vishal')
x=({i:j for i,j in enumerate(tuple,10)})
print(x)
"""


