#creating layout
from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()              #use to display the frame on window
bottomFrame = Frame(root)
bottomFrame.pack(side= BOTTOM)

button1 = Button(topFrame, text = "Button1", fg= "red")
button2 = Button(topFrame, text = "Button2", fg= "green")
button3 = Button(topFrame, text = "Button3", fg= "blue")
button4 = Button(topFrame, text = "Button4", fg= "purple")

button1.pack()
button2.pack()
button3.pack()
button4.pack()
button1.pack(side= LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)

root.mainloop()