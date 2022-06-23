# l1=[1, 1, 2, 3, 4, 5, 1, 2, 1] 
# # Output : 2 3 4 5 2
# l2=[]
# item=1

# for i in l1:
#     if i!=l1:
#         c=l1.count(i)
#         for k in range(c):
#             l1.remove((item))
# print(l1)

# l1=[1,1,2,3,4,5,1,2,1]
# l2=[]
# item=1
# for i in l1:
#     if i!=item:
#         c=l1.count(item)
#         l2.append(i)
        
# print(l2)

# l1=[(4, 5), (5, 6), (1, 3), (0, 0)]
# k = 0
# l2=[]
# # Output : [(4, 5), (5, 6), (1, 3)]
# for i in l1:
#     if (k,k) not in zip(i,i[:-1]):
#         l2.append(i)
# print(l2)

# l2=[[1,4],[2,6],[4,4],[3,4],[6,4]]
# k=4
# l3=[]

# for i in l2:
#     if  ([k,k]) not in zip(i,i[:-1]):
#         l3.append(i)
# print(l3)

# l1={'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# # [[‘gfg’, 1, 3, 4], [‘is’, 7, 6], [‘best’, 4, 5]]
# l2=[]
# for i,v in l1.items():
#     a=[i]+v
#     l2.append((a))
# print(l2)

# l1=[['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
# # The mapped Dictionary : {(‘c’, ‘d’): (3, 4), (‘e’, ‘f’): (5, 6), (‘a’, ‘b’): (1, 2)}
# d1={}
# for i in l1:
    
#     a=tuple((i[:2]))
#     print(a)
#     b=tuple(i[2:])
#     print(b)
#     # b=tuple((i[2:3],i[2:3]))
#     d1.update({a:b})
# print(d1)

# test_list = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]
# # Output : [[‘Gfg’, ‘best’], [123, 10], [51, 7]]
# l1=[]
# l2=[]

# for i in test_list:
#     a=list(set(i.keys()))
#     l2.append(a)
#     b=list(i.values())
#     l1.append(b)
#     print(a)
# print(l1,l2)

# d1={'gfg' : {'x' : 5, 'y' : 6, 'z': 3}, 'best' : {'x' : 8, 'y' : 3, 'z': 5}}
# # Output : [(‘x’, (5, 8)), (‘y’, (6, 3)), (‘z’, (3, 5))]
# l1=[]
# l2=[]
# l3=[]
# l4=[]
# for i,v in d1.items():
#     for k,s in v.items():
#         if (k,s) not in l2:
#             l2.append((k,s))
#         else:
#            pass

# for m in range(0,len(l2)):
#     print(m)
#     for n in range(i+1,len(l2)):
#         print(n)
#         if [m][0]==[n][:-1]:
#             l3.append(m,n)
# print(l3)
            
# a = [2,3,4]
# b = [5,6,7]
# c = map(lambda x,y:(x,y),a,b)
# print(type(c))


        