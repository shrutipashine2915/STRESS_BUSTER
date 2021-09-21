from Window import Window

from tkinter import *
from tkinter import Tk
from register import Registration
from login import Login


class Startup:
    
    def __init__(self):
        self.win=Window()
        self.root1=self.win.root
        self.root=Frame(self.root1,width=2000,height=1000)
        self.root.place(x=0,y=0)
        self.root.configure(bg="lightblue")
        
        bg = PhotoImage( file = "D:/Project/Stress_Buster/src/Images/icon.png")
        self.label1 = Label(self.root, image = bg)
        self.label1.place(x = 330,y = 0)
        
        self.register=Button(self.root, text='Register',command=self.register,width=15,height=2,bg='goldenrod2',fg='black')
        self.register.place(x=600,y=480)
        self.login=Button(self.root, text='Login',command=self.login,width=15,height=2,bg='goldenrod2',fg='black')
        self.login.place(x=800,y=480)
        self.root.mainloop()
        
    
    def register(self):
        self.root.destroy()
        a=Registration()
        a.placing()
    def login(self):
        self.root.destroy()
        a=Login()
        return
    
