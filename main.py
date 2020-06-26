from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from login import *

from signup import *

class digital:
    def logino(self):
        self.root.destroy()
        obj=log()

    def signupit(self):
        obj = signup()

    def __init__(self):
        self.root=Tk()
        self.root.title("Account")
        self.root.geometry("320x90")
        self.hd=Label(self.root,text="Welcome to My Project")
        self.hd.config(font=("Courier", 10))
        self.lgin=Label(self.root,text="Already Have Account")
        self.bt1=Button(self.root,text="Login",command=self.logino)
        self.signup=Label(self.root,text="Create New Account")
        self.bt2=Button(self.root,text="Sign up",command=lambda :[self.signupit()])

        self.hd.grid(row=0,column=0)
        self.lgin.grid(row=2,column=0)
        self.bt1.grid(row=2,column=1)
        self.signup.grid(row=3,column=0)
        self.bt2.grid(row=3,column=1)
        self.root.mainloop()

#-----------------------------

obj=digital()