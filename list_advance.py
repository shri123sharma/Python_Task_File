# l1=[1,2,4,4,5,7,8,8,9,9]
# l2=[]
# count=0
# for i in l1:
#     if i not in l2:
#         count+=1
#         l2.append(i)
# print(count)

# l1=[1, 3, 5, 6, 3, 5, 6, 1]
# # Duplication removal list product : 90
# l2=[]
# m=1
# for i in l1:
#     if i  not in l2:
#         l2.append(i)
# for k in l2:
#     m=k*m
# print(m)

# l1 =[4, 6, 4, 3, 3, 4, 3, 4, 3, 8] 
# l2=[]
# d1={}
# K = 3
# # Output : [4, 3]
# for i in l1:
#     # if i not in l2:
#     c=l1.count(i)
#     d1.update({i:c})
# for i,v in d1.items():
#     print(i,v)
#     if v>=K:
#         l2.append(i)
# print(l2)

# l1=[4, 5, 5, 5, 3, 8]
# l2=[]
# l3=[]
# for i in range(1,len(l1)):
#     if l1[i]==l1[i-1]:
#         if l1[i]==l1[i+1]:
#             l2.append(l1[i])
        
#         # else:
#         #     l2.append(l1[i])
# print(l2)

# l1=[1,1,1,64,78,34,22,22,22]
# l2=[]
# l3=[]
# for i in range(1,len(l1)-1):
#     if l1[i]==l1[i-1]:
#         if l1[i]==l1[i+1]:
#             l2.append(l1[i])
#         else:
#             l3.append(l1[i])
# print(l2)

# l1=[1, 2, 2, 3, 4, 5]
# l2=[]
# # Output: 2 2 3 4 5
# for i in range(1,len(l1)):
#     if l1[i]>=l1[i-1]:
#         l2.append(l1[i])
        
# print(l2)

l1=[1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# l2=[]
# for i in range(0,len(l1)):
#     for j in range(0,len(l1)):
#         for k in range(0,len(l1)):
#             if i!=j and j!=k and k!=i:
#                 print(l1[i],l1[j],l1[k])
#             # else:
#             #     if (i==j==k):
#             #         l2.append((i,j,k))
# print(l2)

# l2=[0,9,5]
# l=len(l2)
# for i in range(0,l):
#     for j in range(0,l):
#         for k in range(0,l):
#             if i==j and j==k and k==i:
#                 print(l2[i],l2[j],l2[k])

# from itertools import permutations
# l1=[10,20,30,40]
# l2=permutations(l1,3)

# for i in l2:
#     print(i)

# l2=["geekforgeeks", [5, 4, 3], "is", ["best", "good", "better"]]
# K = 3 
# # Output : [[‘geekforgeeks’, 5, ‘is’, ‘best’], [‘geekforgeeks’, 4, ‘is’, ‘good’], [‘geekforgeeks’, 3, ‘is’, ‘better’]] 
# l3=[]
  
# for i in range(0,len(l2)-1):
#     l1=[]
      
#     for k in l2:
#         if not isinstance(k,list):
#             l1.append(k)
#         else:
#             l1.append(k[i])
#     l3.append(l1)
# print(l3)

# l2=['geekforgeeks', [5, 4], 'is', ['best', 'good']] 
# K = 2 
# # Output : [[‘geekforgeeks’, 5, ‘is’, ‘best’], [‘geekforgeeks’, 4, ‘is’, ‘good’]] 
# res=[]
# for i in range(0,len(l1)-1):
#     l3=[]
#     for k in l2:
#         if not isinstance(k,list):
#             l3.append(k)
#         else:
#             l3.append(k[i])
#     res.append(l3)
# print(res)
# print(type==int)

    


