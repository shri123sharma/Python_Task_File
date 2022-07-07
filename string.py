"""
text="Lists and Strings can be accessed via indices!{}"

print(text[10])
print(text[18])
print(text[-1])
print(text[-10])

print(text[10:17])
print(text[:20])
print(text.capitalize())
print(text.endswith("indices!"))
print(text.casefold())
#print(text.center("100","#"))
print(text.count("s"))
print(text.encode)
#print(text.expandtabs("8"))
print(text.find("Strings"))
print(text.format("shrikant"))
print(text.index("can"))

string_1="shrikant11212"

print(string_1.isalnum())

num_1="784782478"
print(num_1.isdecimal())
print(num_1.isidentifier())
print(num_1.isnumeric())


name_1="Shrikantrisabhajay"
print(name_1.islower())
print(name_1.isspace())

empty_1=""
print(empty_1.isprintable())

list_1=["1","23","4","5","6","7","7",]
string_1=""

S=string_1.join(list_1)
print(S)

# Python program to demonstrate the
# use of join function to join list
# elements with a character.
  
list1 = ['1','2','3','4'] 
  
s = "-"
  
# joins elements of list1 by '-'
# and stores in sting s
s = s.join(list1)
  
# join use to join a list of
# strings to a separator s
print(s)
a=2232
b=24242
print(a+b)

string_1="what are you doing man"
print(len(string_1))
print(string_1.lower())

print(string_1.lstrip(","))
print(string_1.partition("you"))
print(string_1.replace("man","women"))
print(string_1.rfind("are"))

s="shrikant"
print(type(s))
print(len(s))

# string="my name is shrikant sharma i belong to narsingapur district.i am last six month staying."
string="restart"
str_1=""
for i in string:
    str_1=i+str_1
print(str_1)

string="restart"
char=string[0]
print(char)
string=string.replace(char, "$")
print(string)
string=char+string[1:]
print(string)

str_1="restart"
char=str_1[3]
print(char)
str_1=str_1.replace(char, "*")
print(str_1)
str_1=str_1[0:3]+char+str_1[4:]
print(str_1)
"""


a = [1,4,2,9,7,5]
b = []

while a:
    min = a[0] 
    for i in a: 
        if i < min :
            min = i
            b.append(min)
            a.remove(i)
print(b)

