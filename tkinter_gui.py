import tkinter as tk

root=tk.Tk()
root.title("GUI learn")
root.geometry("500x500")

label=tk.Label(root,text="Hello World",font=('Arial',16))
label.pack(padx=20,pady=20)

textbox=tk.Text(root,height=3,font=('Arial',10))
textbox.pack()

myentry=tk.Entry(root,font=('Arial',10))
myentry.pack()

buttonframe=tk.Frame(root)
buttonframe.columnconfigure(index=0,weight=1)
buttonframe.columnconfigure(index=1,weight=1)
buttonframe.columnconfigure(index=2,weight=1)

btn1=tk.Button(buttonframe,font=('Arial',12),text='1')
btn1.grid(row=0,column=0,sticky=tk.E+tk.W)

btn2=tk.Button(buttonframe,font=('Arial',12),text='2')
btn2.grid(row=0,column=1,sticky=tk.E+tk.W)

btn3=tk.Button(buttonframe,font=('Arial',12),text='3')
btn3.grid(row=0,column=2,sticky=tk.E+tk.W)

btn4=tk.Button(buttonframe,font=('Arial',12),text='4')
btn4.grid(row=1,column=0,sticky=tk.E+tk.W)

btn5=tk.Button(buttonframe,font=('Arial',12),text='5')
btn5.grid(row=1,column=1,sticky=tk.E+tk.W)

btn6=tk.Button(buttonframe,font=('Arial',12),text='6')
btn6.grid(row=1,column=2,sticky=tk.E+tk.W)



buttonframe.pack(fill='x')
root.mainloop()