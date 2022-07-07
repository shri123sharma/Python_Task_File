# open function in used in open the file
# if open function in two parmeter in first
# syntax:

# file=open("basic.py","r")
# for i in file:

#     print(i.read())

# file_1=open("class.py","r")
# print(file_1.read())

# a,b=10,20

# big= a if a < b else b
# print(big)
# a=(1,2,3,4,4)
# b=(32,32,323,23,33,32,3)

# print(a+b)
# dict={1:'shri',2:"sharma",3:"hello"}
# a=dict.copy()
# print(a)

# dictionary={"shrikant":2121,"location":"indore","state":"madhya pradesh"}

# dictionary["location"]="bhopal"

# print(dictionary)

# set_1={1,2,3,4,5,6}
# set_2={5,6,4,7}

# a=set_1.intersection(set_2)
# print(a)

# n=int(input("enter a number"))
# tem=n
# rev=0
# while n>0:
#     dig=n%10 #dig=0
#     rev=rev*10+dig #rev=0
#     n=n//10 #n=1
# if (tem==rev):

#     print("this is palidrome")
# else:
#     print("this number in not palidrome")

# n=int(input('enter a number of row'))
# row=6

# for i in range(1,row):
#     for j in range(i):
#         print(i)
#     print("\n")

# def pattern(n):

#     for i in range(n):
#         for j in range(i):
#             print(i,end=" ")
#         print(" ")
# pattern(5)

# def pattern(n):

#     for i in range(n):
#         for j in range(0,i+1):
#             print("#",end=" ")
#         print("")
# pattern(5)

# num=7
# factorial=1

# if num<0:

#     print("factorial is not negative number")
# elif num==0:
#     print("the factorial is 0 is 1")

# else:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print("the factorial of",num,"is",factorial)

# from math import factorial

# n=6

# for i in range(n):
#     for j in range(n,i+1):
#         print(end=" ")

#     for j in range(i+1):
                 
#         print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")

#     print()
# row=6

# for i in range(0,row):

#     for j in range(0,i+1):

#         print(j,end="")

#     char=chr(row)

#     print(char,end=" ")

#     row+=1

#     print("")

# def pattern(num):

#     number=65

#     for i in range(0,num):

#         for j in range(0,i+1):

#             char=chr(number)

#             print(char,end=" ")
#             number=number+1

#         print("\n")
        
# pattern(5)

# d1={"k1":10,"k2":20,"k3":30}

# for i in d1.keys():

#     d1[i]=d1[i]+1

# print(d1.values())

# import random
# n=random.randint(10,20)
# print(n)

# def fun(*args,**kwargs):

#     print(args)
#     print(kwargs)

# fun(1,2,3,4,5,name='shrikant')

# def fun(name,age="24"):

#     print("this is first candiate",name+age)
#     print("this is second candiate",name+age)

# fun("shrikant")
# fun("ajay")
# # shallow copy   
# first_list=[1,2,3,4,5,6]
# second_list=first_list

# second_list.append(9)
# print(first_list)
# print(second_list)

# list_1=[1,2,3,4,5,6,7,7323,3,2,22,]
# list_2=[]
# a=list_1[2:5]
# list_2.append(a)
# print(list_2)

# list_1=[10,20,30,40,50]

# a=list_1[-1:-4:-1]
# print(a)

# a=int(input("enter a number"))
# num=a

# reverse=0

# while a>0:

#     rem=a%10
#     reverse=reverse*10+rem
#     a=a//10

# print("reverse num is",reverse)
# if num==reverse:

#     print("this is palimdrome")
# else:
#     print("this is not palidrome")

# list=['hello',1,2,3,4,"nice","hii"]

# str="".join([str(i) for i in list])
# print(str)

# list=[1,2,3,4,5,6]

# dict={i:"pass" for i in list}
# print(dict)
















