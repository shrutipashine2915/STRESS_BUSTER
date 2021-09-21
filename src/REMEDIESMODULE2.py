from tkinter import *
import tkinter as tk
from tkinter import PhotoImage
from REMEDIESPANEL import REMEDIES
from Window import Window
from _overlapped import NULL
class Episodic_Stress :
    
    
    def __init__(self):
        self.win=Window()
        self.root1 = self.win.root
        self.root1.lift()
        self.root=Frame(self.root1,width=2000,height=1000)
        self.root.place(x=0,y=0)
        self.root.configure(bg="lightblue")
        
    def start(self):
        bg = PhotoImage( file = "D:/Project/Stress_Buster/src/Images/bg1.png")
        label1 = Label(self.root, image = bg)
        label1.place(x = 460,y = 150)
        self.b = Button(self.root, text="Remedies" ,command=lambda:self.cRemides(),font=("Comic Sans MS", 8, "bold"), bd=10, bg="goldenrod2", width= 25 , height = 2)
        self.c = Button(self.root, text="Product",command=self.cProduct,font=("Comic Sans MS", 8, "bold"), bd=10, bg="goldenrod2", width= 25, height=2)
        self.b.place(x = 710, y = 500, anchor=CENTER)
        self.c.place(x = 910, y = 500,anchor=CENTER)
        self.root1.mainloop()
    def cRemides(self):
        
        self.root.destroy()
        a=REMEDIES()
        a.form(3)
        return
    def cProduct(self):
        
        root1 = tk.Toplevel()
        root1.geometry("1080x640")
        root=Frame(root1,height=1000,width=1080)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/EpisodicStressProduct.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
        return
        

#Episodic_Stress.start(Episodic_Stress)
    
