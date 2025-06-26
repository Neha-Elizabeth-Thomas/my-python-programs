import tkinter as tk
import math
class GUI(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("my gui")
        self.master.geometry("500x500")
        # self.master.resizable(True,False)
        self.master.configure(bg="light blue")
        self.master.columnconfigure(0,weight=1)
        self.master.rowconfigure(0,weight=1)
        self.grid(sticky=tk.N+tk.E+tk.W+tk.S)
        
        for row in range(2):
            self.rowconfigure(row,weight=1)
            self.columnconfigure(row,weight=1)

        self.radiuslabel=tk.Label(self,text="Radius: ")
        self.radiuslabel.grid(row=0,column=0,sticky=tk.N+tk.E+tk.W+tk.S)
        self.radiusVar=tk.DoubleVar()
        self.radiusEntry=tk.Entry(self,textvariable=self.radiusVar)
        self.radiusEntry.grid(row=0,column=1,sticky=tk.N+tk.E+tk.W+tk.S)
         
        self.arealabel=tk.Label(self,text="Area:")
        self.arealabel.grid(row=1,column=0,sticky=tk.N+tk.E+tk.W+tk.S)
        self.areaVar=tk.DoubleVar(value=0)
        self.areaEntry=tk.Entry(self,textvariable=self.areaVar,state="readonly")
        self.areaEntry.grid(row=1,column=1,sticky=tk.N+tk.E+tk.W+tk.S)
        
        self.button=tk.Button(self,text="compute",command=self.compute)
        self.button.grid(columnspan=2,sticky=tk.N+tk.E+tk.W+tk.S)

    def compute(self):
        try:
            r=self.radiusVar.get()
            area=math.pi*r**2
            self.areaVar.set(area)
        except(ValueError):
            tk.messagebox.showerror(self,message="Incorrect datatype for radius")
def main():
    GUI().mainloop()
    
main()
