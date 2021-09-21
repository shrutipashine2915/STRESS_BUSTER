from Window import Window

from tkinter import *
from tkinter import Tk
from dataManagement import DataManagement
from Symptomlist import Symptoms
from REMEDIESMODULE1 import Acute_Stress
from REMEDIESMODULE2 import Episodic_Stress
from REMEDIESMODULE3 import Chronic_Stress


class Login:
    
    def __init__(self):
        self.win=Window()
        self.root1=self.win.root
        self.root=Frame(self.root1,width=1000,height=1000)
        self.root.place(x=0,y=0)
        self.root.configure(bg="lightblue")
        
        X=600
        Y=300
        XD=170
        YD=50
        self.lno=Label(self.root,text="Mobile Number",width=20,font=("bold", 15),bg="lightblue")
        self.tno=Entry(self.root,width=20)
        
        self.lno.place(x=X-15,y=Y)
        self.tno.place(x=X+XD,y=Y+5)
        Y=Y+YD
        
        self.lpass=Label(self.root,text="Password",width=20,font=("bold", 15),bg="lightblue")
        self.tpass=Entry(self.root,width=20,show='*')
        
        self.lpass.place(x=X-15,y=Y)
        self.tpass.place(x=X+XD,y=Y+5)
        
        Y=Y+YD
        self.sumit=Button(self.root, text='Submit',command=self.validation,width=15,height=1,bg='brown',fg='black')
        
        self.sumit.place(x=X+XD-40,y=Y)
        
        self.root.mainloop()
        
    def validation(self):
        a=DataManagement()
        result=a.verification(self.tno.get(), self.tpass.get())
        if result==0:
            messagebox.showwarning("Wrong Credentials","Enter Correct Mobile Number Or PassWord")
            return
        else:
            str="Welcome "+result
            messagebox.showinfo("SuccesFull",str)
            type=DataManagement.getStressType(DataManagement,name=result)
            print(type)
            if type=='0':
                self.root.destroy()
                a=Symptoms(result)
                a.draw()
            elif type=='1':
                self.root.destroy()
                asc=Acute_Stress()
                asc.start()
                
            elif type=='2':
                self.root.destroy()
                csc=Chronic_Stress()
                csc.start()
                
            elif type=='3':
                self.root.destroy()
                esc=Episodic_Stress()
                esc.start()
        return
    
