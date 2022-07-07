"""
#user defined dictionary#
dict_1=dict({"name":"shrikant","age":24,"location":"indore","country":"india"})
print(dict_1)

dict={"india":3231212121,
      "china":23231212212,
      "america":121323232,
      "frnce":2113121212,
}
print(dict)
print(type(dict))

detail={"name":"johan",
        "age":23,
        "company":"google",
        "salary":"24000",

}
print(type(detail))
print("if name is access the dict%s"%detail["name"])
print("age is access%s"%detail["age"])
print(detail)
print(detail["name"])
print(detail["age"])

for i in detail:
    print(i)

#print(detail["name1"])
detail["location"]="indore"
print(detail)

dict_1={"item":"milk","food":"daal","breakfast":"poha","price":120,"breakfast":"samosa"}
print(dict_1)
for key in dict_1:
    print(key)

for value in dict:
    print(value)

from re import T


dict_1={"item":"milk","food":"daal","breakfast":"poha","price":120,"breakfast":"samosa"}
print(dict_1.get("breakfast"))
print(dict_1.get("item"))
print(dict_1.get("price"))
print(dict_1.get("food"))

#dict_2={[1,2,3,4,5]:"100 to 80 marks"}
#print(dict_2)
d=dict_1["item"]="doodh"
print(d)
print(dict_1)

dict_3={"name":"python","fees":8000,"duration":"2months"}
print(dict_3["name"])
for i in dict_3:
    print(i)
    print(dict_3[i])

dict_4={1:"tcs",2:"ifosys",3:"wipro",4:"byjuice"}

for i in dict_4:
    print(i)
    print(dict_4[i])

for key in dict_4:
    print(key)
    print(dict_4[key])

dict_1={"name":"shrikant","age":24,"loaction":"indore","country":"india"}
print(dict_1["country"])
print(dict_1["loaction"])
print(dict_1["name"])

dict_2={1:"china",2:"india",3:"america",4:"russia"}
print(type(dict_2))
print(dict_2.get(3))
print(dict_2.get(1))
print(dict_2.get(4))

dict_3={"cloths1":"shirt","cloths2":"pants","cloths3":"tshirt","sunglass":"blackgogle"}
for i in dict_3:
    if i=="cloths3":
        continue
    print(i)
    print(dict_3.get(i))

dict_4={"item1":"daal",
        "item2":"milk",
        "item3":"curd",
        "item4":"haldi",
}

for i in dict_4:
    print(i)
    print(dict_4[i])

for i in dict_4.keys():
    print(i)

for i in dict_4.values():
    print(i)

dict_5={"name":"","age":"","district":"","state":""}
dict_5["name"]="soni"
dict_5["age"]="25"
dict_5["district"]="jaunpur"
dict_5["state"]="uttar pradesh"
print(dict_5)

dict_6={"company":"tcs",
        "employee":100000,
        "work":"It",
        "location":"india",
        "owner":"ratn tata",

}
dict_6.items()
print(dict_6)

for i,n in dict_6.items():
    if i =="work":
        break
    print(i,n)

print(dict_6[1])

from ast import Compare
from distutils.errors import DistutilsClassError


dict_a={"temple1":"shridi sai baba",
        "location1":"shridi",
        "temple2":"somnath",
        "location2":"gujrat",
        "temple3":"ramesvaram",
        "location3":"south",
}

del dict_a["temple3"]
print(dict_a)

del dict_a["location3"]
print(dict_a)

print(dict_a.pop("location2"))
print(dict_a)

print(dict_a.pop("temple1"))
print(dict_a)

del dict_a["location1"]
print(dict_a)

print(dict_a.pop("temple2"))
print(dict_a)

dict_a.update({"state":"madhya pradesh"})
dict_a.update({"capital":"bhopal"})
dict_a.update({"state1":"uttar pradesh"})
dict_a.update({"capital1":"lucnow"})
print(dict_a)

dict_b={}
dict_b["companyname"]="wipro"
dict_b["total employee"]="100000"
dict_b["turn over"]="billions"
dict_b["company value"]="100000cr"

print(dict_b)    

dict_c={"mp cm":"shivraj singh","up cm":"yogi adityanath","delhi cm":"arvind kejriwal"}

for i in dict_c:
    print(i)
    print(dict_c[i])
        
for i in dict_c.keys():
    print(i)

for i in dict_c.values():
    print(i)

dict_d={1:["shrikant","24","indore"],2:("india","1997","kareli"),3:{"state","madhya pradesh","country","india"},
}
print(dict_d)
print(dict_d[1])
print(dict_d.get(2))
print(dict_d.keys())
print(dict_d.values())
print(dict_d.items())
del dict_d[1]
print(dict_d)

print(dict_d.pop(2))
print(dict_d)
print(dict_d.pop(3))

dict_e={1:"laptop",2:"mouse",3:"keyboard",4:"earphone",5:"ssd",6:"ram"}
dict_f={10:"wheat",20:"dhaan",30:"chana",40:"masoor",50:"ghana"}

print (dict_e,dict_f)
print(len(dict_e))
s=str(dict_e)
print(s)

company={
    "employee1":{"name1":"mohan","age1":"24","salary1":10000,"department1":"deploy"},
    "employee2":{"name2":"sohan","age2":"32","salary2":20000,"department":"testing"},
    "employee3":{"name3":"ram","age":"29","salary3":30000,"department":"production"},

}

print(company)
print(company["employee1"]["salary1"])
# p=company.get("employee2"("name2"))
company["employee1"]["name1"]="shyam"
print(company)

del company["employee2"]["department"]
print(company)

for i in company:
    print(i)
    print(company[i])

for i,n in company.items():
    print(i,n)

company.pop("employee1"("salary1"))
print(company)

from optparse import Values


list=[1,2,3,4,5,5]
string="shrikant sharma"

print(enumerate(list))

dictionary={'1':'shri','2':'ajay','3':'arun'}

for Keys,Values in enumerate(dictionary):

    print(Keys,Values)

list=['eat','food','daal']

for i in enumerate(list,100):

    print(i)



list_1=[]

list_1.append(10)
list_1.append(2.7)
list_1.append("sharma")
list_1.append(True)

print(list_1)

dict_1={'name':'shrikant','age':24,'loaction':'indore'}
print(type(dict_1))
print(dict_1)

dict_2={'company':'infosys','list':[1,2,3,4,5,6,7],'tuple':("indore","bhopal","jaipur"),'set':{10,20,30,40,50}}
print(type(dict_2))
print(dict_2)

dict_3=dict({1:'shrikant',2:'ajay',3:'risabh'})
print(type(dict_3))
print(dict_3)

dict_4={1:'madhya pradesh',2:'haryana',3:'punjab',4:{"capital_1":"bhopal",'capital2':"chandigarh",'capital3':"amritsar"}}
print(dict_4)

dict_5={
    'name':'shrikant',
    'age':24,
    'location':'indore',
    'state':'madhya pradesh',
}

dict_5['country']='india'
print(dict_5)

dict_6={}

dict_6['name']='risabh'
dict_6['age']=24
dict_6['location']='jhansi'
dict_6['country']='india'
dict_6['age']=28
print(dict_6)
print(dict_6['name'])
print(dict_6.get('age'))

dict_7={1:{'name':'ajay','company':'bridgefix'},2:{'name':'sarika','company':'tcs'}}
print(dict_7[1]['name'])

dict={1:'shri',2:'kant',3:'hello',4:'hii'}

dict.pop(1)
print(dict)

dict.popitem()
print(dict)
"""
dict={1:'shri',2:'kant',3:'hello',4:'hii'}
dict.get(1)
print(dict)

dict[5]="nice"
print(dict)

dict[5]='hello world'
print(dict)

print(dict[1])
print(dict.get(3))

del dict[4]
print(dict)

print(dict.pop(1))
print(dict)

dict.popitem()
print(dict)

dict_1={'name':'john','age':24,'salary':'25000','company':'google'}

for i in dict_1.pop('name'):
    print(i)


    


    


