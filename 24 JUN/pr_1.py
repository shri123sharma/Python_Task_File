t1 =(3, 7, 1, 18, 9) 
k = 2 
l2=[]
# Output : (3, 1, 9, 18)
l1=list(t1)
l1.sort()
for i,v in enumerate(l1):
    print(i,v)
    if i<k or i>k:
        l2.append(v)
t1=tuple(l2)
print(t1)



    
        
