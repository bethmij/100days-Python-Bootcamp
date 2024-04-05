from tkinter import *

FONT = ("Arial", 10)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

text_web = Label(text="Website:", font=FONT)
text_web.grid(row=1, column=0)

input_web = Entry(width=35)
input_web.grid(row=1, column=1, columnspan=2)

text_email = Label(text="Email/Username:", font=FONT)
text_email.grid(row=2, column=0)

input_email = Entry(width=35)
input_email.grid(row=2, column=1, columnspan=2)

text_password = Label(text="Password", font=FONT)
text_password.grid(row=3, column=0)

input_password = Entry(width=21)
input_password.grid(row=3, column=1)

button_generate = Button(text="Generate Password:", command=None, width=15)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", command=None, width=36)
button_add.grid(row=4, column=1, columnspan=2)

#Entries


window.mainloop()
