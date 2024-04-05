from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.pack()

text_web = Label(text="Website", font=("Arial", 20, "bold"), bg="")
input_web = Entry(width=35)
text_email = Label(text="Email/Username", font=(""))

window.mainloop()
