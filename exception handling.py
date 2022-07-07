# variable=100

# if 0<variable

# print(variable)
# marks=1000

# a=marks/0
# print(a)

def add(a,b):

    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("zero divsion error a/b=0")
    
    else:
        print(c)
add(10,20)

a=[1,23,4]

try:
    print("this is first element in accss%d"%(a[1]))

    print("this is third element in access%d"%(a[3]))

except:
    print("this is error in generate")


def divide(a,b):

    try:
        result=a//b
        print("this is proper execute the code%d"%(result))

    except ZeroDivisionError:

        print("this is error occured")
    else:
        print("this is correct execution in try blog")
divide(3,0)

def list_1(n):

    try:
        sum=0
        for i in range(0,n):
            total=sum+i
            sum=total+i
            print("this is sum in list",sum)
    except RuntimeWarning:

        print("this is run time warning")
    else:
        print("execuation is completed")
list_1(10)

a=10
b=20

try:
    c=a//b
    print("this is complete")
except ZeroDivisionError:

    print("this is raise error generate")
else:

    print("this is try blog in coplete execute")
finally:

    print("both try and except blog in right and wrong")
        
a=1000
b=200

result=a+b
if result<100:
    print(result)

a=100
b=1

result=a//b
print(result)

list=[1,2,3,4,5,6]
list.index(4)
print(list)

try:
    amount=500

    if amount<2000:

        raise ValueError("please add the more money in your account")

    else:
        print("if you are eligiable in dsa question in open")

except ValueError as e:

    print("this is exception in this code")

