from tkinter import *
from Window import Window
from Music import music
from Remedies import Remedies
from modbuttons import ModButton
import ACUTESTRESSREMEDIES
import CHRONICSTRESSREMEDIES
import EPISODICSTRESSREMEDIES
import Tic1
from Tic1 import Tic

class REMEDIES:
    
    def __init__(self):
        self.win=Window()
        self.root1 = self.win.root
        self.root=Frame(self.root1,width=1000,height=1000)
        self.root.place(x=0,y=0)
        self.root.configure(bg="lightblue")
        
    def form(self,i):
        
        label1 = Label(self.root, text="REMEDIES.....",width=20,font=("bold", 20),bg="lightblue")
        label1.place(x=30,y=50)
        self.i=i
        


        self.hm=Button(self.root, text='HOME REMEDIES',command=self.ghome,width=30,font=("Comic Sans MS", 8, "bold"), bd=10, bg="goldenrod2")
        self.hm.place(x=90,y=150)
        self.w=Button(self.root, text='WORKOUT',command=self.gworkout,width=30,fg='black',font=("Comic Sans MS", 8, "bold"), bd=10, bg="goldenrod2")
        self.w.place(x=90,y=200)
        self.m=Button(self.root, text='MUSIC',command=self.gmusic,width=30,font=("Comic Sans MS", 8, "bold"), bd=10, bg="goldenrod2")
        self.m.place(x=90,y=250)
        self.a=Button(self.root,text='ACTIVITES',command=self.activites,width=30,font=("Comic Sans MS", 8, "bold"), bd=10, bg="goldenrod2")
        self.a.place(x=90,y=300)

        print("num->",self.i)
        self.root.mainloop()
    
    def activites(self):
        
        a=Tic()
        a.main()        
        
        
        return
    def gmusic(self):
        mp=music.MusicPlayer(Window.root)
    
    def gworkout(self):
        self.root.destroy()
        mb=ModButton()
        mb.place()
        
        return
    def ghome(self):
        if self.i==1 :
            root = Tk()
            root.title("")
            root.geometry("1000x1000")
            root.attributes('-topmost',1)
            root.configure(bg="paleturquoise")
            
            label = Label(root, text="Home Remedies", bg="paleturquoise",fg="black", font=("comic sans MS", 30, "bold"))
            label.place(x=5, y=0)
            
            label0 = Label(root, text="Drink Ginger Tea Or Coffee", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label0.place(x=5, y=80)
    
            label1 = Label(root, text="Medication", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label1.place(x=5, y=120)
            
            label2 = Label(root, text="Play Video Games ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label2.place(x=5, y=160)
            
            label3 = Label(root, text="Watch TV", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label3.place(x=5, y=200)
    
            label4 = Label(root, text="Take a Yoga Class", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label4.place(x=5, y=240)
            
            label5 = Label(root, text="Chew A Gum", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label5.place(x=5, y=280)
            
            label6 = Label(root, text="Take Some Fresh Air ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label6.place(x=5, y=320)
            
            label6 = Label(root, text="Deep Breathing ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label6.place(x=5, y=360)
            
            label7= Label(root, text="Take Proper Sleep", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label7.place(x=5, y=400)
    
    
            label9= Label(root, text="Drink Plenty Of Water", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label9.place(x=5, y=440)
    
    
    
            label10= Label(root, text="Eat Healthy", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label10.place(x=5, y=480)
                  
    
            root.mainloop()
        if self.i==2:
            print("I am On")
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
            label1.place(x=5, y=110)
            
            label2 = Label(root, text="Play Outdoor Games ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label2.place(x=5, y=140)
            
            label3 = Label(root, text="Laught or Cry", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label3.place(x=5, y=170)
    
            label4 = Label(root, text="Take a Yoga Class", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label4.place(x=5, y=200)
            
            label5 = Label(root, text="Chew A Gum", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label5.place(x=5, y=230)
            
            label6 = Label(root, text="Take Some Fresh Air ", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label6.place(x=5, y=260)
    
            label7 = Label(root, text="Cuddle", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label7.place(x=5, y=290)
    
            label8 = Label(root, text="Play With Your Pet", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label8.place(x=5, y=320)
    
            label9= Label(root, text="Deep Breathing", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label9.place(x=5, y=350)
            
            label10= Label(root, text="Talk To Your Close One About Your Problems", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label10.place(x=5, y=380)
    
    
            label11= Label(root, text="Medication", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label11.place(x=5, y=410)
    
    
    
            label12= Label(root, text="Play Video Games", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label12.place(x=5, y=440)
    
    
            label13= Label(root, text="Watch Tv", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label13.place(x=5, y=470)
    
            label14= Label(root, text="Take Proper Sleep", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label14.place(x=5, y=500)
    
    
            label15= Label(root, text="Drink Plenty Of Water", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label15.place(x=5, y=530)
    
    
    
            label16= Label(root, text="Eat Healthy", bg="paleturquoise",fg="black", font=("century", 15, "bold"))
            label16.place(x=5, y=560)
                  
            root.mainloop()
        if self.i==3 :
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
        

        
            
#REMEDIES.form(REMEDIES)
        

        

        