from tkinter import *
from cProfile import label
from Tools.demo.sortvisu import WIDTH
window=Tk()
window.geometry("1000x1000")

frame1=Frame(window,width=1000)

l1=Label(frame1,text="Enter the text")
l1.place(x=1000,y=10)

window.mainloop()