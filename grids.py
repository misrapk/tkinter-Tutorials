#--------------------Grid Layout----------------------
from tkinter import *
root = Tk()

labelOne = Label(root,text="Name")
labelTwo = Label(root, text = "Password")

#text boxes
entryOne = Entry(root)
entryTwo = Entry(root)
labelOne.grid(row = 0)
labelTwo.grid(row = 2)
entryOne.grid(row = 0, column = 1)
entryTwo.grid(row = 2, column = 1)

c = Checkbutton(root, text="Keep me LoggedIn")
c.grid(columnspan = 2)
root.mainloop()
