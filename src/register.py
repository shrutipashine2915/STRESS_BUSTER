from tkinter import *
from tkinter import Tk
from _overlapped import NULL
from _functools import partial
from gettext import find
from tkcalendar import Calendar

from tkinter  import messagebox
from dataManagement import DataManagement
from calendar import month
from Window import Window
from Symptomlist import Symptoms
from login import Login



class Registration:
    "This is Registration Class"
    #All Variables:-
    def __init__(self):
        self.win=Window()
        self.root1 = self.win.root
        
        self.root =Frame(self.root1,width=2000,height=2000)
        self.root.place(x=0,y=0)
        #root.configure(width=1000,height=1000)
        
        self.i=0
        self.b1=Button()
        self.label1 = Label(self.root, text="Registration form",width=20,font=("bold", 30))
        self.Name= Label(self.root, text="Full Name:",width=20,font=("bold", 15),bg="lightblue")
        self.tName = Entry(self.root,width=50)
        
        self.Email= Label(self.root, text="Email:",width=20,font=("bold", 15),bg="lightblue")
        self.tEmail = Entry(self.root,width=50)
        self.Gender = Label(self.root, text="Gender:",width=20,font=("bold", 15),bg="lightblue")
        self.var = IntVar()
        self.DOB= Label(self.root, text="Date Of Birth",width=20,font=("bold", 15),bg="lightblue")
        
        
        self.Contact= Label(self.root, text="Phone No.",width=20,font=("bold", 15),bg="lightblue")
        self.tContact= Entry(self.root,width=50)
       
        self.c=StringVar()
    
        self.Address= Label(self.root, text="Address",width=20,font=("bold", 15),bg="lightblue")
        self.tAddress= Entry(self.root,width=50)
        self.pnum= Label(self.root, text="Friend/Parent No.",width=20,font=("bold", 15),bg="lightblue")
        self.tpnum= Entry(self.root,width=50)
        self.password= Label(self.root, text="Password",width=20,font=("bold", 15),bg="lightblue")
        self.tpasword= Entry(self.root,width=50,show='*')
        self.Taluka= Label(self.root, text="Taluka",width=20,font=("bold", 15),bg="lightblue")
        self.tTaluka= Entry(self.root,width=50,bg="lightblue")
        self.r1=Radiobutton(self.root, text="Male",padx = 5, variable=self.var, value=1,font=("bold", 15),bg="lightblue")
        self.r2=Radiobutton(self.root, text="Female",padx = 20, variable=self.var, value=2,font=("bold", 15),bg="lightblue")
        self.r3=Radiobutton(self.root, text="Other",padx = 45, variable=self.var, value=3,font=("bold", 15),bg="lightblue")
        self.cal =Calendar(self.root,year=2021,month=1,date=1)
        self.b1=Button(self.root, text='Submit',command=self.validation,width=30,bg='brown',fg='black')
        self.root.configure(bg="lightblue")
    
    def validation(self):
        
        data=DataManagement()
        if len(self.tName.get())<=5 :
            print("Please Enter Correct Name")
            messagebox.showwarning("Wrong Name","Enter Correct Name")
            
            return
        else :
            data.set_name__(self.tName.get())
        
        if self.tEmail.get().find("@") != -1 :
            value=self.tEmail.get()
            data.set_email__(value)
        else:
            print("Please Enter Correct Email Address")
            messagebox.showwarning("Wrong Email Address","Enter Correct Email Address")
            return
        
        if self.var.get() == 1:
            data.set_gender__("Male")
        elif self.var.get() == 2:
            data.set_gender__("Female")
        elif self.var.get() == 3:
            data.set_gender__("Other")
        else:
            print("Please Select Gender")
            messagebox.showwarning("Gender Not Selected","Please Select Gender")
            return
        
        data.set_dob__(self.cal.get_date())
        if self.tContact.get().isdigit():
            data.set_contact__(self.tContact.get())
        else :
            print("Wrong Number")
            messagebox.showwarning("Wrong Mobile Number","Enter Correct Mobile Number")
            return
        if self.tpnum.get().isdigit():
            data.set_pnum__(self.tpnum.get())
        else :
            print("Wrong Number")
            messagebox.showwarning("Wrong Mobile Number","Enter Correct Mobile Number")
            return
        
        if len(self.tpasword.get())<=7:
            messagebox.showwarning("Small Password","Enter 8 Digit PassWord")
            
            return
        else :
            data.set_pass__(self.tpasword.get())
            
            

            
        data.set_address__(self.tAddress.get())
        data.storeNew()
        
        
        messagebox.showinfo("Complete","Registration is Successfully Done")
        self.root.destroy()
        
        a=Login()
        
       
        
        
        

    




    def placing(self):
        X=630
        Y=250
        XD=170
        YD=50

        #Registration.label1.place(x=90,y=53)
        self.Name.place(x=X,y=Y)
        self.tName.place(x=X+XD,y=Y)
        Y+=YD
        self.Email.place(x=X,y=Y)
        self.tEmail.place(x=X+XD,y=Y)
        Y+=YD
        self.Gender.place(x=X,y=Y)
        
        self.r1.place(x=X+XD,y=Y)
        self.r2.place(x=X+XD+80,y=Y)
        self.r3.place(x=X+XD+70+XD,y=Y)
        Y+=YD
        self.DOB.place(x=X-10,y=Y)
        self.cal.place(x=X+XD,y=Y)
        Y=Y+(YD*4)
        
        self.Contact.place(x=X,y=Y)
        self.tContact.place(x=X+XD,y=Y)
        Y=Y+YD
        
        self.pnum.place(x=600,y=Y)
        self.tpnum.place(x=X+XD,y=Y)
        Y=Y+YD

        self.password.place(x=X,y=Y)
        self.tpasword.place(x=X+XD,y=Y)
        Y=Y+YD
        """
        Registration.Taluka.place(x=X,y=Y)
        Registration.tTaluka.place(x=X+XD,y=Y)
        Y=Y+YD

        """
        self.Address.place(x=X,y=Y)
        self.tAddress.place(x=X+XD,y=Y)
        Y=Y+YD
        print(Y)
        self.c.set('Select your City')
        
        
        self.b1.place(x=X+XD,y=Y)
        
        
       
        self.root.mainloop()
        
        



        
    
       
        

        
    
