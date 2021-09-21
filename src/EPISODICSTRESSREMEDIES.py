from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
class Remedies():
    top = Tk()
    top.geometry("1000x1000")
    Lb1 = Listbox(top, height=50, width=150)
    def placing(self):
        root = Tk()
        root.title("")
        root.geometry("1000x1000")
        root.attributes('-topmost',1)
        root.configure(bg="paleturquoise")
        
        label = Label(root, text="Home Remedies", bg="paleturquoise",fg="black", font=("comic sans MS", 30, "bold"))
        label.place(x=5, y=0)
       
       
        label0 = Label(root, text="Drink Ginger Tea Or Coffee", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label0.place(x=5, y=80)

        label1 = Label(root, text="Eat Chocolates Or Icecream", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label1.place(x=5, y=120)
        
        label2 = Label(root, text="Play Outdoor Games ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label2.place(x=5, y=160)
        
        label3 = Label(root, text="Laught or Cry", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label3.place(x=5, y=200)

        label4 = Label(root, text="Take a Yoga Class", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label4.place(x=5, y=240)
        
        label5 = Label(root, text="Chew A Gum", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label5.place(x=5, y=280)
        
        label6 = Label(root, text="Take Some Fresh Air ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label6.place(x=5, y=320)

        label7 = Label(root, text="Cuddle", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label7.place(x=5, y=360)

        label8 = Label(root, text="Play With Your Pet", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label8.place(x=5, y=400)

        label9= Label(root, text="Deep Breathing", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label9.place(x=5, y=440)
        
        

        root.mainloop()

       
