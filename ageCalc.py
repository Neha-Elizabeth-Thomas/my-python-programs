import tkinter as tk
import datetime 
from dateutil.relativedelta import *

class Age(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Age calculator:")
        self.master.geometry("500x500")
        self.master.resizable(True,False)
        self.master.configure(bg="light blue")
        
        self.grid()
        
        self.bdaylabel=tk.Label(self,text="Birthday [dd/mm/yyyy]: ",bg="yellow",fg="green")
        self.bdaylabel.grid(row=0,column=0)

        self.bdayVar=tk.StringVar()
        self.bdayEntry=tk.Entry(self,textvariable=self.bdayVar)
        self.bdayEntry.grid(row=0,column=1)
        
        self.agelabel=tk.Label(self,text="Age: ",bg="light green")
        self.agelabel.grid(row=1,column=0)
        self.ageVar=tk.StringVar()
        self.ageEntry=tk.Entry(self,textvariable=self.ageVar,state="readonly")
        self.ageEntry.grid(row=1,column=1)
        
        self.btn=tk.Button(self,text="Compute Age",command=self.calcAge)
        self.btn.grid(columnspan=2)
        
    def calcAge(self):
        bday=datetime.datetime.strptime(self.bdayVar.get(),"%d/%m/%Y")
        today=datetime.datetime.now()
        age=str(relativedelta(today,bday).years)+" Years"
        self.ageVar.set(age)
def main():
    Age().mainloop()

main()