from tkinter import *
from distutils import command
from _overlapped import NULL
import tkinter

from Window import Window
from _ast import If
from REMEDIESMODULE1 import Acute_Stress
from REMEDIESMODULE2 import Episodic_Stress
from REMEDIESMODULE3 import Chronic_Stress
from dataManagement import DataManagement
class Symptoms:
    wind=Window()
    win1= wind.root
    
    w, h = win1.winfo_screenwidth(),win1.winfo_screenheight()
    win=Frame(win1,width=1000,height=1000)
    win.place(x=0,y=0)
    win.configure(bg="lightblue")
    
    acute_stress= ["ANXIETY","LOW MOOD","IRRITATION","POOR SLEEP","WANTING TO BE ALONE","HEADACHE","CHEST PAIN"]
    episodic_stress=["TENSION","CHEST PAIN","RAPID HEARTBEAT","ELEVATED BLOOD PRESSURE","MIGRANINES"]
    chronic_stress=["FATIGUE","HEADACHE","FEELING HELPLESS","LOSS OF SEXUAL DESIRE","LOW SELF ESTEEM","DIFFULTY SLEEPING"]
    symptom_list = ["HEADACHE","FEVER","LOW ENERGY","LOW MOOD","ACHES","CHEST PAIN","RAPID HEARTBEAT","IRRITATION","POOR SLEEP","WANTING TO BE ALONE","INFECTIONS","LOSS OF SEXUAL DESIRE","NERVOUSNESS AND SHAKING","DIFFICULTY IN SLEEPING","COLD","SWEATY ","SUCIDAL THOUGHTS","MIGRANINES","ELEVATED BLOOD PRESSURE","TENSION","FRUSTRATION","FEAR","SADNESS","ANGER","GUILT","SHAME","JEALOUSY","WORRY","ANXIETY","FATIGUE","VOMITTING","PANIC ATTACK","CHRONIC FATIGUE","DIFFICULTY SLEEPING","GRINDING TEETH","SELF CRTICISM","DIGESTIVE PROBLEMS","CRYING","NO APPETITE","LOW SELF ESTEEM","INCREASES USE OF ALCHOL","WEIGHT LOSS OR GAIN","DISTRACTED","BACK PAIN","HAIR LOSS","IRREGULAR MENSTURATION CYCLE","SKIN PROBLEM","BREATHING PROBLEM","DEPRESSION","FEELING HELPLESS"]
    l1=Label(win,text="PLEASE SELECT THE SYMPTOMS",bg="lightblue")
    checkbox = [0]*len(symptom_list)
    #checkbox=Checkbutton()
    
    
    #e1 = Entry(win,width=50)
    var=[0]*len(symptom_list)
    
    def __init__(self,result):
        self.result=result
    
    def draw(self):
     
        symptom_list = self.symptom_list
       
        
       
        font_tup1 = ("Comic Sans MS", 30, "bold")
        font_tup = ("Century", 10, "bold")

        
        self.l1.place(x=0,y=0)

        
       

        
        
        for symptom in symptom_list:
            
            i = symptom_list.index(symptom)
            self.var[i] = IntVar()
            self.checkbox[i] = Checkbutton(self.win,text=symptom,font=font_tup,bg="lightblue",variable=self.var[i])
            
            if i <= int(len(symptom_list)/2):
                #self.checkbox[i].grid(row = i, column = 1)
                self.checkbox[i].place(x=90,y=(i+1)*20)
            else:
               # self.checkbox[i].grid(row = i % int(len(symptom_list)),column = 8)
                self.checkbox[i].place(x = 600, y = (i%25)*20)
                
        self.b=Button(self.win,text="SUBMIT",command=self.validation)
        self.b.place(x=400,y=600)
        
        self.win.mainloop()
       
    
  
    def validation(self):
        ass = 0
        cs = 0
        es = 0
        sym=Symptoms.symptom_list
        asl=Symptoms.acute_stress
        csl=Symptoms.chronic_stress
        esl=Symptoms.episodic_stress
        no=0
        for ind in Symptoms.symptom_list:
            i =Symptoms.symptom_list.index(ind)
           
            check=Symptoms.var[i].get()
            if check==0 :
               # print("ok")
               continue
            else :
                no=no+1
                s=sym[i]
                for j in asl:
                    
                    if s==j:
                        ass=ass+1
                        print(ass)
                for j in csl:
                    
                    if s==j:
                        cs=cs+1
                        print(cs)
                for j in esl:
                    
                    if s==j:
                        es=es+1
                        print(es)
                    
        if ass>=4:
            Symptoms.win.destroy()
            DataManagement.updateStress(DataManagement,self.result,1)
            print(self.result)
            asc=Acute_Stress()
            asc.start()
    
        if cs>=4:
            Symptoms.win.destroy()
            DataManagement.updateStress(DataManagement,self.result,2)
            csc=Chronic_Stress()
            csc.start()
        if es>=4:
            Symptoms.win.destroy()
            DataManagement.updateStress(DataManagement,self.result,3)
            
            esc=Episodic_Stress()
            esc.start()
        
        if no==0:
            messagebox.showinfo("Not Selected","Please Select The CheckBox")
            
        if no>=10:
            DataManagement.sendSms(DataManagement,self.result)
            return
            
        
        #DataManagement.set_symptoms__(Symptoms,list1)
        #DataManagement.storesymptom(DataManagement)
        
        #Symptoms.win.destroy()
  



