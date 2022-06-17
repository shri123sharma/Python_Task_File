ls=[5,5,10,10,20]
count5=0
count10=0
count20=0
count=0
length=len(ls)

# import pdb;pdb.set_trace()
for i in ls:

    if i==5:
        count5+=1
        
        
    elif i==10 and count5>=1:
        
            # bag.append(i)
            # bag.remove(5)
        count10+=1
        count5-=1
        
    elif i==20 and count10>=1 and count5>=1:
            
            # bag.append(i)
            # bag.remove(10)
                count20+=1
                count10-=1
                count5-=1
    elif i==20 and count5>=3:
            # bag.append(i)
            # bag.remove(10)
        count5-=3
        count20+=1
    else:
        break    
    count+=1
if count!=length:
    print(False)
else:
    print(True) 

str_1="aaabbbccccccbbbaaa"
# length=len(str_1)
# count=1
# str_2=""
# for i in range(length):
#     # for j in range(i+1,length):
#         if i<(length-1) and str_1[i]==str_1[i+1]:
#             count+=1
#         else:
#             str_2=str_2+str_1[i]+str(count)
#             count=1
# print(str_2)

