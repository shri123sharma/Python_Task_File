N = int(input("please_1:"))
ls_1=[]
res=[]
for i in range(N):
    ls_1.append(input("please command:").split(" "))
   
    if ls_1[i][0]=="insert":
    
        res.insert(int(ls_1[i][1]),int(ls_1[i][2]))
        
    elif ls_1[i][0]=="print":
        print(res)

    elif ls_1[i][0]=="remove":
        res.remove(int(ls_1[i][1]))

    elif ls_1[i][0]=="append":
        res.append(int(ls_1[i][1]))

    elif ls_1[i][0]=="sort":
        res.sort()

    elif ls_1[i][0]=="pop":
        res.pop()

    elif ls_1[i][0]=="reverse":
        res.reverse()

    else:
        pass
    print(res)
   
