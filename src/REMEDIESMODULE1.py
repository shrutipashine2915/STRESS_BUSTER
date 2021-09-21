from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from REMEDIESPANEL import REMEDIES 
from Window import Window
from itertools import product
from product import product
from _overlapped import NULL

class Acute_Stress :
    
    root=NULL
    def __init__(self):
        self.win=Window()
        self.root1 = self.win.root
        self.root1.lift()
        self.root=Frame(self.root1,width=2000,height=1000)
        self.root.place(x=0,y=0)
        self.root.configure(bg="lightblue")
    

    def start(self):
        #print(os.listdir())
        
        bg = PhotoImage( file = "D:/Project/Stress_Buster/src/Images/bg.png")
        label1 = Label(self.root, image = bg)
        label1.place(x = 480,y = 150)
        self.b = Button(self.root, text="Remedies" ,command=lambda:self.cRemides(),font=("Comic Sans MS", 8, "bold"),bg = "tomato2",bd=10, width= 25 , height = 2)
        self.c = Button(self.root, text="Product",command=Acute_Stress.cProduct,font=("Comic Sans MS", 8, "bold"),bg = "tomato2",bd=10, width= 25, height=2)
        self.b.place(x = 620, y = 500)
        self.c.place(x = 830, y = 500)
        
        print("Hello world")
        self.root.mainloop()
        
    def cRemides(self):
        self.root.destroy()
        a=REMEDIES()
        a.form(1)
        return
    def cProduct():
        
        root1 = tk.Toplevel()
        
        root1.geometry("1080x640")
        root=Frame(root1,height=1000,width=1080)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/AcuteStressProduct.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
        
        







