       #we can not print first argument as a default function#

"""def greet(msg="jai shree ram",name):
    print(msg,name)
'''greet("Hii")
greet("hello")'''
greet(name="python")"""



               #factorial with 'for' loop#

'''
a=int(input("enter any no wanted to find factorial: "))
f=1
for i in range(1,a+1):
    f=f*i
print("factorial of the given no is:",f)

'''



           #factorial using function#

'''a=int(input("enter any value "))
def maddy(a,b):
    """factorial programme"""
    total=1
    i=1
    while i<=a:
        total=total*i
        i=i+1
    print("factrial is  ",total+b)
print(maddy.__doc__)
maddy(a,b=5)'''

    #star printing by self logic#
           
'''star=4
i=0
for i in range(0,4):
    for j in range(0,star-i):
        print("*",end="")
    print("")
    i=i+1'''

#print("") is used to switch to the next line#

'''star=10
i=1
for i in range(1,9):
    for j in range(1,star-i):
        print("*",end="")
    print("")
    i=i+1''' 

        

             #leap year programme#


'''
def leap_year():
    """This is a leap year programme"""
    a=int(input("enter any year:"))
    if a%100==0:
        if a%400==0:
            print("this is a leap year")
    else:
        if a%4==0:
            print("this is a leap year")
        else:
            print("this is not a leap year")
print(leap_year.__doc__)
leap_year()

'''



                           #reverse no programme#


'''
a=int(input("enter any no:"))
rev=0
while a>0:
    reminder=a%10
    rev=rev*10+reminder
    a=a//10
print("reverse for the given no is:",rev)

'''



                          #palindrome programme#

#palindrome-defintion of palindrome is,no in reversed postion is same as original once is called palindrome no#

                            #original no == reverse no#


'''
a=int(input("enter any no wanted to check palindrome: "))
num=a
rev=0
while a>0:
    reminder=a%10
    rev=rev*10+reminder
    a=a//10
if num==rev:
    print("NO is palindrome")
else:
    print("no is not palindrome")

'''



                            #PRIME NO programme#


'''
a=int(input("enter any no: "))
for i in range(2,a):
    if a%i==0:
        print("not prime no")
        break   
else:
    print("prime no")

'''
#................................pattern..................................................................#
                                       #1#

                                                                            
'''

                    1   
                    22
                    333
                    4444
                    55555

'''                      



'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print("\n")
print("pattern is printed")

'''

                                   #2#


'''

                  4444
                  55555
                  666666
                  7777777
                  88888888
                  999999999
                  10101010101010101010
                  1111111111111111111111


'''    

'''
for i in range(4,12):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")
print("pattern has been printed")

'''

                            #3#


'''
                          *
                          **
                          ***
                          ****
                          *****
                          ******
                          *******
                          ********
                          *********
                          **********

'''

'''
for i in range(1,11):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\n")
print("pattern has been printed")

'''

                                    #4#


'''

                       11111
                       2222
                       333
                       44
                       5


'''



'''
    
for i in range(1,6):
    for j in range(6,i,-1):
        print(i,end=" ")
    print("\n")
print("pattern has been printed ")


'''


                                #5#

'''

                               1
                               12
                               123
                               1234
                               12345
                               123456


'''

                     #method#


'''

for i in range(1,7):
    for j in range(1,i+1):
        print(j,end=" ")
    print("\n")
print("pattern has been printed")

'''

                                  #6#


'''

                          55555
                          4444
                          333
                          22
                          1

'''

                          #method#


'''

for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print("\n")
print("pattern has been printed ")


'''

                                   #7#

'''

                          55555
                          5555
                          555
                          55
                          5


'''

                           #method#

'''

for i in range(5,0,-1):
    for j in range(0,i):
        print(5,end=" ")
    print("\n")
print("pattern has been printed")

'''



                            #8#

                    #reverse pyramid of numbers#
                                                 


'''

1
21
321
4321
54321

'''
                               #method#

'''

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")
print("pattern has been printed")

'''

                              #9#

                #inverted half pyramid of numbers#

'''

                       012345
                       01234
                       0123
                       012
                       01
                       0


'''
                         #method#
                               
'''

for i in range(6,0,-1):
    for j in range(0,i):
        print(j,end=" ")
    print("\n")
print("Hurrey! Pattern has been printed ")

'''


                              #10#
                               
              # pyramid of in pattern of (1,3,5,7,9...) jumping one #

'''
                                1
                                111
                                11111
                                1111111
                                111111111

'''

                           #method#



'''

for i in range(1,7):
    if i==1:
        for j in range(1,i+1):
            print(1,end=" ")
        print("\n")
    elif i==2:
        for j in range(1,i+2):
            print(3,end=" ")
        print("\n")
    elif i==3:
        for j in range(1,i+3):
            print(5,end=" ")
        print("\n")
    elif i==4:
        for j in range(1,i+4):
            print(7,end=" ")
        print("\n")
    elif i==5:
        for j in range(1,i+5):
            print(9,end=" ")
        print("\n")
    elif i==6:
        for j in range(1,i+6):
            print(11,end=" ")
        print("\n")
    else:
        print("done with it")


'''

                                 #11#

                #reverse pattern of digits from 10#

                            #doubt#

'''       

                         1
                         234
                         56789


'''



                              #12#


'''
                             10
                             10 8
                             10 8 6
                             10 8 6 4
                             10 8 6 4 2

'''
                            
                            #method#

'''

k=9
for i in range(1,6):
    for j in range(10,k,-2):
        print(j,end=" ")
    print("\n")
    k=k-2
print("pattern has been printed")

''' 
    
           
                            #13#


'''

                          0
                          0 1
                          0 2 4
                          0 3 6 9
                          0 4 8 12 16
                          0 5 10 15 20 25
                          0 6 12 18 24 30 36

                          actually this is:

                          0            
                          0 1              (*1)
                          0 1 2            (*2)
                          0 1 2 3          (*3)
                          0 1 2 3 4        (*4)
                          0 1 2 3 4 5      (*5)
                          0 1 2 3 4 5 6    (*6)


''' 
 
                             #method#


'''

k=0
for i in range(0,7):
    for j in range(0,i+1):
        print(j*k,end=" ")
    print("\n")
    k=k+1

'''

                                 
                                 #14#

                    #pyramid of alternate Numbers#

'''
                          1
                          33
                          555
                          7777
                          99999

                          or
                          
                          1      (*1)
                          11     (*3)
                          111    (*5)
                          1111   (*7)
                          11111  (*9)

'''

'''

k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(1*k,end=" ")
    print("\n")
    k=k+2

''' 
                                  #Doubts#
                                    #15#
                                  
                          #right angle triangle pattern of numbers#

'''

                                       1
                                      12
                                     123
                                    1234
                                   12345


'''

                                 #Doubts#
                                   #16#
                      #equilateral triangle with stars#

'''

                                    *
                                   * *
                                  * * *
                                 * * * *
                                * * * * *
'''                        
#............................................................................................................#

                         #dictionary related important questions#

#............................................................................................................#

'''

a={"rishabh":"poet","golu":"DJ","sakshi":"traveller"}
       
                    #update the value of dictionary#


a["rishabh"]=56
a["golu"]=100
a["sakshi"]=98
print(a)

                     #add new key value pair to the dictionary#

b={"shweta":"cunning"}
c={"maddy":"flamboyant"}
d={"radhe":"bol"}
a.update(b)
a.update(c)
a.update(d)
print(a)

                        #delete key and value (with pop method) and print the value of deleted key#


e=a.pop("shweta")
f=a.pop("radhe")
print("deleted value of the key is:",e)
print("deleted value of the key is:",f)


                        #delete key and value with delete function(del())#


del a["maddy"]
del a["rishabh"]
print(a)

a["golu"]="great boy"
print(a)


for i in a.keys():
    print(i)

for i in a.values():
    print(i)

'''

                    #We want increament in this dictionary's values#
                    

'''


a={'a':10,'b':11,'c':12,'d':13,'e':14}
for i in a.keys():
    a[i]=a[i]+1
print("values of dictionary after updating by 1 is:",a)
print(a['a'])
print(a['b'])
print(a['c'])
print(a['d'])
print(a['e'])'

'''



                        #auto increment in the values of the dictionary#



"""
a={"amount1":100,"amount2":101}
print(a.keys()) #for printing keys of any dictionary
print(a.values()) #for printing values of any dictionary
print(a["amount1"]) #FOR PRINTing values of any dictionary
print(a["amount2"])


                  #auto incremented by 1#


'''                

for i in a.keys():
    a[i]=a[i]+1
print(a) #incremented by 1
print(a.values())

'''

                 #auto incremented by '2' #


'''
for i in a.keys():
    a[i]=a[i]+2
print(a)
print(a.values())

'''

"""


                            #dictionary auto incremented by string#
                            #adding wanted string to the wanted keys#


'''                               

a={"name":"rishabh kumar","school":"alphonsa"}
for i in a.keys():
    if a[i]=="rishabh kumar":
        a[i]=a[i]+" gupta"
    elif a[i]=="alphonsa":
        a[i]=a[i]+" high school"
    else:
        print("wrong")
print(a)


''' 

           
                            #This is a first way(of adding wanted string to the wanted key)#

'''
a={"name":"shweta","school":"alphonsa","crush":"Bhagyashree"}
b=a["name"]+" gandhi"
c=a["school"]+" high school"
s=a["crush"]+" bagal"
print(b)
print(c)
print(s)

'''


                        #now we will add wanted string to the key with for loop#



'''

a={"name":"shweta","school":"alphonsa","crush":"Bhagyashree"}
for i in a.keys():
    if a[i]=="shweta":
        print(a[i]+" gandhi")
    elif a[i]=="alphonsa":
        print(a[i]+" high school")
    elif a[i]=="Bhagyashree":
        print(a[i]+" bagal")
    else:
        print("wrong")

'''
#.........................................................................................................#
      

                     #import 'random' number from 'random' library and print random no between range#


'''
import random
a=random.random()
print(a)

#now print random no between given age#
b=random.randint(66,99)
print(b)

'''


                     #definition of lambda and some basic programme of it#


#definition-lambda is am anonymous function ,which can take multiple argument but can only have single expression#

'''
a=lambda a,b,c,d,e,f:a+b-c*d*e%f
print(a(1,2,3,4,5,6))

'''



                 #understanding "*args" and "**kwargs" with an example#

# *args=if we have any unnamed arguments,it will take *args(output will come in the tuples)
# **kwargs=if we have any named argument, it will take **kwargs(output will come in the dictionaries)
                         
                         #example 1#


"""

def maddy(*args,**kwargs):
    print(args)
    print(kwargs)
maddy(True,"rishabh","kumar","gupta",school="alphonsa",Town="prithvipur",district="niwadi")



                             #example 2#


def maddy2(*args,**kwargs):
    print(args)
    print(kwargs)
maddy2("rishabh","kumar","gupta",a="rishabh kumar gupta",fridge="Godrej")



                                #example 3#

def maddy3(*args,**kwargs):
    print(args)
    print(kwargs)
maddy3("sarika vishnoi","deepika birla",12,name="rishabh kumar gupta",language="python")

"""



                           #list slicing and list reversing#




'''
a=[1,2,3,4,5,6,7,8,9]
print(a[-1:-10:-1]) #list slicing
print(a[::-1])#list reversing

'''

                        #ASCII operations#

"""
# 1. To change "ASCII" code to "characters",we use 'chr()' function.
# 2. To change "character" to "ASCII" code ,we use 'ord()' function.

                 # To change 'characters' to 'ASCII" codes with ord() function#



a=input("enter any character:")
print("The ASCII value of this given character is:",ord(a))




                # To change 'ASCII' to 'Characters"  with  "chr()"" function#


a=int(input("enter any ASCII number:"))
print(" character of given ASCII number is:",chr(a))

"""
                            


                            #Floor division concept(//)#

#Definition-Floor division removes the floating point no and crashes the value to the next lowest value.

'''
a=11
print(a//2) #like normal division,output should be 5.5 but in floor division it removes the floating point value(.5) and crashes to the next  lowest value 5 #
#so the output is 5#

'''

'''
a=7
print(a//2)
#like normal division,output should be 3.5 but in floor division it would be 3 because "floor division" removes the floating value(.5) and crashing to the next lowest value which is "3".

'''
                                
                                  #tricky Floor division question#


# Q-what will be the out put of "-7//2" #

#Answer#---#in normal division output will be -3.5 but in "Floor division" answer will be -4#
#important#---#Because it removes the floating point value and crashes to the next lowest value#

                            #Some tricky examples#

'''
a=-7
b=-9
c=-11
print(a//2)
print(b//2)
print(c//2)

'''

                        #another tricky examples#
  #concept-if the value of "a" is lower than divider value then it will give "0" output#


'''
a=4
print(a//5)
b=10
print(b//11)
c=5
print(c//6)

'''

'''
a=9
print(a//3) #this will behave like normal "division" because there is no "floating no" include in it#
b=10
print(a//2)

'''


 
                            #Reverse string and string slicing#

#normal slicing# 

'''

a="HELLO WORLD"
b=a[:11]  #it starts from 0'th index and goes to the (-1) of the last index(10)#
c=a[:-1]  #it starts from 0'th index and goes to the 'one step before' (-1) of the last index (-2)#
d=a[:-3]
e=a[:-5]  #it will contain 'space also'#
f=a[:-6]
g=a[3:10]  #it will start from 3rd index and goes to 9th(-1) index#
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

'''

#reverse string with 'string slicing'#
'''
a="HELLO WORLD"
print(a[-1:-12:-1])

b= 'AEROPLANE'
print(b[-1:-10:-1])

'''

#Now we use short trick which will reverse everything like 'list','tuple','string' from last 'index' to the 'first one'#

                        #Formula is:  "[::-1]"#

                        #now reversing the string#


'''

a="HELLO WORLD"
b="AEROPLANE"
c="HAPPY BIRTHDAY"
d="JAY MATA DI"

print(a[::-1]) #it will start from "last index" and goes upto the "first index"#
print(b[::-1])
print(c[::-1])
print(d[::-1])

'''

                        #now reversing the list#


'''
a=[1,2,1,3,4,5,22,33,44,111,2,3,99,101,123,34,5,6,77,6,4,True,"Hello",False]
b=["Rishabh","kumar","gupta","alphonsa","high","school"]
print(a[::-1])
print(b[::-1])

'''

                         #now will reverse the tuple#

'''
a=(1,2,1,44,3333,222,555,66,22,3,4,5,"Hello",True)
print(a[::-1])

'''



                        #Programme of fabbonacci series to print to the nth term#


#what is fabbonacci series= 0,1,1,2,3,5,8,13,21,34,55,.......

#it means the next term of the series will be the adding of the previous two term#

# While the first two terms will always be '0,1' and thats the "key point"


'''

a=int(input("Enter till how many term you wanted to print:"))
n1=0
n2=1
if a<0:
    print("Please enter positive term")
elif a==1:
    print("fabbonacci series is :",n1)
else:
    while a>0:
        print(n1,end=" ")
        sum=n1+n2
        n1=n2
        n2=sum
        a=a-1
    print("\n"+"fabbonacci series is completed")

'''



              
                    #multipication operation with list,tuple#

#multipication operation is not applicable with 'set' and 'list'.

#if we mutiply list by any "digit" it will replicate himself by "digit times"#
#if we mutiply tuple by any "digit" it will replicate himself by "digit times"#

'''
a=[1,2,3]
print(a*2)  #it will replicate himself by 2 times#
print(a*3)  #it will replicate himself by 3 times#
print(a*8)  #it will replicate himself by 8 times#

'''


'''
a=(1,2,3)
print(a*2)  #it will replicate himself by 2 times#
print(a*3)  #it will replicate himself by 3 times#
print(a*8)  #it will replicate himself by 8 times#

'''



                     
                      #Programme to check "armstrong no"

# what is armstrong no?
# no which is sum of his digit power(if it's two digit then power=2,if it's 3 digit then power =3 and so on)

#examples-
# "0" and "1" are armstorng no because (0=0**1) and (1=1**1)
# "153" and "407" are armstrong no because (153=1**3+5**3+3**3) and (407=4**3+0**3+7**3)
# "1634" is a four digit armstrong no because(1634=1**4+6**4+3**4+4**4)

                                #programme#


'''

a=int(input("please enter a no which you wanted to check armstrong no or not :"))
original=a
b=len(str(a))
power=b
sum=0
while a>0:
    reminder=a%10
    sum=sum+reminder**power
    a=a//10
else:
    if sum==original:
        print("This is armstrong no:")
    else:
        print("This is not armstrong no:")


'''

#************************************************************************************************************#                                      

                                             #list operations#
                            # We will ask user to input element in the "list"#
                            #Then we will declare highest,second highest,third highest etc#

# sort() function is only available in "list" not in "tuple"
# sort() function always ascend a list but it should only be in "int" or "boolean" or "string"

# example

'''
a=[1,4,1,5,22,3,4,22,3,4,5]
a.sort()
print(a)
b=["rishabh","kumar","ambedkar"]
b.sort()
print(b)

c=["rishabh",1,2,3,4,5,True]
c.sort() #this will not sort,because "multiple datatype" are present in this list
print(c)

'''

                        #now finding the "second-highest" of the list#

                                #for integer#

                            

'''
l=[]
a=int(input("Enter how many element you wanted to enter in a list:"))
for i in range(1,a+1):
    b=int(input("enter the element :"))
    l.append(b)
    l.sort()
print("after sorting ascending order of the list is:",l)
print("highest element of the list is:",l[a-1]) #because indexing is starting from 0th index so highest value will be at(a-1)th index#
print("minimum element of the list is:",l[0])
print("second highest value of this list is:",l[a-2])
print("third highest element of the list is:",l[a-3])
print("highest element of the list is:",l[a-4])

'''


                               #for string#


'''

l=[]
a=int(input("Enter how many element you wanted to enter in a list:"))
for i in range(1,a+1):
    b=input("enter the element :")
    l.append(b)
    l.sort()
print("after sorting ascending order of the list is:",l)
print("highest element of the list is:",l[a-1]) #because indexing is starting from 0th index so highest value will be at(a-1)th index#
print("minimum element of the list is:",l[0])
print("second highest value of this list is:",l[a-2])
print("third highest element of the list is:",l[a-3])
print("fourth highest element of the list is:",l[a-4])

'''

# "len()" is an inbuilt function and it is a function of "list","set","tuple" and "dictionary" #

'''
a=[1,2,3,4,5,6]
b=(1,2,3,4,5,6)
c={1,2,3,4,5,6}
d={"name":"rishabh","school":"alphonsa"}
print(len(a))
print(len(b))
print(len(c))
print(len(d))

'''


           
                            #shuffling a list with 'shuffle()' function#
                              
            #each time when we print it ,it will give random shuffling output#
            # "shuffle()" function comes under "random" module #


'''

from random import shuffle
a=['hello','hi','ram-ram',1,2,3,4,5,6,7,8,False,True]
shuffle(a)
print(a)
b=[1,2,3,4,5,6,7,8,9,10]
shuffle(b)
print(b)

c=[1,2,3,4,6,7,8,9,10,13,4,5,"hello","hi","rishabh kumar gupta",True,False]
shuffle(c)
print(c)

'''

                                 
                                  #swapping of elements of list#


"""

l=[]
a=int(input("enter how many element you want to input in a list :"))
for i in range (1,a+1):
    b=int(input("please enter element :"))
    l.append(b)
 
'''
temp=l[0]
l[0]=l[a-1]    #This logic belongs to swapping "first" and "last" element of the list#
l[a-1]=temp
'''
'''
temp=l[1]
l[1]=l[a-2]     #This logic belongs to swapping 'second lowest' and "'second highest'  element of the list#
l[a-2]=temp
'''

'''
temp=l[1]
l[1]=l[2]      #This logic belongs to swapping 'second' and 'third'  element of the list#
l[2]=temp

'''

'''
temp=l[0]
l[0]=l[1]      #This logic belongs to swapping 'first' and 'second'  element of the list#
l[1]=temp

'''


'''
temp=l[2]
l[2]=l[3]      #This logic belongs to swapping 'third' and 'fourth'  element of the list#
l[3]=temp

'''

#print("After swapping first and last element of the list, list will be:",l)
#print("After swapping 'second ' and 'second last' of the list, list will be:",l)
#print("After swapping 'second ' and 'third' element of the list, list will be:",l)
#print("After swapping 'first' and 'second' element of the list, list will be:",l)
#print("After swapping 'third' and 'fourth' element of the list, list will be:",l)
 
"""
                              
                                        
                            #sorting list without sort() inbuilt function#

#in all data type like 'list','tuple','set','dictionary' we can only short "list" with or without "sort()" inbuilt funtion# 
#in other way we can say "sorting" is only "available" in "list" only#


                            #sorting a given list(for int) without sort() inbuilt function#

'''
a=[45,333,1,222,5,66666,7,88,22,1,5555,6,76555,3456,7,8,999,7,33,3333,0000,7,452,254,756363]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("list after sorting without sort() inbuilt function is :",a)

'''


 
                  #now we will create a list and then sorting it(for int) without sort() inbuilt function#


'''
l=[]
a=int(input("enter how many element you want to enter in a list :"))
for i in range(1,a+1):
    b=int(input("Please enter element:"))
    l.append(b)
#now we will sort list "l"
for j in range(len(l)):
    for k in range(j+1,len(l)):
        if l[j]>l[k]:
            l[j],l[k]=l[k],l[j]
print("list after sorting without sort() inbuilt function is :",l)

'''

                         #sorting a given list(for string) without sort() inbuilt function#

'''
a=['gupta','bagal','agrawal','rishabh','bhagyashree','aman','ravi','kag']
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print("list after sorting without sort() inbuilt function is :",a)

'''

                                # all important operation on list(for integer) #
                             
        #1   #now we will create a list and then sorting it(for string) without sort() inbuilt function#
        #2   #perform multiple operations like finding 'highest','lowest','second-highest','second-lowest'#
        #3   #swapping list element #



"""

l=[]
a=int(input("enter how many element,you want to enter in a list :"))
for i in range(1,a+1):
    b=input("please enter 'string' element :")
    l.append(b)
print("without sorting list is :",l)
#now we will sort() list without sorting inbuilt function, "sort()" #
for j in range(len(l)):
    for k in range(j+1,len(l)):
        if l[j]>l[k]:
            l[j],l[k]=l[k],l[j]
print("list after sorting without inbuilt function 'sort()' is :",l)
print("second highest element of the list is :",l[a-2])
print(" highest element of the list is :",l[a-1])
print("lowest element of the list is :",l[0])
print("second lowest element of the list is :",l[1])

'''
temp=l[0]
l[0]=l[a-1]  #logic of swapping 'first' element with 'last' one#
l[a-1]=temp

'''

'''
temp=l[1]
l[1]=l[a-2]   #logic of swapping 'second ' element with 'second last' one#
l[a-2]=temp
'''

'''
temp=l[0]
l[0]=l[1]
l[1]=temp

'''
#print("after swapping 'first' and 'last' element of the list :",l)
#print("after swapping 'second' and 'second-last' element of the list :",l)
#print("after swapping 'first' and 'second' element of the list :",l)


"""


                                    
                                   #list#(operation for integer)

                    # first we will create list by asking user # 
                    # Then we will sort it #
                    # Then we will declare 'highest','second highest','lowest','second lowest' #
                    # Then we will swap list element respectfully #


"""

l=[]
a=int(input("enter how many element you want to enter in list:"))
for i in range(1,a+1):
    b=int(input("please enter elements :"))
    l.append(b)
print("List without sorting is :",l)

#now we will do sorting without "sort()" inbuilt function #

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print("list after sorting is :",l)

# now we will find out second highest and lowest and so on....... #
#it will be only done after "sorting" because "sorting" done list in the ascending order so it will be easy with the help of indexing to find out "greater" and "lesser" #
print("Highest element  of the list is: ",l[a-1])
print("second highest element of the list is: ",l[a-2])
print("third highest element of the list is :",l[a-3])
print("lowest elelment of the list is :",l[0])
print("second lowest of the list is: ",l[1])
print("third lowest element of the list is: ",l[2])
print("fourth lowest element of the list :",l[3])

#  now we will swapping list element with the help of indexing  #

'''
temp=l[0]
l[0]=l[a-1]    #logic of swapping "first" and last element of the list #
l[a-1]=temp
'''

'''
temp=l[1]
l[1]=l[a-2]     #logic of swapping "second" and "second-last" element of the list #
l[a-2]=temp

'''
'''
temp=l[0]
l[0]=l[1]      #logic of swapping "first" and "second" element of the list #
l[1]=temp

'''

#print("after swapping first and last element of the list ,list will be: ",l)
#print("after swapping 'second' and 'second last' element of the list ,list will be: ",l)
#print("after swapping 'first' and 'second ' element of the list ,list will be: ",l)


"""

 
#***********************************************************************************************************#                  
                                  #programmes#

                            #Find out vowels in string#


'''
a=input("Enter any string in which we want to count vowels :")
vowels=0
for i in a:
    if(i=="a"or i=="e"or i=="i" or i=="o"or i=="u"or i=="A"or i=="E"or i=="I"or i=="O"or i=="U"):
        vowels=vowels+1
print("total no of vowels in this string is:",vowels)

'''


                                #important#

       #find out that first character of a string is a "numerical" or "character"#



'''

a=input("Enter any string :")
b=a[0]
if b.isalpha()==True:
    print("first character is alphabet")
elif b.isdigit()==True:
    print("first character of a string is numeric")
else:
     print("first character is neither a 'numeric' nor a 'alphabet' ,it is a 'special character' ")


'''


               






















