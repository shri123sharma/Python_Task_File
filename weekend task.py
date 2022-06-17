"""str_1="aabbbcdaa"
ls=str_1.split()
print(ls)
count=0
length=len(str_1)
for i in str_1:
    for j in str_1:
"""
# str_3="aabbbcdaa"
# str_1=str_3[0]
# length=len(str_3)
# str_2=""
# count=1
# for i in range(1,length):
        
#         if str_3[i]==str_1 and str_3[i]==str_1[-1]:
#             count+=1
#             pass 
#         else:
#             str_2=str_2+str_1+str(count)
#             str_1=str_3[i]
#             count=1
# print(str_2)
"""
str_1="aabbccddeeaaaa"
length=len(str_1)
count=1
str_2=""
print(length)
for i in range(len(str_1)):
         if i<len(str_1)-1 and str_1[i]==str_1[i+1]:
             count=count+1
         else:
            str_2+=str_1[i]+str(count)
            count=1
print(str_2)
"""           
# str_3="aabbbcdaa"
# li = []
# count=0
# for  i  in str_3:
 
#     for j in str_3:
        
#         if i==j:
#             count +=1
#     else:
            
#         li.append(i+str(count))
# print(li)

# str_1="hello World"
# str_2=str_1.lower()
# f=collections.Counter(str_1)
# dict={}

# for key,value in f.items():
#     if value>1:
#         dict[key]=value
# print(dict)

ls=[5,10,20,15,20]
bag=0
# import pdb;pdb.set_trace()
for i in ls:
    if i==5:
        bag+=5
        print(bag,True)
    elif i > 5 and (bag-(i-5))>=0:
        bag= bag+5
        print(bag,True)
    else:
        print(False)

# import itertools
# ls=[1,2,3,4,4]
# ls_1=(list(itertools.permutations(ls)))
# print(ls_1)

# ls=[10,20,30,40,50,60]
# for i,v in enumerate(ls,1):
#     print({i:v})

# ls=["h","e","l","l","o","w","o","r","l","d"]
# str_1="".join(ls)
# print(str_1)

# ls_1=[10,20,30,40,20,50,60,40]
# print("orginial list",ls_1)
# set_1=set(ls_1)
# ls_2=list(set_1)
# print(ls_2)

# ls=[10,10,10,20,2030,40,40,40,40,50,50,50]
# count=0
# dict={}
# for i in ls:
#     if i==ls:
#         count+=1
#     else:
#         count=1

# l = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# # op=[(5,6,7,8),(6,10),(7,13)]
# # import pdb;pdb.set_trace()
# d={}
# m = []
# for i in range(len(l)):
#     if l[i][0] not in d.keys():
        
#         d[l[i][0]] = [l[i][1]]
#     else:
        
#         d[l[i][0]].append(l[i][1])
        
# for k, v in d.items():
#     print(k,v)
#     r = []
#     r.append(k)
#     for i in v:
#         r.append(i)
#     m.append(tuple(r))
# print(m)

# l = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# d={}
# m=[]
# for i in range(len(l)):
#     if l[i][0] not in d.keys():
#         d[l[i][0]]=[l[i][0],l[i][1]]

#     else:
#         d[l[i][0]].append(l[i][1])
# print(d)

# r=[]
# for k,v in d.items():
#     r.append(tuple(v))
# print(r)

# ls=[10,20,30,40,40,40,60,70,80,99]
# count=0

# for i in range(40,100):
    
#     if i in ls:
#         count+=1
#     else:
#         pass
# print(count)

# ls=[2,5,7,4,3]

# for i in ls:
#     if i==[]:
#         print("not a sublist")
# else:
#     print("this list access in sublist")

# marks=int(input("enter a number"))

# if marks==90 :
#     print("grade A+")
# elif marks==80:
#     print("grade B")
# elif marks==60:
#     print("grade C")
# else:
#     print("grade D")

# l=[5,5,10,10]
# count_5=0
# count_10=0
# # import pdb;pdb.set_trace()
# c = 0
# res = []
# for m in l:
#     if m == 5:
#        res.append(m)
#        count_5+=1
#     elif m>5:
#         if m==10 and count_5>=1:
#             res.remove(5)
#             res.append(m)
#             count_5-=1
#             count_10+=1
#             # print(res)
#         elif m==20 and count_5>=3:
#             res.remove(5)
#             res.remove(5)
#             res.remove(5)
#             res.append(m)
#             count_5-=3
#         elif count_5>=1 and count_10>=1:
#             res.remove(5)
#             res.remove(10)
#             res.append(m)
#             count_5-=1
#             count_10-=1
#         else:
#             break
#     else:
#         break
#     c+=1
# print(res)
# if c != (len(l)):
#     print(False)
# else:
#     print(True)

# ls=[5,10,15,20,30]
# count5=0
# count10=0
# count15=0
# bag=[]

# for i in ls:
#     if i==5:
#         bag=i+bag
#         count5+=1
    
#     elif i>=10:
#         if i==10 and i>5:
#             bag=i-bag
#             count10+=1
#             count5-=1
#             print(count5)

# set_1={"hello world"}
# print(set_1)
# set_2=set([1,2,3,4,5,6,7])
# print(set_2)

# str_1="hello world"
# set_1=set(str_1)
# print(set_1)

# dict={"name":"xyz","location":"indore"}
# set_1=set(dict.items())
# print(set_1)

# tp=("hello","world","india")
# set_1=set(tp)
# print(set_1)

# set_2={10,20,30,40,50}
# set_2.add(60)
# print(set_2)

# set_2=set()
# set_2.add(10)
# print(set_2)

# set_1=set()
# for i in range(1,10):
#     set_1.add(i)
# print(set_1)

# # set_1=set()
# # for i in range(1,5):
# #     set_1.update(i)
# # print(set_1)

# set_1=set([1,2,3,4,5,5,])
# for i in set_1:
#     print(i)

# set_2=set([10,102,2829,22,90,404,])
# set_2.remove(10)
# print(set_2)

# set_2.discard(102)
# print(set_2)

# print(set_2.pop())
# print(set_2)

# set_3=set((1,2,3,4,5,6,7,8,9))

# str_1="aaabbbccccccbbbaaa"
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


