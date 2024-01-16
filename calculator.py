from tkinter import *
getting = ""
def number(num):
    global getting
    getting = getting + str(num)
    equation.set(getting)
    return

def clear():
    global getting
    getting = ""
    equation.set("")
    return

def equal():
    try:
        global getting 
        everythin = str(eval(getting))
        equation.set(everythin)
        getting = ""
        return 
    except SyntaxError:
        equation.set("Error")
        getting = ""
if __name__ == '__main__':
    root = Tk()
    title_1= root.title('KP Calculator')
    equation = StringVar()

    white_space = Entry(root, width=35, borderwidth=5, textvariable=equation)
    white_space.grid(row=0,column=0,columnspan=5, padx=10, pady= 10)
    button_1 = Button(root, text = '1', command=lambda: number(1))
    button_2 = Button(root, text = '2', command=lambda: number(2))
    button_3 = Button(root, text = '3', command=lambda: number(3))
    button_4 = Button(root, text = '4', command=lambda: number(4))
    button_5 = Button(root, text = '5', command=lambda: number(5))
    button_6 = Button(root, text = '6', command=lambda: number(6))
    button_7 = Button(root, text = '7', command=lambda: number(7))
    button_8 = Button(root, text = '8', command=lambda: number(8))
    button_9 = Button(root, text = '9', command=lambda: number(9))
    button_0 = Button(root, text = '0', command=lambda: number(0))
    button_point = Button(root, text= '.', command= lambda: number('.'))
    button_clear = Button(root, text = 'Clear',command=clear)
    button_multiply = Button(root,text = 'x', command=lambda: number('*'))
    button_plus = Button(root,text = '+', command=lambda: number('+'))
    button_minus = Button(root,text = '-', command=lambda: number('-'))
    button_equal = Button(root,text = '=', command=equal)
    button_divide = Button(root,text = '/', command=lambda: number('/'))

    button_1.grid(row=3,column=1)
    button_2.grid(row=3,column=2)
    button_3.grid(row=3,column=3)
    button_4.grid(row=2,column=1)
    button_5.grid(row=2,column=2)
    button_6.grid(row=2,column=3)
    button_7.grid(row=1,column=1)
    button_8.grid(row=1,column=2)
    button_9.grid(row=1,column=3)
    button_0.grid(row=4,column=1)
    button_point.grid(row=4, column=2)
    button_clear.grid(row=4,column=3)
    button_plus.grid(row=1,column=4)
    button_minus.grid(row=2,column=4)
    button_equal.grid(row=4)
    button_multiply.grid(row=3,column=4)
    button_divide.grid(row=4,column=4)
    root.mainloop()