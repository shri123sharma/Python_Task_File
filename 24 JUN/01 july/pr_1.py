from datetime import datetime
f = open("demofile.txt","w")
d=datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
f.write(f"current time{d}")

f = open("demofile.txt", "r")
print(f.read())

# f1=open('file_1','w')
# d=('hello world')
# f1.write(f"welcome to{d}")

# f1.open('file_1','r')
# print(f.read())

