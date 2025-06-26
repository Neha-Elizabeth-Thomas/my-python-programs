import tkinter as tk

class Event(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("Event Handling")
        self.master.geometry("300x200")
        self.master.resizable(True,False)
        self.master.configure(bg="light green")
        
        self.pack()
        
        self.label=tk.Label(self,text="")
        self.label.pack()
        
        def handle_leftclick(event):
            self.label.config(text=f"Mouse Left CLick at ({event.x},{event.y})")
        def handle_mouseEnter(event):
            self.label.config(text=f"Mouse entered")

        def handle_mouseMotion(event):
            pass
        def handle_mouseLeave(event):
            pass
        
        self.master.bind("<Button-1>",handle_leftclick)
        self.master.bind("<Enter>",handle_mouseEnter)
        self.master.bind("<Leave>",handle_mouseLeave)
        self.master. bind("<Motion>",handle_mouseMotion)
        
        
        
    
    
def main():
    Event().mainloop()
main()