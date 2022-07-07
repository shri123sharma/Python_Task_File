from tkinter import*
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()

    if username=="" and password=="":
        messagebox.showinfo("","BLANK NOT ALLOWED")
    elif username=="shrikant" and password=="shri123":
        messagebox.showinfo("","LOGIN SUCESSFULLY")
    else:
        messagebox.showinfo("","BOTH ARE WRONG")
    

root=Tk()
root.geometry("500x400")
root.title("LOGIN PAGE")

#c1=root.configure(background="black").place()

global entry1
global entry2

l1=Label(root,text="username",bg="red",bd=5,width=20).place(x=20,y=30)
l2=Label(root,text="password",bg="red",bd=5,width=20).place(x=20,y=60)

entry1=Entry(root,bd=5,width=30).place(x=200,y=30)
entry2=Entry(root,bd=5,width=30).place(x=200,y=60)

b1=Button(root,text="login",command=login,bd=5,height=3,width=13)
b1.place(x=200,y=200)
root.mainloop()


