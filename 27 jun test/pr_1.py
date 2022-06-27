s1="Ram goes to  the    school      daily."
l1=[]
s3=" "
print(type(s1))
s2=(s1.split(" "))
# print(s2)
for i in s2:
    if i not in "":
        l1.append(i)
s3=s3+" ".join(l1)
print(s3)

# for j in l1:
#     print(j)
#     s3+=j
#     # ' '.join(l1) 
# print(s3)

# s2=s1.split(",")
# print(s2)
# for i in s2:
#     if i==" ":
#         s2.remove(i)
#         "".join(s2)
# print(s2)

            
    
       

        