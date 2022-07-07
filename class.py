"""
class parent():

    var_1="hello"
    var_2="hi"

    def add(self):

        print("shrikant",self.var_1)
        print("ajay",self.var_2)

obj_1=parent()
print(obj_1.var_1)
obj_1.add()

class person:

    def __init__(self,name):

        self.name=name

    def add_msg(self):

        print("this is person name",self.name)

obj=person("shrikant")
obj.add_msg()

class parent:

    name="mohan"

    def __init__(self,occupation,city):

        self.occupation=occupation
        self.city=city

obj=parent("teacher","dhanbaad")
print(obj.name)
print(obj.city)
print(obj.occupation)

class dog:

    animal="dog"

    def __init__(self,breed):

        self.breed=breed

    def setcolor(self,colour):

        self.colour=colour

    def getcolor(self):

        return self.colour
obj=dog("pug")
obj.setcolor("black")
print(obj.getcolor())

class demo():

    def __init__(self):

        self.name="laptop"
        self.brand="hp"
        self.price="25000"

    def inform(self):

        print(self.name)
        print(self.brand)
        print(self.price)

obj=demo()
obj.inform()

class addition():

    first=100
    second=200
    third=300

    def __init__(self,f,s):

        self.f=f
        self.s=s

    def display(self):

        print("this is first",self.f)
        print("this is second",self.s)
        print("this both are added",self.f+self.s)

obj=addition(1000,2000)
obj.display()

class index():

    def __init__(self,a,b):

        self.a=a
        self.b=b
    def __del__(self):

        print("both are instance variable in delete",self.a,self.b)

obj=index(100,200)
del obj

class delete():

    def __init__(self):

        print("employee created")

    def __del__(self):

        print("destructor is called")

    def index(self):
        print("making function")
obj=delete()
print("this is class object",obj)

a=obj.index()
print("after a index function",a)
del a

class demo():

    def __init__(self):

        self.a=100
        self.b=200

    def add(self):

        return self.a+self.b

obj=demo()
print(obj.add())

class parent():

    name='encoresky technology'
    loaction='indore'

    def __init__(self,area,work):

        self.area=area
        self.work=work

obj=parent("viajaynagar",'frontented')
print(obj.name)
print(obj.work)

class demo():

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def add(self,c,d):

        self.c=c
        self.d=d
        return self.a+self.b

    def getvalue(self):
        return self.c-self.d

obj=demo(10,20)
obj.getvalue()
print(obj.getvalue())

class demo():

    def __init__(self):

        self.name="indore"
        self.state="madhya pradesh"

    def call(self):
        return self.name+self.state

obj=demo()
print(obj.call())


class index():

    def __init__(self,a,b):

        self.a=a
        self.b=b

    def display(self):

        print("first value is",self.a)
        print("second value is",self.b)
        print("both are value",self.answer)
    def calcualte(self):
        self.answer=self.a+self.b
obj=index(1000,20000)
obj.calcualte()
obj.display()

class Demo_1:

    def __init__(self):

        print("variable are created")
        self.name="shri"
        self.age='24'

    def __del__(self):

        print("variables are deleated")
obj=Demo_1()
del obj

class demo_2:

    def __init__(self,name,location):

        print("variable is craeted")
        self.name=name
        self.location=location

    def __del__(self):

        print("del is deleted for complete execution")

    def show(self):

        print("first variable is show",self.name)
        print("second variable is show",self.location)
        print("third is both add",self.add)

    def both(self):

        self.add=self.name+self.location
        return self.add
obj=demo_2("shrikant","indore")
print(obj.show())
print(obj.both())

l=[]

for i in range(1,10):

    if i%2==0:
        l.append(i)
print(l)

list=[i for i in range(1,10) if i%2==0]
print(list)

dict={i:i*i for i in range(1,10)}
print(dict)

def add():

    for i in range(1,10):
        yield i*i

a=add()
print(next(a))
print(next(a))
print(next(a))

list=iter([1,2,3,4,5,7])
print(next(list))

list=[10,20,30,40,50,60]
for i in range(len(list[::-1])):
    print(i)
class parent():

    def __init__(self,name,age):

        self.name=name
        self.age=age

    def both(self):

        print("this is name",self.name)
        print("this is age",self.age)
    def add(self):

        print("both argument is concetaination",self.name+self.age)

object=parent("shrikant",'24')
object.both()
object.add()

class parent():

    def __init__(self,name,age):

        self.name=name
        self.age=age
    
    def show(self):

        print("this is first name",self.name)
        print("this is second age",self.age)
class child(parent):

    def __init__(self,name,age,firstname,lastname):

        self.firstname=firstname
        self.lastname=lastname
        parent.__init__(self,name,age)
    
obj=child('shri','24',"shrikant",'sharma')

obj.show()

class Demo_1():

    def __init__(self,firstname):

        self.firstname=firstname

class Demo_2():

    def __init__(self,lastname):

        self.lastname=lastname

class Index_1(Demo_1,Demo_2):

    def __init(self,firstname,lastname):

        Demo_1.__init__(self)
        Demo_2.__init__(self)
    def add(self):

        print(self.firstname+self.lastname)
object=Index_1("shrikant","sharma")
object.add()

class parent():

    def __init__(self):

        self.name="shrikant"

    def get_name(self):

        return self.name

class child(parent):

    def __init__(self):
        parent.__init__(self)
        self.name="shrikant"
        self.surname="sharma"

    def get_surname(self):

        return self.surname
class grandchild(child):

    def __init__(self):
        child.__init__(self)
        self.name="shrikant"
        self.surname="sharma"
        self.age="24"

    def get_age(self):

        return self.age

obj=grandchild()
print(obj.get_name(),obj.get_surname(),obj.get_age())

class parent(object):

    def __init__(self,name):

        self.name=name
    def show(self):

        return self.name

class child(parent):

    def __init__(self,name,surname):
        parent.__init__(self,name)

        self.surname=surname
    def show_1(self):

        return self.surname
object=child("shrikant","sharma")
print(object.show())
print(object.show_1())

class father():

    def __init__(self,fname):

        self.fname=fname

    def view(self):

        return self.name

class mother():

    def __init__(self,fname,mname):
        father.__init__(self,fname)
        self.mname=mname

    def view_1(self):

        return self.mname
    
class son(father,mother):

    def __init__(self,fname,mname,sname):
        mother.__init__(self,fname,mname)
        self.sname=sname

    def view_2(self):

        return self.sname
obj=son("mahendra sharma","neelam sharma","shrikant sharma")
print(obj.view())
print(obj.view_1())
print(obj.view_2())
     
class parent():

    def __init__(self):

        self.name="ajay"
        self.age="25"

    def show(self):

        return self.name+self.age
object=parent()
print(object.show())

class demo():

    name="shrikant"

    def __init__(self):

        self.age="24"
        self.height="6.1"

    def show(self):

        return self.age+self.height
obj=demo()
print(demo.name)
print(obj.show())

class parent():

    name="shrikant sharma"

    def __init__(self,age,height):

        self.age=age
        self.height=height
        print(self.age+self.height)

    def setoccupation(self,occupation):

        self.occupation=occupation
        print("my work is ",self.occupation)
    
    def city(self,home,currentstay):

        self.home=home

        self.stay=currentstay

        print("this is hometown",self.home)
        print("this is current stay",self.stay)

obj=parent("24","5.9")

obj.setoccupation("student")
obj.city("bateshra","indore")

class index:

    def __init__(self,name,city):

        self.name=name
        self.city=city

    def show(self):

        return self.name+self.city

obj=index("madhya pradesh","indore")
print(obj.show())
"""
class parent(object):

    def __init__(self,name):

        self.name=name

    def show(self):

        return self.name

class child(parent):

    def __init__(self,name,college,university):
        
        self.college=college
        self.university=university

        parent.__init__(self,name)

    def show_1(self):

        return self.college+self.university
obj=child("shrikant","sirts","rgpv")
print(obj.show())
print(obj.show_1())\

list=[1,2,3,4,5,7,8,9,10]

for i in list:

    if i%2==0:
        print("this is even number",i,end=",")

class base():

    def __init__(self):

        self._name="shrikant"

class derive(base):

    def __init__(self):
        base.__init__(self)
        print("this is prtected first member",self._name)

        self._name="ajay"
        print("second one in modify data",self._name)
obj_1=derive()
obj2_2=base()







    








        

    

