from tkinter import *

def doNothing():
    print("Ok Ok OK")


root = Tk()
frame = Frame(root, width = 300, height=300)


#create MenuBar

menu = Menu(root)
root.config(menu = menu)
subMenu = Menu(menu)
menu.add_cascade(label= "File", menu= subMenu)

subMenu.add_command(label= "New Project...", command= doNothing)

subMenu.add_separator()
subMenu.add_command(label= "Exit", command= subMenu.quit)
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu = editMenu)
editMenu.add_command(label="Redo", command=doNothing)

#create a toolbar
toolbar = Frame(root, bg = "orange")
insertButt = Button(toolbar, text= "Insert", command= doNothing)

insertButt.pack(side = LEFT, padx = 2, pady =2 )
printButt = Button(toolbar, text = "Print", command= doNothing)
printButt.pack(side = LEFT, padx=2, pady = 3)
toolbar.pack(side = TOP, fill = X)

#create statusBar

status = Label(root, text = "This is toolbar", bd = 1, relief = SUNKEN, anchor= W)
status.pack(side=BOTTOM, fill = X)

frame.pack()
root.mainloop()
