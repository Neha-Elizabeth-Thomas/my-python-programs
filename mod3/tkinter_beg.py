import tkinter as tk


def temp_convert():
    temp_c=float(entry.get())
    temp_f=temp_c*9/5+32
    result_label.config(text=f"{temp_f:.2f}F")

root=tk.Tk()
root.title('Temp convertor')

label=tk.Label(root,text="Enter temp in celsius: ")
label.pack()
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="convert",command=temp_convert)
button.pack()
result_label=tk.Label(root,text="")
result_label.pack()

root.mainloop()