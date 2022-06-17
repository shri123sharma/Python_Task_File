"""import collections
from ipaddress import collapse_addresses
from itertools import combinations

ls=[1,2,3,4,5,6]
ls_1=ls.copy()
ls_2=[]
# import pdb;pdb.set_trace()
for i in ls:
    ls_1.pop(i-1)
    sum=0
    for k in ls_1:       
        sum+=k
    ls_2.append(sum)
    ls_1.append(i)
print(ls_2)
min=ls_2[0]
max=ls_2[0]
for i in ls_2:
    if i<min:
        min=i
    elif  i>max:
        max=i

print(min,max)

dict_1={'a':1, 'b':2}
ls=list(dict_1.items())
d2=('c',3)
dict_2={}

ls.insert(0,d2)
print(dict(ls))

l = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
m = []
d={}
import pdb;pdb.set_trace()
for i in range(len(l)):
    if l[i][0] not in d.keys():
        d[l[i][0]] = [l[i][1]]
    else:
        d[l[i][0]].append(l[i][1])
for k, v in d.items():
    r = []
    r.append(k)
    for i in v:
        r.append(i)
    m.append(tuple(r))
print(m)

st= "engineersrock"
pattern = "gsr"
length=len(st)
ls=[]

# size=combinations(st,3)
# for i in size:
#     print(i)

for i in range(length):
    for j in range(i+1,length):
        ls.append(st[i]+st[j])
if "er" in ls:
    print(True)
else:
    print(False) 

if pattern in st:
    print('True')
else:
    print('False')

from collections import OrderedDict
dict_1={}
dict_1[1]=10
dict_1[2]=20
dict_1[3]=30
dict_1[4]=40

print(dict_1)

od=OrderedDict()
od[1]=100
od[2]=200
od[3]=300
od[4]=400
for i,v in od.items():
    print(i,v)

od_1=OrderedDict()
od_1["name"]="xyz"
od_1["location"]="indore"
od_1["city"]="wew"

for i,v in od_1.items():
    print(i,v)

od_1.pop("name")

od_1["name"]="eqwqw"
for k,j in od_1.items():
    print(k,j)

from collections import Counter

str_1="hello world"
dict_1={}
count=0
d=Counter(str_1)
for i,v in d.items():
    if v>1:
        print(i)

from collections import defaultdict, deque
from email.policy import default
from typing import Deque


test_dict = {"Gfg" : [5, 7, 5, 4, 5],
             "is" : [6, 7, 4, 3, 3], 
             "Best" : [9, 9, 6, 5, 5]}

for i in test_dict:
    max_value=0
    max_key=0

    length=len(set((test_dict[i])))
    if length>max_value:
        
        max_value=length
        max_key=i
print(max_key)
#unique element
ls=[10,20,20,40,60,30,70,60]
st=list(set(ls))
print(st)

ls_1=[21,21,23,3,46,56,9,878,79,9,80]
ls_2=[]
count=0
for i in ls_1:
    if i not in ls_2:
        ls_2.append(i)
        count+=1
    else:
        count=0
print(ls_2)
print(count)

ls=[4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
d=defaultdict(int)
d1={}
for i in ls:
    d[i]+=(i*i)
print(d)

ls=[1,2,3,45,7,78,8]
ls_1=(ls)
ls.append(799987,83829839)
"""

        
            
    
    







