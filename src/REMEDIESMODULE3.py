from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from REMEDIESPANEL import *
from Window import Window

class Chronic_Stress :
    
    def __init__(self):
        self.win=Window()
        self.root1 = self.win.root
        
        self.root=Frame(self.root1,width=2000,height=1000)
        self.root.place(x=0,y=0)
        self.root.configure(bg="lightblue")
        
    def start(self):
        bg = PhotoImage( file = "D:/Project/Stress_Buster/src/Images/bg2.png")
        label1 = Label(self.root, image = bg)
        label1.place(x = 400,y = 200)
        self.b = Button(self.root, text="Remedies" ,command=lambda:self.cRemides(),font=("Comic Sans MS", 8, "bold"), bd=10, bg = "HotPink2", width= 25 , height = 2)
        self.c = Button(self.root, text="Product",command=self.cProduct,font=("Comic Sans MS", 8, "bold"), bd=10, bg = "HotPink2", width= 25, height=2)
        self.b.place(x = 710, y = 500, anchor=CENTER)
        self.c.place(x = 910, y = 500,anchor=CENTER)
        self.root1.mainloop()
        
    def cRemides(self):
        
        self.root.destroy()
        a=REMEDIES()
        a.form(2)
    def cProduct(self):
        
        root1 = tk.Toplevel()
        root1.geometry("1080x640")
        root=Frame(root1,height=1000,width=1080)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/ChronicStressProduct.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
        return
        
    
#Chronic_Stress.start(Chronic_Stress)

        

