from tkinter import *

FONT = ("Arial", 11)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    website = input_web.get()
    email = input_email.get()
    password = input_password.get()


    if website and email and password:
        with open("data.txt", "a") as file:
            file.writelines(f"{website} | {email} | {password}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Entries
input_web = Entry(width=39)
input_web.focus()
input_web.grid(row=1, column=1, columnspan=2)

input_email = Entry(width=39)
input_email.insert(0, "bethmij@gmail.com")
input_email.grid(row=2, column=1, columnspan=2)

input_password = Entry(width=22)
input_password.grid(row=3, column=1)

# Labels
text_web = Label(text="Website:", font=FONT)
text_web.grid(row=1, column=0)

text_email = Label(text="Email/Username:", font=FONT)
text_email.grid(row=2, column=0)

text_password = Label(text="Password", font=FONT)
text_password.grid(row=3, column=0)

# Buttons
button_generate = Button(text="Generate", width=10)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=add_details)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
