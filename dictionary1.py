"""
this_dict={
    "name":"shrikant",
    "age":"24",
    "location":"indore",
    "list":[1,2,3,4,5,6,7,8],
    "tuple":(1,2,3,4,5,6,6),
    "set":{100,200,300,400,500},
    "dict":{"country":"india","capital":"delhi"},
    "name":"rahul",

}

print(this_dict)

print(type(this_dict))

print(this_dict["name"])

print(len(this_dict))

access=this_dict["set"]
print(access)
print(this_dict.get("set"))

print(this_dict.keys())

change=this_dict["list"]=[1000,2000,3000,400,50000]
print(change)
print(this_dict)

update=this_dict.update({"age":"25"})
print(update)
print(this_dict)

update_1=this_dict.update({"int":"1,2,3,4,5,6,7"})
print(this_dict)
print(update)


dict_2={

    "company":"tcs",
    "employee":100000,
    "service":"It",
    "owner":"ratan tata",

}

p=dict_2.pop("employee")
print(p)
print(dict_2)

pi=dict_2.popitem()
print(dict_2)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price":1000000
}

for i in thisdict:

    print(i)
for i in thisdict:
    print(thisdict[i])
for values in thisdict.values():
    print(values)

mydict=thisdict.copy()
print(mydict)

my_dict=dict(mydict)
print(my_dict)

my_family={
    "child1":{
        "name":"mohan",
        "age":24,
        "work":"student",
    
    },
    
    "child2":{
        "name":"sohan",
        "age":23,
        "work":"bussiness",
    },

    "child3":{
        "name":"ram",
        "age":27,
        "work":"farming",
    },
    
} 

print(my_family)

print(my_family["child1"]["name"])

my_family["child1"]["name"]="shyam"
print(my_family)

list=[1,2,3,4,45,67,7,88]
obj1=enumerate(list)
print(obj1)

list_1=["mohan","sohan","ram","shyam"]
for i in enumerate(list_1,100):
    print(i)

for i,v in enumerate(list_1):
    print(i,v)

for i,v in enumerate(list_1):
    print(i)
    print(v)

def fun(a,b):

    return a+b
print(fun(10,20))

def fun_1(a):
    for i in a:
        yield i
obj1=fun_1([1,2,3,4,5])
print(next(obj1))
print(next(obj1))

def func_1(n):

    for i in range(2,n):
        if n%i==0:
            print("Not A Prime Number")
            break
    else:
        print("Prime Number")
func_1(11)

def func_2():
    n=10
    yield n
    n=n*n
    yield n
obj1=func_2()
print(next(obj1))
print(next(obj1))

def fun(n):

    yield n
obj1=fun([1,2,3,4,5,5])
print(next(obj1))

n=5

for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1 or j==0 or j==n-2:
            print("*"+"",end="")
        else:
            print("  ")
print()

def fun():
    l=[]
    for i in range(1,21):
        i=i**2
        l.append(i)
    print(l[:5])
    print(l[-5:])
fun()

n=6
for i in range(1,n+1):

    for j in range(i,n+1,-1):
        
        print(j,end="")
    print()
row=5
col=row
for i in range(row,0,-1):
    for j in range(0,i):
        print(j,end="")
    print("")

row=5
for i in range(1,n):
    if i%2!=0 or i%2==0:
        for j in range(i):
            print(i,end=" ")
    print("")

row=5
for i in range(row,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print("")

integer=1212
string="shrikant"
float=1.8989

print("this is hash value integeer",str(hash(integer)))
print("this is string hash value",str(hash(string)))
print("this is float hash value",str(hash(float)))

tuple=(1,2,3,4,5,6,8)
print(hash(tuple))

# list=[1,2,3,45,6,6,7,8]
# print(hash(list))

n=2
tuple=(n)
print(tuple)
n = int(input("if"))
integer_list = map(int, input("if").split())

print(n)
print(integer_list)
print(hash(n))
t=(integer_list)
print(type(t))
"""
name="harry"
score=242.3
grade="A+"
list=[]
list.append([name,score,grade])
print(list)

for i in list.append([name,score]):
    print(i)