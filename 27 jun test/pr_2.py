s1="this$#is% Matrix#  %!"
s2=["!","@","#","$","%","&","*","_",'']
for i in s1:
    print(i)
    if i<=str(len(s2)):
        s1=s1.replace(i," ")
        
    else: 
        pass     
print(s1)
