from tkinter import *


def clickhere():
    count = 1
    if True:
        count += 1
        if count % 2 == 0:
            l.config(text = "Goodbye World")
        else:
            l.config(text = "Goodbye World")

window = Tk()
window.title("Greetings")
l = Label(window, text = "Hello World")
l.pack()
b = Button(window, text = "Click Here", command = clickhere)
b.pack()

window.mainloop()