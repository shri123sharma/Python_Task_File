from tkinter import*
from PIL import Image,ImageTk



def PharmacyManagementSystem():
        
    root=Tk()
    root.title("PHARMACY MANAGEMENT SYSTEM")
    root.geometry("1500x800")
    root.iconbitmap("C:/Users/pc/Desktop/pharmacy project image/pharmacy.ico")

    lbltitle=Label(root,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                            bg="black",fg="white",font=("times new roman",50,"bold"),padx=2,pady=4)
    lbltitle.pack(side=TOP,fill=BOTH)

    

img1=Image.open("C:\\Users\\pc\\Desktop\\pharmacy project image\\Logo Medical.jpg")
img1=img1.resize((80,80),Image.ANTIALIAS)
self.photoimg1=ImageTk(img1)
b1=Button(self.root,Image=self.photoimg1,borderwidth=0)
b1.place(x=70,y=20)



dataframe=Frame(root,bd=15,relief=RIDGE)
dataframe.place(x=0,y=120)




obj=PharmacyManagementSystem()
root.mainloop()
