r1=int(input("enter a start room"))
r2=int(input("enter a end room"))
floor=0

for i in range(r1,r2):
    if (i==10 or i==20 or i==30 or i==40 or i==50 or i==60 or i==70 or i==80 or i==90 or i==100):
        floor+=1
    print(floor)


    if (r1-r2):
        
        if (i==10 or i==20 or i==30 or i==40 or i==50 or i==60 or i==70 or i==80 or i==90 or i==100):
            floor-=1
        else:
            pass
print(floor)






