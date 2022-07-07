"""
from array import*
a=array("i",[1,2,3,4,5,6])
print(type(a))
print(a)

b=array("i",[1,2,3,4,5,6])
print(b[0])
print(type(b))
print(b)

c=array("i",["shri","sharma","arun","ajay"])
print(type(c))
print(c)
c[0]="shrikant"
print(c)

number=int(input("enter a number fibonacci"))
first=0
second=1
third=0

while third<=number:
    first=second #1
    second=third #0
    third=first+second #1+#0

    print(third)

number=int(input("enter a number"))
first=0
second=1
count=0

for i in range(1,number+1):
    first=second
    second=count
    count=first+second

    print(count)

number=int(input("enter a number armstrong"))#153
orginal=number
sum=0

while number>0:
    sum=sum+(number%10)*(number%10)*(number%10)
    number=number//10
print(sum)
if orginal==sum:
    print("armstrong number")
else:
    print("not armstrong number")

number=152 #1+49+125=175
length=0

sum=0
while number!=0:
    length=length+1
    number=number//10
   
print(length)

orginal=number


while number!=0:
    rem=orginal%10
    sum=sum+rem**length
    orginal=orginal//10

if orginal==sum:
    print("this is",sum)

string="shrikant.sharma"
dict={}
for i in string:
    key=dict.keys()
    if i in key:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)

str_1="sh"

if len(str_1)<2:

    print("")
    str_1=str_1[0:2]+str_1[-2:]
    print(str_1)
str="shrikant"
l=len(str)

for i in str:
    if str[-2]=="$":
        print(str)

list=[1,2,3,4,5,6,7]
max=list[0]
for i in list:
    if i>max:
        max=i
print(i)

list=[-1,2,3,4,5,6,6,7,7]
min=list[0]
for i in list:
    if i<min:
        min=i
print(min)           
print(min)

number=int(input("enter a number in given value"))
length=0
duplicate=number
sum=0

while (duplicate!=0):
    duplicate=duplicate//10
    length=length+1
 #print(length)
#len=number

duplicate=number

while (duplicate!=0):
    rem=duplicate%10
    sum=sum+(rem**length)
    duplicate=duplicate//10
if(sum==number):
    print("aaa")
else:
    print("bbb")

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

number=5
fac=1
for i in range(1,number+1):
    fac=fac*i
print(fac)

number=int(input("enter a number"))
duplicate=number
length=0
while (duplicate!=0):
    number=number//10
    length=length+1

duplicate=number
sum=0

#len=length
while (duplicate>0):
    rem=duplicate%10
    sum=sum+rem**length
    duplicate=duplicate//10
    length=length-1
    print(sum)
if (sum==number):
    print("this is disarinum number")
else:
    print("this is not disarinum number")

def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
num = 175;    
rem = sum = 0;    
len = calculateLength(num); 
print(len)   
     
#Makes a copy of the original number num    
n = num;    
     
#Calculates the sum of digits powered with their respective position    
while(num > 0):    
    rem = num%10;    
    sum = sum + int(rem**len);    
    num = num//10;    
    len = len - 1;    
     
#Checks whether the sum is equal to the number itself    
if(sum == n):    
    print(str(n) + " is a disarium number");    
else:    
    print(str(n) + " is not a disarium number");

n=int(input("enter a number"))
length=0
while n!=0:
    length=length+1
    n=n//10    

print(length)

num=175
rem=sum=0
len=length

n=num

while num>0:
    rem=num%10
    sum=sum+(rem**len)
    num=num//10
    len=len-1
print(sum)
"""









    




                
