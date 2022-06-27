t1=(1, 5, 7, 8, 10)
l1=list(t1)
l2=[]
l=len(t1)
a=0
# print(l)
# Resultant tuple after multiplication : (5, 35, 56, 80)
for i in range(0,len(l1)-1):
    a=(t1[i]*t1[i+1])
    l2.append(a)
print(tuple(l2))

#     for j in range(1,len(l1)-1):
#         # if i>j and i<j and i==j:
#             a=(t1[i]*t1[j])
#             l2.append(a)
# print(l2)
