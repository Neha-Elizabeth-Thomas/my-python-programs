import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.root=tk.Tk()
        self.root.geometry("500x500")   
        self.root.title("RadioButtons Demo")
        
        self.choice=tk.StringVar(value=" ")
        self.rbtn1=tk.Radiobutton(text="Red",value="red",variable=self.choice,command=self.show)
        self.rbtn1.pack(padx=10,pady=10)
        self.rbtn2=tk.Radiobutton(text="Green",value="Green",variable=self.choice,command=self.show)
        self.rbtn2.pack(padx=10,pady=10)
        self.rbtn3=tk.Radiobutton(text="Blue",value="Blue",variable=self.choice,command=self.show)
        self.rbtn3.pack(padx=10,pady=10)
        
        self.label=tk.Label(self.root,text="Select a color",font=('Arial',12))
        self.label.pack()
        self.root.mainloop()
        
    def show(self):
        print(f"You have selected {self.choice.get()}")
        self.label.config(text=f"You have selected {self.choice.get()}")

        
GUI()