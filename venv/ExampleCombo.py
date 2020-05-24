from tkinter import *
from tkinter import ttk
def func():
    l2.configure(text=cb.get())
root=Tk()
root.geometry('200x100')
course=("Java","Python","C","C++")
l1=Label(root,text="Choose your fav Lang")
l1.grid(column=0,row=0)
cb=ttk.Combobox(root,values=course,width=15)
cb.grid(column=0,row=2)
cb.current(1)
b=Button(root,text="Click me",command=func)
b.grid(column=0,row=3)
l2=Label(root,text="")
l2.grid(column=0,row=3)
root.mainloop()