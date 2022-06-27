l1=[(1, 3, 4), (2, 4, 6), (3, 8, 1)]

l3=[]
k=4
up=0
# List after bulk update : [(5, 7, 8), (6, 8, 10), (7, 12, 5)]
for i in l1:
    l2=[]
    for j in i:
        up=j+k
        l2.append(up)
    l3.append(tuple(l2))
print(l3)
        