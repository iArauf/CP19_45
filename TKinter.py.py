from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sample GUI")

        self.label = Label(master, text="Our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Hello", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Exit", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("Welcome1")

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()