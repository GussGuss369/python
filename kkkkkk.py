from tkinter import *
from tkinter import messagebox
is_on = True
name = ""

def clickhere():
    global is_on
    if is_on:
        l.config(text = "Hello World")
        is_on = False
    else:
        l.config(text = "Goodbye World")
        is_on = True

def clear():
    message()

def message():
    print(name_var.get())
    messagebox.askyesnocancel(title = "Hello", message = ("Is your name " + name_var.get()))

window = Tk()
name_var = StringVar()
window.title("Greetings")
l = Label(window, text = "Hello World", font = "calibri", bg = "white")
window.configure(background = "blue")
window.geometry("450x450")
window.resizable(False,False)
l.pack()

b = Button(window, text = "Click Here", font = "calibri", bg = "white", command = clickhere)
b.pack()

e = Entry(width = 30, textvariable = name_var)
e.insert(0,"some text here")
e.bind("<Button>", clear)
e.pack()

nameb = Button(window, text = "Enter name", font = "calibri", command = clear)
nameb.pack()

window.mainloop()