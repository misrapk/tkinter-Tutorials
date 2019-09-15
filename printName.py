from tkinter import *

root = Tk()
def print_name(event):
    print("Hey! You Clicked Me!")

button1 = Button(root, text="CLICK ME!")
button1.bind("<Button-1>", print_name)
button1.pack()
root.mainloop()