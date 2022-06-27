
t1=[1, 2, 3]
t2=[]
# Output: [(1, 1), (2, 8), (3, 27)]
for i,v in enumerate(t1,1):
    t2.append((i,v**v))
print(t2)
    