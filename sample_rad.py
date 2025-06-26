import tkinter as tk

class Radio(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("RadioButton Demo")
        self.master.geometry("500x500")
        self.master.resizable(True,False)
        self.master.configure(bg="light blue")
        self.pack()
        
        self.choice=tk.StringVar(value="Blood red")
        self.rbtn1=tk.Radiobutton(text="Red",value="red",variable=self.choice,command=self.show)
        self.rbtn1.pack(padx=20,pady=20)
        self.rbtn2=tk.Radiobutton(text="Blue",value="blue",variable=self.choice,command=self.show)
        self.rbtn2.pack(padx=20,pady=20)
        self.rbtn3=tk.Radiobutton(text="Green",value="green",variable=self.choice,command=self.show)
        self.rbtn3.pack(padx=20,pady=20)
        
        self.oplabel=tk.Label(self,text="Choose!!",font=("Ariel",40))  
        self.oplabel.pack(padx=20,pady=20)
        
    def show(self):
        self.oplabel.config(text=f"You have selected {self.choice.get()}")
        self.master.config(bg=self.choice.get())
        
def main():
    Radio().mainloop()
    
main()
