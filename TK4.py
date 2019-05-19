import tkinter
from tkinter import messagebox
root = tkinter.Tk()
root.geometry('350x200')


def helloCallBack():
    messagebox.showinfo("Hello python","Assalam o elikum")
B = tkinter.Button(root,text="Click here",command = helloCallBack)

B.pack()
root.mainloop()