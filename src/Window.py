from tkinter import Tk
class Window:
    root = Tk()
    
    def __init__(self):
        
        w, h = self.root.winfo_screenwidth(),self.root.winfo_screenheight()
        #self.root.state("zoomed")
        self.root.configure(bg="lightblue")
        self.root.geometry("%dx%d+0+0" % (w,h))
        self.root.attributes('-topmost',-2)
        self.root.title("Registration Form")
        self.root.resizable(True,True)
        