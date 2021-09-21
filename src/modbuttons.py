import tkinter as tk
from tkinter import *

from _overlapped import NULL
from Window import Window
class ModButton:
    
    def __init__(self):
        self.win=Window.root
        self.root1 = self.win
        self.root=Frame(self.root1,width=1000,height=1000)
        self.root.place(x=0,y=0)
        self.root.configure(bg="lightblue")
       
    def place(self):        
        label = Label(self.root, text='WORKOUT', width=20, font=("bold",30),bg="lightblue")
        label.place(x=90, y=53)
        
        
        btn1 = Button(self.root, text = 'Day 1', command=self.day1, width=15, bd = '10',bg="lightblue")
        btn1.place(x=90, y=120)
        
        btn2 = Button(self.root, text = 'Day 2',command=self.day2, width=15, bd = '10',bg="lightblue")
        btn2.place(x=90, y=190)
        
        btn3 = Button(self.root, text = 'Day 3',command=self.day3, width=15, bd = '10',bg="lightblue")
        btn3.place(x=90, y=260)
        
        btn4 = Button(self.root, text = 'Day 4',command=self.day4, width=15, bd = '10',bg="lightblue")
        btn4.place(x=90, y=330)
        
        btn5 = Button(self.root, text = 'Day 5',command=self.day5, width=15, bd = '10',bg="lightblue")
        btn5.place(x=90, y=400)
        
        btn6 = Button(self.root, text = 'Day 6',command=self.day6, width=15, bd = '10',bg="lightblue")
        btn6.place(x=90, y=470)
        
        
        self.root.mainloop()
    def day1(self):
        root1 = tk.Toplevel()
        
        root1.geometry("1280x554")
        root=Frame(root1,height=2000,width=2000)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/Day1.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
        
    
        
    def day2(self):
        root1 = tk.Toplevel()
        
        root1.geometry("1280x400")
        root=Frame(root1,height=2000,width=2000)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/Day2.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
        
    def day3(self):
        root1 = tk.Toplevel()
        
        root1.geometry("1280x520")
        root=Frame(root1,height=2000,width=2000)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/Day3.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
    
    def day4(self):
        
        root1 = tk.Toplevel()
        
        root1.geometry("1280x480")
        root=Frame(root1,height=2000,width=2000)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/Day4.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
        
    def day5(self):
        root1 = tk.Toplevel()
        
        root1.geometry("1280x480")
        root=Frame(root1,height=2000,width=2000)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/Day5.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
        
    def day6(self):
        root1 = tk.Toplevel()
        
        root1.geometry("1280x512")
        root=Frame(root1,height=2000,width=2000)
        root.place(x=0,y=0)
        root1.attributes('-topmost',1)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/Images/Day6.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        root.mainloop()
        


