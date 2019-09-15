from tkinter import *

root = Tk()

def leftClick(event):
    print("Left Press")

def RightClick(event):
    print("Right Press")

frame = Frame(root, width = 300, height=300)
frame.bind("<Button-1>", leftClick)

frame.pack()
root.mainloop()