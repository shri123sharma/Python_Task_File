"""
ls=[1,[],3,4,5,[],8,9,10]

for i in ls:
    if i==[]:
        ls.remove(i)
print(ls)
    
ls_1=[ls for i in ls if i!=[]]

def fun_1(ls):
    ls_1=[]
    for i in ls:
        if i==[]:
            ls.remove(i)
            # print(ls_1.append(i))
    return ls
print(fun_1([1,2,34,[],54,23,[],77]))

ls_1 = ["Gfg", "3", "is", "8"]
ls_2 = ["name", "id"]
ls_3=[]
# op=[{‘name’: ‘Gfg’, ‘id’: 3}, {‘name’: ‘is’, ‘id’: 8}]
# ls_3=dict(zip(ls_2,ls_1))
# for i in range(0len(ls_2)):
length=len(ls_1)

for i in range(0,length,2):

    ls_3.append({ls_2[0]:ls_1[i],ls_2[1]:ls_1[i+1]})
print(ls_3)

ls = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
ls_1=[]
# import pdb;pdb.set_trace()
for i in ls:
    length=len(i)
    for k in range(length-1):
        ls_1.append({ls[k][0]:ls[k][2]})
print(ls_1)
print(k)
print(length)
# {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}
ls = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
d1={}
for i in ls: 
#     dict[tuple(i[:2])]=tuple(i[2:])
# print(dict)
    t1,t2=[],[]
    
    t1.append(i[0])
    t1.append(i[1])
    t2.append(i[2])
    t2.append(i[3])
    
    t3=tuple((t1))
    t4=tuple(t2)
    d1.update({t3:t4})
    # print(t3)
print(d1)

ls_1=[[1, 2], [3, 4], [5, 6]]
ls_2=[[3, 4], [5, 7], [1, 2]]
ls_1.extend(ls_2)
ls_3=[]
for i in ls_1:
    if ls_1.count(i)<=1:

            ls_3.append(i)
            
print(ls_3)


# The uncommon of two lists is : [[5, 6], [5, 7]]
# ls_3=[]
# ls_4=[]
# # print(ls_3)
# for i in ls_1:
#     for j in ls_2:
#         if i!=j:
#             ls_3.append(i)

#     else:
#         ls_4.append(i)
# print(ls_3)
# print(s1)
"""

# test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
# # op=7
# ls_1=str(test_list)
# print(ls_1)
# for i in range(len(test_list)):
#     print(i)

# ls_1=[[4, 1, 6], [7, 8], [4, 10, 8]]
# op=[[6, 4, 1], [8, 7], [10, 8, 4]]
# length=len(ls_1)
# print(length)
# ls_2=[]
# for i in ls_1:
#     for k in range(0,len(i)):
#         for s in range(k+1,len(i)):
#             if i[k]<i[s]:
#                 i[k],i[s]=i[s],i[k]
#     ls_2.append(i)
#     print(ls_2)
# print(ls_2)

# ls_2=[]
# for i in ls_1:
#     i.sort(reverse=True)
#     ls_2.append(i)
# # print(ls_2)

# ls_3=[i for i in ls_1 if (i.sort(reverse=True)) if ls_2.append(i)]
# print(ls_3)

# ls_4=[sorted(i,reverse=True) for i in ls_1]
# print(ls_4)

# d1={"abc":4,"geek":"hello","name":5,"kk":'00'}
# d2=d1.copy()
# ls_1=[]
# ls_2=[]
# # import pdb;pdb.set_trace()
# for i,v in d1.items():
#     if type(v)==int:
#         # ls_1.append((i,v))
#         if v>=4:
#             ls_1.append((i,v))
#     else:
#         ls_2.append((i,v))
# print(ls_2)
#     # for k,s in d2.items():

# ls_1=[[4, 5, 6], [2, 4, 5], [6, 7, 5]]
# # The list after pairing is : [[[4, 6], [5, 6]], [[2, 5], [4, 5]], [[6, 5], [7, 5]]]         
# ls_2=[]
# for i in ls_1:
#     ls_2.append([[i[0],i[-1]],[i[1],i[-1]]])
# print(ls_2)

# ls_1=[(6, 24, 12), (60, 12, 6), (12, 18, 21)]
# K = 6 
# ls_2=ls_1.copy()
# # Output[(6, 24, 12), (60, 12, 6)] 
# # import pdb;pdb.set_trace()
# for i in ls_1:
#     for s in i:
#         if s%K==0:
#             pass
#         else:
#             ls_1.remove(i)
#             break
# print(ls_1)

# ls_2=[(6, 24, 12), (60, 10, 5), (12, 18, 21)]
# K = 5
# # ls_3=ls_2.copy()
# ls_4=[] 
# # Output : [(60, 10, 5)]
# for i in ls_2:
#     for j in i:
#         if j%5==0:
#             pass
#         else:
#             ls_2.remove(i)
#             break
# print(ls_2)

# ls1 =[(4, 5, 9), (3, 2, 3), (-3, 5, 6), (4, -6)]
# # Output:[(4, 5, 9)] 
# ls2=ls1.copy()
# ls3=[]
# for i in ls1:
#     for j in i:
#         if j<0:
#             ls2.remove(i)
#     # ls3.append(i)
# print(ls2)

# ls1=(1, 3, 5, 2, 3, 5, 1, 1, 3)
# ls2=list(ls1)
# s1=set()
# ls3=[]
# # op=(1, 2, 3, 5)
# count=0
# for i in ls2:
#     # count=0
#     for j in ls2:
#         if i==j:
#             count+=1
#             s1.add(i)
#         else:
#             count=0
#             ls3.append(i)
# print(count)
# print(tuple(s1))


# ls1=([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
# # op=[[4, 7, 8], [1, 2, 3], [9, 10, 11]]
# ls2=list(ls1)
# ls3=[]
# for i in ls2:
#     if i not in ls3:
#         ls3.append(i)       
# print(ls3)


# l1=[]
# l2=[]

# ls1= [(15, 3), (3, 9)]
# # Output : [9, 5, 3, 1] 
# for i in ls1:
#     for j in i:
#         if j>=10:
#             for k in str(j):
#                 l1.append(int(k))
#         else:
#             for k in str(j):
#                 l2.append(int(k))
# l1.extend(l2)
# l3=[]
# for s in l1:
#     if s not in l3:
#         # if type(s)==int:
#         l3.append(s)
#         l3.sort(reverse=True)
        
# print((l3))

# ls1=[(1, 7), (6, 7), (8, 100), (4, 21),(3,10)]
# ls2=[(1, 3), (2, 1), (9, 7), (2, 17),(3,18)]
# # Output : [(7, 3)]
# ls3=[]
# # ls1.extend(ls2)
# for i in ls1:
#     for j in ls2:
#         if i[0]==j[0]:
#             ls3.append((i[1],j[1]))
# print(ls3)

# t1=("hello","world")
# t2=(10,20,30)

# if cmp(t1,t2)!=0:
#     print("not same")
# else:
#     print("same")

# tup1=("geeks for geek")
# n=5
# ls1=[]
# for i in range(int(n)):
#     if i==tup1:
#         ls1.append(i)
# print(ls1)

# ls1=[(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
# ls2=ls1.copy()

# k = 0 
# # Output : [4, 4, 2] 
# # Explanation : 5 – 1 = 4, hence 4. 
# ls3=[]
# for i in range(0,len(ls1)-1):
#     # for j in range(i+1,len(ls1)):
#     a=abs(ls1[i][k]-ls1[i+1][k])
#     ls3.append(a)
#             # break
#         # a=ls1[i][k]-ls1[j][k]
#         # ls3.append(a)
# print(ls3)

# ls1=[(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
# k = 2 
# # Output : [2, 4, 5] 
# ls2=[]
# for i in range(0,len(ls1)-1):
#     a=abs(ls1[i][k]-ls1[i+1][k])
#     ls2.append(a)
# print(ls2)

# l2=[(5, 6, 7), (1, 3, 5), (8, 9, 19)]
# # op=665
# l3=[]
# k=2
# length=len(l2)
# print(length)
# a=1
# for i in range(0,len(l2)):
#     a*=l2[i][k]
# l3.append(a)
# print(tuple(l3))

# l1=([5], [6], [3], [8])
# l2=tuple(l1)
# print(l2)
# # op=(5, 6, 3, 8)
# tp1=[]
# for i in l1:
#     l2=tuple(i)
#     tp1.append(l2)
# print(tp1)

# l1=[("Amana", 28), ("Zenat", 30), ("Abhishek", 29), ("Nikhil", 21), ("B", "C")]
# # op=[('Amana', 28), ('Abhishek', 29), ('B', 'C'), ('Nikhil', 21), ('Zenat', 30)

# for i in range(0,len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i][0]>l1[j][0]:
#             l1[i],l1[j]=l1[j],l1[i]
        
# print(l1)

# s1="ddkasmasakjska"
# ls1=list(s1)
# print(ls1)
# s2=ord("a")
# s3=""
# print(s2)

# for i in range(0,len(ls1)):
#     for j in range(i+1,len(ls1)):
#         if ls1[i]>ls1[j]:
#            ls1[i],ls1[j]=ls1[j],ls1[i]
#         s3="".join(ls1)
# print(s3)

from itertools import combinations
ls1=[(2,4), (6, 7), (5, 1), (6, 10)]
# op=[(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
ls2=[]
temp=combinations(ls1,2)
for i in list(temp):
    a=i[0][0]+i[1][0],i[0][1]+i[1][1]
    ls2.append(a)
print(ls2)    
    
# import pdb;pdb.set_trace()
# for j in range(len(ls1)):
#     for k in range(j+1,(len(ls1))):
#         for i in range(1,len(ls1[0])):
#             a=ls1[j][i-1]+ls1[k][i-1],ls1[j][i]+ls1[k][i]
#     ls2.append(a)
# print(ls2)

# import itertools
# for i in itertools.count(10,10):
#     if i==60:
#         break
#     else:
#         print(i,end=",")

# import itertools
# for i in itertools.cycle("abab"):
#     if i==3:
#         break
#     else:
#         print(i)

import itertools
l1=[10,20,30,40,50]
for i in itertools.combinations(l1,2):
    print(i)












        