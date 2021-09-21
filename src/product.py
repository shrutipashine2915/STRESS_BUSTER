from tkinter import *

    
class product:
   

    def place(self):
        root1 = Tk()
        
        root1.geometry("1450x1200")
        root=Frame(root1,height=1000,width=1000)
        text = Label(root, text='PRODUCT FOR STRESS ')
        photo = PhotoImage(file="D:/Project/Stress_Buster/src/main.png")        
        label = Label(root,image=photo)
        label.place(x=0,y=0)
        self.root.mainloop()
