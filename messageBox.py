from tkinter import *
import tkinter.messagebox

root = Tk()
frame = Frame(root, width =500, height= 500)

tkinter.messagebox.showinfo("Title","messageBox info")
answer = tkinter.messagebox.askquestion("Question1", "Do you know me?")

if answer =="yes":
    print("Ohh great!")
else: 
    print("no problem")



frame.pack()
root.mainloop()