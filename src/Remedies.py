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
        
        label = Label(root, text=" PLAY", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=70)
        
        label = Label(root, text=" LAUGH ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=105)
        
        label = Label(root, text=" CHEW A GUM ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=140)
        
        label = Label(root, text=" LEARN TO SAY NO ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=175)
        
        label = Label(root, text=" EXERCISE", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=210)
        
        label = Label(root, text=" LIGHT A CANDLE ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=245)
        
        label = Label(root, text=" REDUCE YOUR CAFFEINE INTAKE ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=280)
        
        label = Label(root, text=" TAKE A YOGA CLASS ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=315)
        
        label = Label(root, text=" CUDDLE ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=350)
        
        label = Label(root, text=" PRACTICE MINDFULNESS ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=385)
        
        label = Label(root, text=" PRACTICE LETTING GO ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=420)
        
        label = Label(root, text=" LISTEN TO SOOTHING MUSIC ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=455)
        
        label = Label(root, text=" DEEP BREATHING ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=490)
        
        label = Label(root, text=" SPEND TIME WITH PET ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=525)
        
        label = Label(root, text=" LEARN TO AVOID PROCRASTINATION ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=560)
        
        label = Label(root, text=" GET OUTDOOR FOR A BREAK ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=595)
        
        label = Label(root, text=" DRINK PLENTY OF WATER ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=630)
        
        label = Label(root, text=" EAT SMALL  ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=665)
        
        label = Label(root, text=" LEARN TO DANCE ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=700)
        
        
        label = Label(root, text=" CONSIDER SUPPLIMENTS ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
        label.place(x=5, y=735)

        root.mainloop()

       
