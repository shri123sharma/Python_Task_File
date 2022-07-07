from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime


class window3:
    def __init__(self,root):
        self.root=root
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        self.root.geometry("1350x750")
        self.root.iconbitmap("C:/Users/pc/Desktop/pharmacy project image/pharmacy.ico")
        self.root.configure(background="#eba234")
        

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
                root.destroy()
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
            #self.txtDetailframe.delete("1.0",END)

            return
            


        
#.........................................................frame........................................................................        
        self.root.mainframe=Frame(self.root)
        self.root.mainframe.config(background="#03fc90")
        self.root.mainframe.grid()

        Titleframe=Frame(self.root.mainframe,bd=20,width=1350,padx=20,relief="ridge")
        Titleframe.pack(side=TOP)

        self.lbltitle=Label(Titleframe,text="HOSPITAL MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                      bg="black",fg="white",font=("times new roman",50,"bold"),padx=2,pady=4)
        self.lbltitle.grid()

        Detailframe=Frame(self.root.mainframe,bd=10,width=1350,height=400,padx=20,relief="ridge")
        Detailframe.pack(side=BOTTOM)

        Buttonframe=Frame(self.root.mainframe,bd=10,width=1350,height=50,padx=20,relief="ridge")
        Buttonframe.pack(side=BOTTOM)

        Dataframe=Frame(self.root.mainframe,bd=10,width=1350,height=400,padx=20,relief="ridge")
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
    
    root=Tk()
    app=window3(root)
    root.mainloop()
    






