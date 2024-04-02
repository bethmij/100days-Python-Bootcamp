# from tkinter import *
#
# window = Tk()
# window.title("Playground")
# window.minsize(width=500, height=500)
#
# label = Label(text="I am a label", font=('Arial', 20, 'normal'))
# label.pack()
#
#
# def change_text():
#     msg = input_field.get()
#     label['text'] = msg
#
#
# button = Button(text='click me', command=change_text)
# button.pack()
#
# input_field = Entry()
# input_field.pack()
#
#
# window.mainloop

from tkinter import *

window = Tk()
window.title("Playground")
window.minsize(width=500, height=500)

label = Label(text="I am a label", font=("Arial"))
label.pack()


def button_click():
    text = input.get()
    label.config(text=text)


button = Button(text="Click me here", command=button_click)
button.pack()

input = Entry(width=20)
input.pack()
window.mainloop()
