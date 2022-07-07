"""
list=[1,3,5,8,0]
sum=0

for i in list:
    sum=sum+i
print(sum)

lst=["abc","xyz","aba","1221"]
count=0
# length=len(lst)

for i in lst:
    if len(i)>1 and i[0]==i[-1]:
        count=count+1
print(count)

list=[1,2,3,3,4,4,6,8,9,11,1,13]
list_1=set(list)
print(list_1)

list=[1,2,3,4,5,6,7,1,2,3,4,5,6,7,8]
dup_item=set()
unique_item=[]

for i in list:
    if i not in dup_item:
        unique_item.append(i)
        dup_item.add(i)
print(dup_item)

list=[1,2,3]
if list==[]:
    print("empty")
else:
    print("not empty")

def long_word(number,string):
    word_list=[]
    txt=string.split()

    for i in txt:
        if len(i)>number:
            word_list.append(i)
    return word_list
print(long_word(3, 'my name is shrikat sharma'))

    
# string="this is my laptop"
# txt=string.split()
# print(txt)


list1=[1,2,3,4,5,6,7,8]
list2=[1,11,12,14]

list1.extend(list2)
for i in list1:
    if list1[i]==list[i]:
        print(i)
    print(i)

year=int(input("enter a number this year"))
if year%100==0:
    if year%400==0:
        print("this is leap year")
    else:
        print("this is not leap year")
else:
    if year%4==0:
        print("this is leap year")
    else:
        print("this not a leap year")

number=int(input("enter a number"))
if number%2==0:
    print("even number")
else:
    print("odd number")

prime=int(input("enter a prime number"))
factor=0

for i in range(1,prime+1):
    if prime%i==0:
        factor=factor+1
        print("this is prime number")

print(factor)

number=int(input("enter a number is prime or not"))
factor=0
if number<0:
    print("prime number in not count negative num")

elif number==0:
    print("prime number is upper with 0")
else:
    factor=0
    for i in range(1,number+1):
        if number%i==0:
            factor=factor+1
if factor==2:
    print("this is prime number")
else:
    print("not a prime number")

number=int(input("enter a number"))
for i in range(2,number):
     if number%i==0:
         print("not a prime number")
         break
     else:
         print("prime number")
         break
number=int(input("enter a number prime in while"))
factor=0

while number<=0:
    if number%i==0:
        factor=factor+1
if factor==2:
    print("prime number")
else:
    print("not prime number")

number=int(input("enter a factorial value"))
if number<0:
    print("factorial is not define negative result")
elif number==0:
    print("factorial value is 0 and 1 are same")
else:
    fac=1
    for i in range(1,number+1):
        fac=fac*i
print("this is factorial value",fac)

number=int(input("enter a number"))
fac=1

while number>0:
    fac=number*fac
    number=number-1
print(fac)

number=int(input("enter a number multipication table"))
multi=0
for i in range(1,11):
    multi=number*i
    print(multi) 

number=int(input("enter a number")) #1221
rev=0

while number>0:
    rem=number%10
    rev=rev*10+rem
    number=number//10

print("reverse in number",rev)

number=int(input("enter a number1"))
rev=0
length=0
length=length+1
number=number//10

print("total input number length",length)

list=[1,2,45,7,8,9,0,34,5,]
max=list[0]

for i in list:
    if i>max:
        max=i
print(max)

def min(list):
    min=list[0]

    for i in list:
        if i<min:
            min=i
    return min
print(min([1,4,5,6,8,9,-1]))

list=[1,3,6,9,11,4,33,2,4,6,7,56,7778,9,7,766,6,]
length=len(list)
print("list length is",length)

for i in range(0,length):
    for j in range(i+1,length):
        if list[i]<list[j]:
            list[i],list[j]=list[j],list[i]
print("this is decending order list",list)
list_1=list[::-1]
print(list_1)

number=int(input("enter a number"))
first=0
second=1
count=0

for i in range(0,10):
    first=second
    second=count
    count=first+second

    print(count)

number=int(input("enter a number")) #4
for i in range(2,a):
    if number%i==0:
        print("this is not a prime number")
        break
    else:
        print("this number is prime number")

list=[1,2,34,5,7,88,90,0]
sum=0
for i in list:
    sum=sum+i
print(sum)

list=[1,2,4,6,8]
multi=1

for i in list:
    multi=multi*i
print(multi)

# 407 
number=int(input("enter a number armstrong"))
duplicate=number
length=0
while duplicate!=0:
    duplicate=duplicate//10
    length=length+1

sum=0
duplicate=number
while duplicate!=0:
    rem=duplicate%10
    sum=sum+rem**length
    duplicate=duplicate//10
print("return armstrong value",sum)

if number==sum:
    print("this is armstrong value")
else:
    print("this is not armstrong value")

row=5
for i in range(1,row+1):
    for j in range(i,row+1):
        print(j,end="")
    print(" ")

dict={"peter":0,"franka":0,"eva":0}

while True:
    name=input("name")
    if name=="":
        break
    dict[name]+=1
    print(dict[name])
print(dict)

list=[[0,1,1,1],[0,0,0,1],[1,1,0,0]]
list_1=[]
for i in list:
    p=i[::-1]
    list_1.append(p)
    print(list_1)

def long_word(n,word):#"this is my world"
    list=[]
    separate=word.split(" ")

    for i in separate:
        if len(i)==n:
            list.append(i)
    return list
print(long_word(3,"how are you im fine and you"))

def common(list1,list2):
    for i in list1:
        for j in list2:
            if [i]==[j]:
                return True
    return False
print(common([1,23,4,5,6,76,7],[10,12,23,14,18,16,19]))
"""
row=3
n=int(input("ENTER"))

for row in range(0,n):
    print(row)
    for col in range(row,n-1):
        print(col)
        if row== 1 and row==n-1:
            print("*",end="")
        print("")
        
        if col==1 and col ==n-1:
            print("*",end=" ")
        print(" ")


