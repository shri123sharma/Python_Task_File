"""
a=1000
b=200

def fun_1():
    global a
    global b
    
    return a+b
print(fun_1())
print("g;obal is",a+b)

num=int(input("enter a number"))
if num>0:
    print("this value is greater for 0")
elif num<0:
    print("")

list=[3,5,6,7,7,2,1,24,5,6]
min=list[0]
for i in list:
    if i < min:
        min=i
print(min)

list=["hello","world","this","is","india"]
length=len(list)
first=list[0]
list[0]=list[length-1]
list[length-1]=first
print(list)

list=[10,20,30,40,50,60]
length=len(list)
print(length)

list=[1,4,7,9,3]
length=0
# import pdb;pdb.set_trace()
for i in list:
    length+=1
print(length)

a=1000
b=200

if a>b:
    print("first is greater")
else:
    print("second is greater")

a=100
b=20

if a<b:
    print("first is less")
else:
    print("second is less")

n=int(input("enter a number"))
list=[1,2,3,4,5,6,7,7,8]
if n in list:
    print("yes it will exit")
else:
    print("no at item in this list")

list=[100,200,300,400,500,600,700]
length=len(list)
for i in list:
    if i==400:
        print("this value inside a list")
else:
    print("this value not a list")

from tabnanny import check


list=[[1,2,3,4,5,6,],
    [10,20,30,40,50,60],
    [100,200,300,400,500]
     ]

find_item=10
find_item_1=1000

list_1=any(find_item in sublist for sublist in list)
list_2=any(find_item_1 in sublist for sublist in list)

print(list_1)
print(list_2)

list=[[1,20,4,6,7,7,3,2],
    ["hello","world","this"],
    [1.3,32.3,32434.6,65657]]

check_1=20
check_2="this"
check_3=1.3

list_1=check_1 in(list in sublist for sublist in list)
print(list_1)

from collections import Counter

x=Counter("hello world this is india")
count=0
for i in x.elements():
    if i==x:
        count+=1
    print(i,end="")

x=Counter([1,2,3,4,5,6,78,2])
count=0
for i in x.elements():
    print(i,end=",")

list=[1,2,3,4,5,6,7,7,8,9]
list_1=[]
for i in reversed(list):
    list_1.append(i)
    
print(list_1)
list_2=list[::-1]
print(list_1)

def fun_1(list):
    sum=0
    avg=len(list)
    for i in list:
        sum=i+sum
        avg_1=sum/avg
    return avg_1
print(fun_1([1,2,3,4,5,6,6]))

def fun_2():
    list=[10,20,30,40,50,60,70]
    sum=0

    for i in list:
        sum=i+sum
        if sum>=200:
            print(True)
        else:
            print(False)
fun_2()

def fun_3():
    list=[100,200,300,400,500,600]
    str=""
    for i in list:
        str=i+str
        print(str)
fun_3()

def fun_4(list):
    list=[[1,2],[3,4],[5,7]]
    return ["".join(str(j) for j in (i)) for i in list]
print(fun_4(list))

def fun_5(list):
    list=[[100,200],[300,400],[500,600]]

    for i in list:
        for j in i:
            k="".join(str(j))
        print(k)
fun_5(list)

from collections import Counter

list=[[1,2,3],[3,6,7],[8,10,22]]
s=str(list)
print(s)

f=dict(Counter(j for i in list for j in set(i)))
print(f)

list=[10,2,3,4,5,3,6,7,8,9,3,10,13,15]
x=3
count=0
for i in list:
    # for j in list:
        if i==x:
            count+=1
print(count)

str="shrikantsharma"
dict={}
for i in str:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)    

from collections import Counter
str_1="hello india"

count=Counter(str_1)
print(count)

str_1="hello world welcome"

dict={}

res={i:str_1.count(i) for i in set(str_1)}
print(res)

list=[1,2,3,4,5,6,10]
multi=1

for i in list:
    multi=multi*i
    print(multi)

list=[212,23,4,45,56,68,8,45,8,9]
min=list[0]

for i in list:
    if i<min:
        min=i
        
print(min)

list=[10,20,3,12,19,18,17]
max=list[0]

for i in range(0,len(list)):
    if list[i]>max:
        max=list[i]

list=[1,2,3,4]
list_1=["hello","india","hello","world"]
print(id(list))
print(id(list_1))

del list[1]
del list[-1]
print(list)
del list_1[1]
del list_1[-1]
print(list_1)


# list=[100,200,300,400,500,600,700,100,200,]
# list_1=set(list)
# a=list(list_1)
# print(a)

def fun_1(n,str):
    # import pdb;pdb.set_trace()
    list=[]
    s=len(str.split())
    print(s)
    for i in s:
        if i>=n:
            list.append(i)
            return list
    else:
        return list
print(fun_1(2,"this is string")) 
"""
