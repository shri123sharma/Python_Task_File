from tkinter import*
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class Registration:

    def __init__(self,root):
        self.root=root
        self.root.title("PATIENT MEMBER REGISTRATION SYSTEM")
        self.root.iconbitmap("C:/Users/pc/Desktop/pharmacy project image/pharmacy.ico")
        self.root.geometry("1350x750")
        self.root.configure(background="#0eeb9d")
        

        DateofOrder=StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1=StringVar()
        var2=StringVar()
        var3=StringVar()
        var4=IntVar()

        
        FirstName=StringVar()
        LastName=StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Telephone=StringVar()
        Ref=StringVar()
        

        Membership=StringVar()
        Membership.set("0")

#....................................function declared..............................................................................

        def iExit():
            iExit=tkinter.messagebox.askyesno("PATIENT REGISTRATION SYSTEM","Confirm you want to exit")
            if iExit>0:
                root.destroy()
                return

        def Reset():
            FirstName.set("")
            LastName.set("")
            Address.set("")
            PostCode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("0")
            

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.CboProve_Id.current(0)
            self.CboTypeofMember.current(0)
            self.CboMethodPayment.current(0)

        def iResetRecord():
                
            iResetRecord=tkinter.messagebox.askokcancel("PATIENT REGISTRATION SYSTEM","Confirm you want to exit to new record")
            if iResetRecord>0:
                
                Reset()
            elif iResetRecord<=0:
                
                Reset()
                self.txtReceipt.delete("0",END)
                
                return

        def Ref_No():

            x=random.randint(10903,600873)
            randomRef=str(x)
            Ref.set(randomRef)

        def Receipt():

            Ref_No()
            self.txtReceipt.insert(END,"\t"+Ref.get()+"\t\t"+FirstName.get()+"\t\t"+LastName.get()+"\t\t"+PostCode.get()+"\t\t"+
                                   DateofOrder.get()+"\t\t"+Telephone.get()+"\t\t"+Membership.get()+"\n")

        

#.................................................frame................................................................................

        Mainframe=Frame(self.root)
        Mainframe.config(background="#03fc90")
        Mainframe.grid()

        Titleframe=Frame(Mainframe,bd=20,width=1350,padx=20,relief="ridge")
        Titleframe.pack(side=TOP,padx=20)

        self.lbltitle=Label(Titleframe,text="PATIENT REGISTRATION SYSTEM",bd=15,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",50,"bold"),padx=10,pady=4)
        self.lbltitle.grid()

#................................................Lowerframe...................................................................

        MemberDetailFrame=LabelFrame(Mainframe,width=1350,height=500,bd=20,pady=5,relief="ridge")
        MemberDetailFrame.pack(side=BOTTOM)

        DetailFrame=LabelFrame(MemberDetailFrame,bd=10,width=800,height=400,bg="#f50e0a",relief="ridge")
        DetailFrame.pack(side=LEFT)

        MemberNameFrame=LabelFrame(DetailFrame,bd=10,width=350,height=400,font=("times new roman",12,"bold"),text="CUSTOMER DETAIL",
                              bg="#f50e0a",relief="ridge")
        
        MemberNameFrame.grid(row=0,column=0)

        ReceiptButtonFrame=LabelFrame(MemberDetailFrame,bd=10,width=1000,height=400,relief="ridge",bg="#f50e0a")

        ReceiptButtonFrame.pack(side=RIGHT)


#...............................................................................................................................

        self.lblReferenceNo=Label(MemberNameFrame,text="ReferenceNo",bd=7,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.lblReferenceNo.grid(row=0,column=0)

        self.txtReferenceNo=Entry(MemberNameFrame,bd=7,relief=RIDGE,textvariable=Ref,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.txtReferenceNo.grid(row=0,column=1)

        self.lblFirstName=Label(MemberNameFrame,text="FirstName",bd=7,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.lblFirstName.grid(row=1,column=0)

        self.txtFirstName=Entry(MemberNameFrame,bd=7,relief=RIDGE,textvariable=FirstName,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.txtFirstName.grid(row=1,column=1)

        self.lblLastName=Label(MemberNameFrame,text="LastName",bd=7,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.lblLastName.grid(row=2,column=0)

        self.txtLastName=Entry(MemberNameFrame,bd=7,relief=RIDGE,textvariable=LastName,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.txtLastName.grid(row=2,column=1)

        self.lblAddress=Label(MemberNameFrame,text="Address",bd=7,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.lblAddress.grid(row=3,column=0)

        self.txtAddress=Entry(MemberNameFrame,bd=7,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.txtAddress.grid(row=3,column=1)

        self.lblPostCode=Label(MemberNameFrame,text="PostCode",bd=7,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.lblPostCode.grid(row=4,column=0)

        self.txtPostCode=Entry(MemberNameFrame,bd=7,relief=RIDGE,textvariable=PostCode,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.txtPostCode.grid(row=4,column=1)

        self.lblTelephone=Label(MemberNameFrame,text="Telephone",bd=7,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.lblTelephone.grid(row=5,column=0)

        self.txtTelephone=Entry(MemberNameFrame,bd=7,relief=RIDGE,textvariable=Telephone,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
        self.txtTelephone.grid(row=5,column=1)


        self.lblDate=Label(MemberNameFrame,text="Date",bd=7,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",14,"bold"))
                      
        self.lblDate.grid(row=6,column=0)

        self.txtDate=Entry(MemberNameFrame,bd=7,relief=RIDGE,textvariable=DateofOrder,
                      bg="black",fg="white",font=("times new roman",14,"bold"))
        self.txtDate.grid(row=6,column=1)
        
#........................................................MemberInformation............................................................

        self.lblProve_Id=Label(MemberNameFrame,text="Prove_Id",
                      font=("times new roman",14,"bold"))
                      
        self.lblProve_Id.grid(row=7,column=0,sticky=W)

        self.CboProve_Id=ttk.Combobox(MemberNameFrame,textvariable=var1,state="readonly",
                      font=("times new roman",14,"bold"),width=19)
        self.CboProve_Id["value"]=("","PilotLicence","Driving Licence","Passport","Student Id")
        self.CboProve_Id.current(0)
        self.CboProve_Id.grid(row=7,column=1)

        self.lblTypeofMember=Label(MemberNameFrame,text="Type of Member",
                      font=("times new roman",14,"bold"))
                      
        self.lblTypeofMember.grid(row=8,column=0,sticky=W)

        self.CboTypeofMember=ttk.Combobox(MemberNameFrame,textvariable=var2,state="readonly",
                      font=("times new roman",14,"bold"),width=19)
        self.CboTypeofMember["value"]=("","Full Member","Annual Membership","Pay As you Go","Honary Member")
        self.CboTypeofMember.current(0)
        self.CboTypeofMember.grid(row=8,column=1)

        self.lblMethodPayment=Label(MemberNameFrame,text="MethodPayment",
                      font=("times new roman",14,"bold"))
                      
        self.lblMethodPayment.grid(row=9,column=0,sticky=W)

        self.CboMethodPayment=ttk.Combobox(MemberNameFrame,textvariable=var3,state="readonly",
                      font=("times new roman",14,"bold"),width=19)
        self.CboMethodPayment["value"]=("","Visa Card","Master Card","Debit Card","Cash")
        self.CboMethodPayment.current(0)
        self.CboMethodPayment.grid(row=9,column=1)
#.........................................................checkButton.................................................................
        self.chkMembership=Checkbutton(MemberNameFrame,text="Membership Fees",variable=var4,onvalue=1,offvalue=0,
                      font=("times new roman",14,"bold"))
                      
        self.chkMembership.grid(row=10,column=0,sticky=W)

        self.chkMembership=Entry(MemberNameFrame,textvariable=Membership,bd=7,state=NORMAL,justify=RIGHT,
                      font=("times new roman",14,"bold"))
                      
        self.chkMembership.grid(row=10,column=1)

#...........................................................buttonframe...............................................................

        self.lblReceipt=Label(ReceiptButtonFrame,font=("times new roman",14,"bold"),pady=10,fg="#0eeb9d",bg="black",
                              text="Member Ref\tFirstName\tLastName\tpostcode\t\tDateReg.\t\tTelephone\tMemberPaid",bd=10)
                      
        self.lblReceipt.grid(row=0,column=0,columnspan=4)

        self.txtReceipt=Text(ReceiptButtonFrame,width=112,height=22,font=("times new roman",14,"bold"))
                      
                      
        self.txtReceipt.grid(row=1,column=0,columnspan=4)

#.............................................................button..................................................................

        self.btnReceipt=Button(ReceiptButtonFrame,width=13,font=("times new roman",16,"bold"),bd=7,
                               text="Receipt",command=Receipt,padx=18,bg="#283fed",fg="#313038").grid(row=2,column=0)
                      
                      
        

        self.btnReset=Button(ReceiptButtonFrame,width=13,font=("times new roman",16,"bold"),bd=7,
                             text="Reset",command=iResetRecord,padx=18,bg="#283fed",fg="#313038").grid(row=2,column=1)
                      
                      
        

        self.btnExit=Button(ReceiptButtonFrame,width=13,font=("times new roman",16,"bold"),bd=7,
                            text="Exit",command=iExit,padx=18,bg="#283fed",fg="#313038").grid(row=2,column=2)
                      
                      
    

        

        
        

        
if __name__=="__main__":
    root=Tk()
    app=Registration(root)
    root.mainloop()













    
        
        
