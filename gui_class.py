import tkinter as tk
from tkinter import messagebox

class myGUI:
    def __init__(self):
        self.root=tk.Tk()
        
        self.menu_bar=tk.Menu(self.root)

        self.filemenu=tk.Menu(self.menu_bar,tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Save")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit",command=self.onclosing)        
        
        self.menu_bar.add_cascade(label="File",menu=self.filemenu)
        
        self.root.config(menu=self.menu_bar)

        self.label=tk.Label(self.root,text="NEter your msg: ",font=('Arial',16))
        self.label.pack(padx=10,pady=10)
        
        self.textbox=tk.Text(self.root,height=2,font=('Arial',16))
        self.textbox.bind("<KeyPress>",self.handleEvent)
        self.textbox.pack(padx=10,pady=10)
        
        self.check_status=tk.IntVar()
        self.checkbox=tk.Checkbutton(self.root,text="Click to show message",font=('Arial',14),variable=self.check_status)
        self.checkbox.pack(padx=10,pady=10)
        
        self.btn=tk.Button(self.root,text="Click me",command=self.showMsg)
        self.btn.pack(padx=10,pady=10)
        
        self.root.protocol("WM_DELETE_WINDOW",self.onclosing)
        self.root.mainloop()
        
    def showMsg(self):
        if(self.check_status.get()==0):
            print(self.textbox.get("1.0",tk.END))
        else:
            messagebox.showinfo(title="Show message",message=self.textbox.get("1.0",tk.END))
            
    def handleEvent(self,event):
        if(event.state==12 and event.keysym=="Return"):
            self.showMsg()

    def onclosing(self):
        if(messagebox.askyesno(title="Quit",message="Do you want ot close? ")):
            self.root.destroy()

myGUI()