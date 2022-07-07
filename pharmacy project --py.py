from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime

 
def main():
    root=Tk()
    app=window1(root)

class window1:
    def __init__(self,master):
        self.master=master
        self.master.title("PHARMACY MANAGEMENT SYSTEM")
        self.master.geometry("1350x750")
        self.master.iconbitmap("C:/Users/pc/Desktop/pharmacy project image/pharmacy.ico")
        self.master.configure(background="#eba234")
        self.frame=Frame(self.master,bg="#34ebd6")
        self.frame.pack()

        self.username=StringVar()
        self.password=StringVar()
#............................................................label.....................................................................
        self.lbltitle=Label(self.frame,text="PHARMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                      bg="black",fg="white",font=("times new roman",50,"bold"),padx=2,pady=4)
        self.lbltitle.grid(row=0,column=0,columnspan=2,pady=5)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<frame>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.loginframe1=Frame(self.frame,height=300,width=1010,bd=20,relief="ridge")

        self.loginframe1.grid(padx=200,pady=30)

        self.loginframe2=Frame(self.frame,height=100,width=1000,bd=20,relief="ridge")

        self.loginframe2.grid(padx=100,pady=30)
        
        self.loginframe3=Frame(self.frame,height=200,width=1000,bd=20,relief="ridge")

        self.loginframe3.grid(padx=100,pady=30)
#.....................................................................................................................................
        self.lblusername=Label(self.loginframe1,text="USERNAME",bd=15,relief="ridge",
                      bg="black",fg="white",font=("times new roman",20,"bold"))
        self.lblusername.grid(row=0,column=0,padx=5,pady=5)

        self.lblentry=Entry(self.loginframe1,text="USERNAME",bd=15,relief=RIDGE,textvariable=self.username,
                      bg="black",fg="white",font=("times new roman",20,"bold"))
        self.lblentry.grid(row=0,column=1,padx=5,pady=5)

        self.lblpassword=Label(self.loginframe1,text="PASSWORD",bd=15,relief="ridge",
                      bg="black",fg="white",font=("times new roman",20,"bold"))
        self.lblpassword.grid(row=1,column=0,padx=5,pady=5)

        self.lblentry=Entry(self.loginframe1,text="PASSWORD",bd=15,relief="ridge",textvariable=self.password,
                      bg="black",fg="white",font=("times new roman",20,"bold"))
        self.lblentry.grid(row=1,column=1,padx=5,pady=5)



#......................................................................................................................................
        self.btnlogin=Button(self.loginframe2,text="LOGIN",width=20,command=self.login_system,cursor="hand2",
                                    bg="black",fg="white",font=("times new roman",20,"bold"),bd=4)
        self.btnlogin.grid(row=0,column=0,padx=2)

        self.btnreset=Button(self.loginframe2,text="RESET",width=20,command=self.reset,cursor="hand2",
                                    bg="black",fg="white",font=("times new roman",20,"bold"),bd=4)
        self.btnreset.grid(row=0,column=1,padx=2)

        self.btnexit=Button(self.loginframe2,text="EXIT",width=20,command=self.iExit,cursor="hand2",
                                    bg="black",fg="white",font=("times new roman",20,"bold"),bd=4)
        self.btnexit.grid(row=0,column=2,padx=2)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.btnregistration=Button(self.loginframe3,text="PATIENT REGISTRATION",command=self.registration_window,cursor="hand2",
                                    state=DISABLED,bg="black",fg="white",font=("times new roman",20,"bold"),bd=4)
        self.btnregistration.grid(row=0,column=0,pady=8,padx=20)
        
        self.btnhospital=Button(self.loginframe3,text="HOSPITAL MANAGEMENT",command=self.hospital_window,cursor="hand2",
                                state=DISABLED,bg="black",fg="white",font=("times new roman",20,"bold"),bd=4)
        self.btnhospital.grid(row=0,column=1,pady=8,padx=20)
#......................................................................................................................................

    def login_system(self):
        user=self.username.get()
        pas=self.password.get()


        if (user==str("shri")) and (pas==str(1234)):
            self.btnregistration.config(state=NORMAL)
            self.btnhospital.config(state=NORMAL)

        else:
            tkinter.messagebox.askyesno("PHARMACY MANAGEMENT SYSTEM","you have entered invalid login detail")
            self.btnregistration.config(state=DISABLED)
            self.btnhospital.config(state=DISABLED)
            self.username.set("")
            self.password.set("")
                
            self.lblentry.focus()

    def reset(self):
            self.btnregistration.config(state=DISABLED)
            self.btnhospital.config(state=DISABLED)
            self.username.set("")
            self.password.set("")
                
            self.lblentry.focus()

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("PHARMACY MANAGEMENT SYSTEM","confirm you want to exit")

        if self.iExit>0:
            self.master.destroy()
            return 
                
                
#......................................................................................................................................
    def registration_window(self):
        self.newwindow=Toplevel(self.master)
        self.app=window2(self.newwindow)
        
    def hospital_window(self):
        self.newwindow=Toplevel(self.master)
        self.app=window3(self.newwindow)

    
        
    
        
class window2:
    def __init__(self,master):
        self.master=master
        self.master.title("PHARMACY MANAGEMENT SYSTEM")
        self.master.geometry("1350x750")
        self.master.iconbitmap("C:/Users/pc/Desktop/pharmacy project image/pharmacy.ico")
        self.master.configure(background="#eba234")
        self.frame=Frame(self.master,bg="#eba234")
        self.frame.pack()
        
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
                master.destroy()
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

        Mainframe=Frame(self.frame)
        Mainframe.config(background="#03fc90")
        Mainframe.grid()

        Titleframe=Frame(Mainframe,bd=20,width=1350,padx=10,relief="ridge")
        Titleframe.pack(side=TOP,padx=10)

        self.lbltitle=Label(Titleframe,text="PATIENT REGISTRATION SYSTEM",bd=15,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",50,"bold"),padx=10,pady=4)
        self.lbltitle.grid()

#................................................Lowerframe...................................................................

        MemberDetailFrame=LabelFrame(Mainframe,width=1050,height=500,bd=20,pady=5,relief="ridge")
        MemberDetailFrame.pack(side=BOTTOM)

        DetailFrame=LabelFrame(MemberDetailFrame,bd=10,width=800,height=400,bg="#f50e0a",relief="ridge")
        DetailFrame.pack(side=LEFT)

        MemberNameFrame=LabelFrame(DetailFrame,bd=10,width=350,height=400,font=("times new roman",12,"bold"),text="CUSTOMER DETAIL",
                              bg="#f50e0a",relief="ridge")
        
        MemberNameFrame.grid(row=0,column=0)

        ReceiptButtonFrame=LabelFrame(MemberDetailFrame,bd=10,width=800,height=200,relief="ridge",bg="#f50e0a")

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
                      
                      
    
    
class window3:
    def __init__(self,master):
        self.master=master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1350x750")
        self.master.iconbitmap("C:/Users/pc/Desktop/pharmacy project image/pharmacy.ico")
        self.master.configure(background="#eba234")
        self.frame=Frame(self.master)
        self.frame.pack()
    

        Cmbnametablet=StringVar()
        ReferenceNo=StringVar()
        Dose=StringVar()
        Numbertablet=StringVar()
        Lot=StringVar()
        IssuedDate=StringVar()
        ExpDate=StringVar()
        Dailydose=StringVar()
        PossiableSideEffects=StringVar()
        FurtherInformation=StringVar()
        HowToUse=StringVar()
        PatientID=StringVar()
        PatientName=StringVar()
        DateOfBirth=StringVar()
        PatientsAddress=StringVar()
        Prescripation=StringVar()

#...............................................function declare......................................................................
        def iExit():
            iExit=tkinter.messagebox.askyesno("HOSPITAL MANAGEMENT SYSTEM","confirm you want to exit")
            if iExit>0:
                self.master.destroy()
                return

        def iPrescripation():

            self.txtPrescripation.insert(END,"Name Of Tablets:\t\t\t"+Cmbnametablet.get()+"\n")
            self.txtPrescripation.insert(END,"ReferenceNo:\t\t\t"+ReferenceNo.get()+"\n")
            self.txtPrescripation.insert(END,"Dose:\t\t\t"+Dose.get()+"\n")
            self.txtPrescripation.insert(END,"Numbertablet:\t\t\t"+Numbertablet.get()+"\n")
            self.txtPrescripation.insert(END,"Lot:\t\t\t"+Lot.get()+"\n")
            self.txtPrescripation.insert(END,"IssuedDate:\t\t\t"+IssuedDate.get()+"\n")
            self.txtPrescripation.insert(END,"ExpDate:\t\t\t"+ExpDate.get()+"\n")
            self.txtPrescripation.insert(END,"Dailydose:\t\t\t"+Dailydose.get()+"\n")
            self.txtPrescripation.insert(END,"PatientName:\t\t\t"+PatientName.get()+"\n")
            self.txtPrescripation.insert(END,+"DateOfBirth:\t\t\t"+DateOfBirth.get()+"\n")
            self.txtPrescripation.insert(END,+"PatientsAddress:\t\t\t"+PatientsAddress.get()+"\n")
            

            return


        def iPrescripationData():
            
            

                self.txtDetailframe.insert(END, Cmbnametablet.get()+"\t\t"+ReferenceNo.get()+"\t\t"+ Dose.get()+"\t\t"+
                                    Numbertablet.get()+ "\t"+   Lot.get()+"\t"+
                                     IssuedDate.get()+ "\t"+ ExpDate.get()+ "\t"+Dailydose.get()+
                                      "\t\t"+PatientName.get()+  "\t\t"+DateOfBirth.get()+
                                     "\t\t"+PatientsAddress.get()+"\n")

                return
        
        def iDelete():
            Cmbnametablet.set("")
            self.nametablet.current(0)
            ReferenceNo.set("")
            Dose.set("")
            Numbertablet.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            Dailydose.set("")
            PossiableSideEffects.set("")
            FurtherInformation.set("")
            HowToUse.set("")
            PatientID.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientsAddress.set("")
            self.txtPrescripation.delete("1.0",END)
            self.txtDetailframe.delete("1.0",END)
            return

        def iReset():
            Cmbnametablet.set("")
            self.nametablet.current(0)
            ReferenceNo.set("")
            Dose.set("")
            Numbertablet.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpDate.set("")
            Dailydose.set("")
            PossiableSideEffects.set("")
            FurtherInformation.set("")
            HowToUse.set("")
            PatientID.set("")
            PatientName.set("")
            DateOfBirth.set("")
            PatientsAddress.set("")
            self.txtPrescripation.delete("1.0",END)
             

            return
            


        
#.........................................................frame........................................................................        
        mainframe=Frame(self.frame) 
        #mainframe.config(background="#03fc90")
        mainframe.grid()

        Titleframe=Frame(mainframe,bd=20,width=1350,padx=20,relief="ridge")
        Titleframe.pack(side=TOP)

        self.lbltitle=Label(Titleframe,text="HOSPITAL MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                      bg="black",fg="#0eeb9d",font=("times new roman",50,"bold"),padx=2,pady=4)
        self.lbltitle.grid()

        Detailframe=Frame(mainframe,bd=10,width=1350,height=400,padx=20,relief="ridge")
        Detailframe.pack(side=BOTTOM)

        Buttonframe=Frame(mainframe,bd=10,width=1350,height=50,padx=20,relief="ridge")
        Buttonframe.pack(side=BOTTOM)

        Dataframe=Frame(mainframe,bd=10,width=1350,height=400,padx=20,relief="ridge")
        Dataframe.pack(side=BOTTOM)

        Dataframeleft=LabelFrame(Dataframe,bd=10,width=800,height=300,padx=10,relief="ridge",text="PatientInformation:",bg="#f50e0a",font=("times new roman",12,"bold"))
        Dataframeleft.pack(side=LEFT)

        Dataframeright=LabelFrame(Dataframe,bd=10,width=450,height=300,padx=10,relief="ridge",text="Prescripation:",bg="#f50e0a",font=("times new roman",12,"bold"))
        Dataframeright.pack(side=RIGHT)
#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Dataframeleft,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,        
        self.lblnametablet=Label(Dataframeleft,text="Name Of Tablets:",bg="#3f6e6b",font=("times new roman",12,"bold"))
                      
        self.lblnametablet.grid(row=0,column=0,sticky=W)
        
        self.nametablet=ttk.Combobox(Dataframeleft,textvariable=Cmbnametablet,state="readonly",font=("times new roman",12,"bold"))
        self.nametablet["value"]=("","Vicodin","Albuterol","Gabapentin","Metformin","Metformin")
        self.nametablet.current(0)
        self.nametablet.grid(row=0,column=1)

        self.lblFurtherInformation=Label(Dataframeleft,text="FurtherInformation:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblFurtherInformation.grid(row=0,column=2,sticky=W)

        self.entryFurtherInformation=Entry(Dataframeleft,textvariable=FurtherInformation,font=("times new roman",12,"bold"))
                      
        self.entryFurtherInformation.grid(row=0,column=3)

        self.lblRefNo=Label(Dataframeleft,text="ReferenceNo:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblRefNo.grid(row=1,column=0,sticky=W)
        self.entryRefNo=Entry(Dataframeleft,textvariable=ReferenceNo,font=("times new roman",12,"bold"))
                      
        self.entryRefNo.grid(row=1,column=1,sticky=W)

        self.lblDose=Label(Dataframeleft,text="Dose:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblDose.grid(row=1,column=2,sticky=W)
        self.entryDose=Entry(Dataframeleft,textvariable=Dose,font=("times new roman",12,"bold"))
                      
        self.entryDose.grid(row=1,column=3,sticky=W)

        self.lblNumbertablet=Label(Dataframeleft,text="Numbertablet:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblNumbertablet.grid(row=2,column=0,sticky=W)
        self.entryNumbertablet=Entry(Dataframeleft,textvariable=Numbertablet,font=("times new roman",12,"bold"))
                      
        self.entryNumbertablet.grid(row=2,column=1,sticky=W)

        self.lblLot=Label(Dataframeleft,text="Lot:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblLot.grid(row=2,column=2,sticky=W)
        self.entryLot=Entry(Dataframeleft,textvariable=Lot,font=("times new roman",12,"bold"))
                      
        self.entryLot.grid(row=2,column=3,sticky=W)

        self.lblIssuedDate=Label(Dataframeleft,text="IssuedDate:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblIssuedDate.grid(row=3,column=0,sticky=W)
        self.entryIssuedDate=Entry(Dataframeleft,textvariable=IssuedDate,font=("times new roman",12,"bold"))
                      
        self.entryIssuedDate.grid(row=3,column=1,sticky=W)

        self.lblExpDate=Label(Dataframeleft,text="ExpDate:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblExpDate.grid(row=3,column=2,sticky=W)
        self.entryExpDate=Entry(Dataframeleft,textvariable=ExpDate,font=("times new roman",12,"bold"))
                      
        self.entryExpDate.grid(row=3,column=3,sticky=W)

        self.lblDailydose=Label(Dataframeleft,text="Dailydose:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblDailydose.grid(row=4,column=0,sticky=W)
        self.entryDailydose=Entry(Dataframeleft,textvariable=Dailydose,font=("times new roman",12,"bold"))
                      
        self.entryDailydose.grid(row=4,column=1,sticky=W)

        self.lblPossiableSideEffects=Label(Dataframeleft,text="PossiableSideEffects:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblPossiableSideEffects.grid(row=4,column=2,sticky=W)
        self.entryPossiableSideEffects=Entry(Dataframeleft,textvariable=PossiableSideEffects,font=("times new roman",12,"bold"))
                      
        self.entryPossiableSideEffects.grid(row=4,column=3,sticky=W)

        self.lblHowToUse=Label(Dataframeleft,text="HowToUse:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblHowToUse.grid(row=5,column=0,sticky=W)
        self.entryHowToUse=Entry(Dataframeleft,textvariable=HowToUse,font=("times new roman",12,"bold"))
                      
        self.entryHowToUse.grid(row=5,column=1,sticky=W)

        self.lblPatientID=Label(Dataframeleft,text="PatientID:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblPatientID.grid(row=5,column=2,sticky=W)
        self.entryPatientID=Entry(Dataframeleft,textvariable=PatientID,font=("times new roman",12,"bold"))
                      
        self.entryPatientID.grid(row=5,column=3,sticky=W)

        self.lblPatientName=Label(Dataframeleft,text="PatientName:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblPatientName.grid(row=6,column=0,sticky=W)
        self.entryPatientName=Entry(Dataframeleft,textvariable=PatientName,font=("times new roman",12,"bold"))
                      
        self.entryPatientName.grid(row=6,column=1,sticky=W)

        self.lblDateOfBirth=Label(Dataframeleft,text="DateOfBirth:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblDateOfBirth.grid(row=6,column=2,sticky=W)
        self.entryDateOfBirth=Entry(Dataframeleft,textvariable=DateOfBirth,font=("times new roman",12,"bold"))
                      
        self.entryDateOfBirth.grid(row=6,column=3,sticky=W)

        self.lblPatientsAddress=Label(Dataframeleft,text="PatientsAddress:",bg="#3f6e6b",font=("times new roman",12,"bold"),padx=2)
                      
        self.lblPatientsAddress.grid(row=7,column=0,sticky=W)
        self.entryPatientsAddress=Entry(Dataframeleft,textvariable=PatientsAddress,font=("times new roman",12,"bold"))
                      
        self.entryPatientsAddress.grid(row=7,column=1,sticky=W)

        
#................................................................Dataframeright.....................................................................       
        self.txtPrescripation=Text(Dataframeright,font=("times new roman",12,"bold"),width=50,height=12,padx=2,pady=4)
                      
        self.txtPrescripation.grid(row=0,column=0)
#................................................................Buttonframe.....................................................................       
        self.btnPrescripation=Button(Buttonframe,text="Prescripation",font=("times new roman",12,"bold"),command=iPrescripation,width=20,bd=4,bg="#283fed",fg="#222224")
                      
        self.btnPrescripation.grid(row=0,column=0)

        self.btniPrescripationData=Button(Buttonframe,text="PrescripationData",font=("times new roman",12,"bold"),command=iPrescripationData,width=20,bd=4,bg="#283fed",fg="#222224")
                      
        self.btniPrescripationData.grid(row=0,column=1)

        self.btnDelete=Button(Buttonframe,text="Delete",font=("times new roman",12,"bold"),command=iDelete,width=20,bd=4,bg="#283fed",fg="#222224")
                      
        self.btnDelete.grid(row=0,column=2)

        self.btnReset=Button(Buttonframe,text="Reset",font=("times new roman",12,"bold"),command=iReset,width=20,bd=4,bg="#283fed",fg="#222224")
                      
        self.btnReset.grid(row=0,column=3)

        self.btnExit=Button(Buttonframe,text="Exit",font=("times new roman",12,"bold"),command=iExit,width=20,bd=4,bg="#283fed",fg="#222224")
                      
        self.btnExit.grid(row=0,column=4)




#................................................................Detailframe.....................................................................       

        self.lblLabel=Label(Detailframe,font=("times new roman",10,"bold"),pady=8,
        text="Name of Tablets\t Reference No.\t Doseage\t No.of Tablets\t Lots\t IssueDate\t ExpDate\t Dailydose\t PatientName\t DateOfBirth\t PatientsAddress")
              
        self.lblLabel.grid(row=0,column=0)

        self.txtDetailframe=Text(Detailframe,font=("times new roman",12,"bold"),width=140,height=10,padx=2,pady=4)
                      
        self.txtDetailframe.grid(row=1,column=0)

if __name__=="__main__":
    main()


        

