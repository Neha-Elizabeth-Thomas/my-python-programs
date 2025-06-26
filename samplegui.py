import tkinter as tk

class GUI(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("image label")
        self.master.geometry("500x500")
        self.master.configure(bg="light blue")
        self.master.resizable(True,False)
        self.grid()
        
        # self.img=tk.PhotoImage(file="smokey.gif")
        # self.label=tk.Label(self,image=self.img)
        # self.label.grid()
        
        self.textLabel=tk.Label(self,text="Smokey the Cat")
        self.textLabel.grid()
        
        self.switchButton=tk.Button(self,text="switch",command=self.switch)
        self.switchButton.grid()
    def switch(self):
        if self.textLabel["text"]=="Smokey the Cat":
            self.textLabel["text"]="Snowy the Rabbit"
        else:
            self.textLabel["text"]=="Snowy the Rabbit"
            self.textLabel["text"]="Smokey the Cat"

def main():
    GUI().mainloop()
    
main()