from tkinter import *
root = Tk()

canvas = Canvas(root, width=500, height = 300)
canvas.pack()

blackline = canvas.create_line(0,0,200,50)
redLine = canvas.create_line(0,100,200,50, fill="red")
greenbox = canvas.create_rectangle(25,25,120,60, fill="green")
root.mainloop()