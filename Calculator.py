#calculator GUI
from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    textInput.set(operator)

def btnClear():
    global operator
    operator = ""
    textInput.set("")

def btnEqual():
    global operator
    sumup = str(eval(operator))
    textInput.set(sumup)
    operator = ""


cal = Tk()

cal.title("My Calculator")

operator = ""
textInput = StringVar()
textDisp = Entry(cal, font = ('arial', 20, 'bold'), textvariable = textInput, bd = 30, insertwidth = 4, bg = "white", justify =  'right').grid(columnspan =4)

btn7 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "7", bg = "skyblue", command = lambda:btnClick(7)).grid(row=1, column =0)
btn8 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "8", bg = "skyblue", command = lambda:btnClick(8)).grid(row=1, column =1)
btn9 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "9", bg = "skyblue", command = lambda:btnClick(9)).grid(row=1, column =2)
btnadd = Button(cal, padx = 15, pady=16, bd = 8, fg = "yellow", font=('arial', 20, 'bold'),text= "+", bg = "red", command = lambda:btnClick("+")).grid(row=1, column =3)
btn4 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "4", bg = "skyblue", command = lambda:btnClick(4)).grid(row=2, column =0)
btn5 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "5", bg = "skyblue", command = lambda:btnClick(5)).grid(row=2, column =1)
btn6 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "6", bg = "skyblue", command = lambda:btnClick(6)).grid(row=2, column =2)
btnsub = Button(cal, padx = 16, pady=16, bd = 8, fg = "yellow", font=('arial', 20, 'bold'),text= "-", bg = "red", command = lambda:btnClick("-")).grid(row=2, column =3)
btn1 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "1", bg = "skyblue", command = lambda:btnClick(1)).grid(row=3, column =0)
btn2 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "2", bg = "skyblue", command = lambda:btnClick(2)).grid(row=3, column =1)
btn3 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "3", bg = "skyblue", command = lambda:btnClick(3)).grid(row=3, column =2)
btnmul = Button(cal, padx = 16, pady=16, bd = 8, fg = "yellow", font=('arial', 20, 'bold'),text= "*", bg = "red", command = lambda:btnClick("*")).grid(row=3, column =3)
btndot = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= ".", bg = "skyblue", command = lambda:btnClick(".")).grid(row=4, column =0)
btn0 = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "0", bg = "skyblue", command = lambda:btnClick(0)).grid(row=4, column =1)
btnclr = Button(cal, padx = 16, pady=10, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "C", bg = "skyblue", command = btnClear).grid(row=4, column =2)
btneql = Button(cal, padx = 16, pady=16, bd = 8, fg = "green", font=('arial', 20, 'bold'),text= "=", bg = "orange", command = btnEqual).grid(row=4, column =3)

cal.mainloop()
