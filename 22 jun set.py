# import sys

# s1={1,2,3,4,4,55,6,76,77}
# s2={"hello","world",}
# s3={(1,2,3,),("hello","world"),(10,20,30)}

# print((str(sys.getsizeof(s1))+"bytes"))
# print(("set2 size of"+(str(sys.getsizeof(s2))+" bytes")))
# s1=set()
# for i in s1:
#     if i not in s1:
#         print(i)

# s1=([8, 16, 24, 1, 25, 3, 10, 65, 55])
# # Output : max is 65
# # l1=list(s1)
# # print(l1)
# max=s1[0]
# print(max)
# for i in s1:
#     # max=s1[0]
#     if i>max:
#         max=i
# print(max)

# s2=([8, 16, 24, 1, 25, 3, 10, 65, 55])
# min=s1[0]

# for i in s2:
#     if i<min:
#         min=i
# print(min)
# l1=[122,3,32,2,35,35,45,4,454,3]
# for i in l1:
#     print(i)

# s3=set(["s","e","e","q","r" "8:", "9"])
# s1={1212,32,3,23,4,3,3}
# # print(s1)
# print(s3)
# for i in s1:
#     print(i)
    
# s3=[12, 10, 13, 15, 8]
# print(type(s3))
# l=len(s3)
# for i in s3:
#     print(i)
#     s3.pop()
# print(s3)

# s4=set([10,40,60,11,212])
# while s4:
#     s4.pop()
#     print(s4)

# a = [1, 2, 3, 4, 5]
# b = [5, 6, 7, 8, 9]
# a.extend(b)
# count=1
# l=len(a)
# print(l)
# # Output : True
# for i in range(0,len(a)-1):
#     if a[i]==a[i+1]:
#             count+=1
#             print("True")
# else:
#     count=1
#     pass

# a = [1, 1, 3, 4, 5]
# b = [10, 6, 7, 8, 9]
# a.extend(b)
# count=1
# l=len(a)
# for i in range(0,l-1):
#     if a[i]==a[i+1]:
#         count+=1
#         print("True")
#     else:
#         count=1
#         print("False")
# a = [1, 1, 3, 4, 5]
# b = [10, 6, 7, 8, 9]
# s1=set(a)
# s2=set(b)

# def fun_1(s1,s2):
#     if (s1==s2):
#         print(True)
#     else:
#         print(False)
# fun_1(s1,s2)

# def fun_2(s1,s2):
#     s1=set(a)
#     s2=set(b)

#     if len(s1.intersection(s2))>0:
#         return True
#     else:
#         return False
# a=[1, 1, 3, 4, 5]
# b=[5, 6, 7, 8, 9]
# print(fun_2(a,b))

# ar1 = [1, 5, 10, 20, 40, 80]
# ar2 = [6, 7, 20, 80, 100]
# ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# s1=set(ar1)
# s2=set(ar2)
# s3=set(ar3)
# # print(s1)
# set_1=s1.intersection(s2)
# set_2=set_1.intersection(s3)
# print(list(set_2))
# print(set_1)
# s1=(s1.union(s2,s3))
# print(s1)
# s3=set()
# for i in range(0,len(s1)):
#     if s1[i]==s1[i+1]:
#         s3.add(i)
# print(s3)

# set_1={10,20,30,40,50}
# set_2={100,20,30,40,60}

# set_3=set_1.difference(set_2)
# print(set_3)

# list1 = [10, 15, 20, 25, 30, 35, 40]
# list2 = [25, 40, 35] 
# # Output :
# # [10, 20, 30, 15]
# s1=set(list1)
# s2=set(list2)
# s3=s1.difference(s2)
# print(list(s3))

# A = [1, 4, 5, 7, 9]
# B = [4, 5, 7, 9]
# # Output: [1]
# s1=set(A)
# s2=set(B)
# s3=s1.difference(s2)
# print(list(s3))

# s="GeeksforGeeks"
# str_1=s.lower()
# # Output : No. of vowels : 5
# s1="aeiouA"
# s1=set()
# count=1
# for i in str_1:
#     print(i)
#     if i==("a","i","e","o","u"):
#         count+=1
        
# else:
#     count=0
# print(count)
