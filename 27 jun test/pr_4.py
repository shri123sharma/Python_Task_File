a=int(input("enter first value:"))
b=int(input("enter second value:"))
c=int(input("enter third value:"))
d=int(input("enter fourth value:"))

# n=int(input("enter 1"))
# l1=[]
# for i in (n):
    # a,b,c,d=l1.append(int(input("").split(",")))

if a<b:
    a=a+c
    if a>b and b>a:
        b=b+d
    if a>b:
        print("B is winner")
    else:
        print("A is winner")

elif a==b and b==c and c==d and d==a:
    print("A is winner")

elif a>b:
    b=b+c
    if a>b:
        a=a+d
        print("A is winner")
    else:
        print("B is winner")
    





        

    
