"""
inbuilt defined set
set_1=set("my name is shrikant sharma")
print(type(set_1))
print(set_1)

set_2={"japan","america","india","france","italy"}
print(set_2)

set_3={"japan","america","india","france","italy","india"}
for i in set_3:
    print(i)

set_1={"ukraine","mla","minister","pm","cm"}
print(type(set_1))
print(set_1)

set_1={"ukraine","india","japan","canada","usa","india"}
print(set_1)

for i in set_1:
    if i=="canada":
        break
    print(i)
        
print("loop in break in collection")

set_2=set("this is my laptop")

print(set_2)

set_3={'s', 't ', 'o', 'l', 't', 'p', 'h', 'i', 'y', 'a', 'm'}

for i in set_3:
    if i=="h":
        continue

    print(i)
print("h value is skip in this collection")

set_4=set(["python","perl","java","c"])

print(set_4)

set_4.add("react")

print(set_4)

set_5={"cloths","footwear","watch","goggle"}
set_5.add("jeans")
print(set_5)
set_5.add("shirt")
print(set_5)

while i==set_5:
    print(i)

for i in set_5:

        if i=="watch":
            continue
        print(i)

set_a={"jan","feb","march","april","may","june","july"}

set_a.update("aug","sep","oct","nov","decem")

print(set_a)

set_b=set(["mon","tue","web","thur"])
set_b.update(["fri","sat","sun"])

print(type(set_b))
print(set_b)

set_c={"air","water","agni","akash","patal","sun","moon"}
set_c.discard("patal")
print(set_c)

set_c.discard("air")
print(set_c)

set_c.remove("water")
print(set_c)

set_d={"my","name","is","shri","kant"}
set_d.pop()
print(set_d)

set_d.clear()
print(set_d)

set_e=set(["wheat","rice","maze","beans"])
set_e.remove("wh")
print(set_e)


set_1={"mp","up","punjab","delhi","haryana"}
set_2={"1","2","3","4","5","6","7"}

print(set_1|set_2)
print(set_1.union(set_2))

st_1={"mp","ajay","shrikant","deepika"}
st_2={"1","2","3","mp","sarika"}

print(st_1&st_2)
print(st_1.intersection(st_2))

from typing import FrozenSet


set_a={"jan","30","feb","28/29","march","31"}
set_b={"jan","31","may","21","june","12"}
set_c={"aug","13","jan","31","nov","8"}

set_a.intersection_update(set_b,set_c)
print(set_a)

day_1={"monday","tuesday","wednesday"}
day_2={"monday","tuesday","sunday"}

print(day_1.difference(day_2))

fset_1=frozenSet(["dubai","abudhabi","malysia","bangkok"])
print(type(fset_1))
fset_1.add("india")
print(fset_1)

user=input("enter a number in cooma separeted:")
List=user.split(",")
Tuple=tuple(List)
print(Tuple)
print(List)

str_1="russia is powerful country:"
list=str_1.split()
print("list:",list)

color_list = ["Red","Green","White" ,"Black"]
first=color_list[0]
second=color_list[-1]
print(first)
print(second)

a=(21,11,2022)
print("this is backslash BASE %i/%i/%i"%(a))

input_1=int(input("enter a number:"))
n1=int("%i"%(input_1))
n2=int("%i%i"%(input_1,input_1))
n3=int("%i%i%i"%(input_1,input_1,input_1))
n=int(n1+n2+n3)
print(n)

import calendar
year=int(input("please enter a year"))
month=int(input("please enter a month"))

print(calendar.month(year,month))
print(calendar.year(year,month))

from datetime import date

date_1=date(2017,7,2)
date_2=date(2017,8,11)

date_3=date_1-date_2
print(date_3.days)

def difference(n):

    if n<=17:
        return 17-n

    else:
        return (n-17)*2
difference(22)
difference(10)
print(difference(22))
print(difference(10))

a={"system","laptop",1,2,3,4,5,12.2,True,False}
b=set([1,2,3,4,4,5,])
c=set(("india","ukraie","russia",))
d=set()
print(d)
print(c)
print(type(b))
print(a)
print(b)

a={1,2,3,4,5,6,7,8,9,10}
print(len(a))


set_1={"my","name","is","shri",24,1997,True,True}
for i in set_1:
    print(i)

set_2={10,20,30,30,40,50,60,80,"edurkha"}
set_2.add("shri")
print(set_2)

set_3={23233,32,23,23,32,323,33333}
set_3.update([1,2,3,4,5])
print(set_3)

set_3.remove(1)
print(set_3)

set_2.discard(10)
print(set_2)

set_2.pop()
print(set_2)

set_1={1,2,3,4,5,6,7,8,9,10}
set_2={10,20,30,1,2,3,"shri","sharma"}
set_3={"shri","india","indore",1,2,9,5}

print(set_1)
print(set_2)
print(set_3)
print(set_1|set_2|set_3)

print(set_1.union(set_2,set_3))

print(set_1&set_2&set_3)
print(set_1.intersection(set_2,set_3))

set_1={10,20,30,11,22,33,21,42,"shri"}
set_2={111,112,222,10,11,7878,"indore","india"}

print(set_1-set_2)

set_1={10,20,30,40}
set_2={1,2,3,4,20,5,6}
set_3={100,200,1,10}

print(set_1.difference(set_2,set_3))

from optparse import Values


set_1=frozenset({"shri","sharma","1","true",11211,3,3,44,55})
print(set_1)

set_2=frozenset({"name":"shrikant","age":24,"location":"indore","country":"india"})
print(type(set_2))
for i in set_2:

    print(i,Values)

set_1={"the","real","life","data","arrangement"}
set_2=set((10,20,30,40,20,30,60,89))
set_3=set()

print(type(set_1))
print(type(set_2))
print(type(set_3))

print(set_1)
print(set_2)
print(set_3)
print("set in iteration")
for i in set_1:
        print(i)
print(" set data type element in access only loop")

set_1=set(["name","id","address","local","host","ip"])
set_2=set("my self is python developer")

print("firstsetiniterateusingloop")
for i in set_1:
    if i=="host":
        continue
    print(i)
print("item in iterate in skip one element")

print("iterate in string in set type")
for i in set_2:
    if i=="i":
        break
    print(i)
print("i do not have what is output of this iteration")

set_1=set("shrikant")
list_1=list(set_1)

print("for iteating the list")

for i in range(len(list_1)):
    if i==5:
        break
    print(list_1[i],end="")
print("if loop in break for 'a' element")

a={"a","b","c"}
b={"d","a","f"}

print(a.isdisjoint(b))

c={"12","13","14","15"}
d={"16","17","18","19"}

print(c.isdisjoint(d))

seT_1={"shrikant","risabh","sarika","deepika"}
print(seT_1.clear())
seT_1=set()
print=seT_1.update(["indore","bhopal","jabalpur","narsingapur"])

set_1=set()
print(type(set_1))

set_1=set("hello this world")
print(set_1)

list=[1,2,3,4,5,]
set_2=set(list)
print(set_2)

list_1=[10,20,30,40,1,1,22,22,2,2222,22]
set_3=set(list_1)
print(set_3)

set_3=set()
set_3.add(10)
set_3.add("shrikant")
set_3.add("sharma")
set_3.add(10)
set_3.add(100)
set_3.add(1000)

print(set_3)

set_4=set()

for i in range(1,11):

    set_4.add(i)

print(set_4)
"""

set_1={1,2,3,4,5,6}

set_1.update(["shrikant","sharma","indore","madhyapradesh"])

print(set_1)

set_1.update(["india"])
print(set_1)

for i in set_1:

    print(i)

set_2={10,29,394,75,755,48,44,8484}
set_2.discard(100)
print(set_2)

set_3={1,2,3,4,5,6,7,8}

print(set_3.pop())
print(set_3.pop())
print(set_3)

set_1={1,2,3,4,5,}
set_2={1,2,3,4,6,}

set_3=set_1.union(set_2)
print(set_3)

set_3=set_1.difference(set_2)
print(set_3)

set_3=set_1.intersection(set_2)
print(set_3)




