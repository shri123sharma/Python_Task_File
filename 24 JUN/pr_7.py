l1 = [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)]
l2=[]
print("the orginal tuple in",str(l1))

# Output : [(5, 6, 7, 8), (6, 10), (7, 13)]
# for i in range(0,len(l1)-1):
#     if l1[i][0]==l1[i+1][0]:
#         l2.append((l1[i][0],l1[i][1]))
#     else:
#         l1[i][1]!=l1[i+1][1]
#         l2.append((i))
# print(l2)

# for i in range(0,len(l1)):
#     for j in range(1,len(l1)):
#         if l1[i][0]==l1[j][0] or l1[i][1]!=l1[j][1]:
#             l2.append((l1[i][0]))
#             s1=set(l2)
#     else:
#         # l2.append((l1[i]))
#         pass   
# print(s1)
# # print(l3)            
        
# def addition(n):
#     return n+n
# number=(1,2,3,4)
# m1=map(addition,number)
# print(list(m1))

# l1=(4, 5, 4, 5, 6, 6, 5) 
# # Output : {4: 2, 5: 3, 6: 2} 
# d1={}
# c=1
# for i in l1:
#     if i not in d1:
#         d1.update(i)
#         c+=1
#     else:
#         c=1
#         d1.update(i)
# print(d1)

# from collections import Counter
# l1=(4, 5, 4, 5, 6, 6, 5) 

# res=dict(Counter(l1))
# print(res)

# d1={4:"indore",9:"haryana",5:"punjab"}
# a=sorted(d1.items())
# print(a)

# l1=[('for', 24), ('Geeks', 8), ('Geeks', 30)] 
# #Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]
# l=len(l1)
# print(l)
# for i in range(0,len(l1)):
#     for j in range(1,len(l1)):
#         if l1[i][1]>l1[j][1]:
#             l1[i],l1[j]=l1[j],l1[i]
#         else:
#             pass

# print(l1)
