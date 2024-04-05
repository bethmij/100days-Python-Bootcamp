from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = ("Arial", 11)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    pass_letters = [random.choice(letters) for _ in range(nr_letters)]
    pass_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    pass_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = pass_letters + pass_symbols + pass_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    input_password.delete(0, END)
    input_password.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_details():
    website = input_web.get()
    email = input_email.get()
    password = input_password.get()

    if website and email and password:
        is_ok = messagebox.askokcancel(website, f"Email : {email}\nPassword : {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.writelines(f"{website} | {email} | {password}\n")
                messagebox.showinfo("Success", "Details saved!")
                input_web.delete(0, END)
                input_password.delete(0, END)

    else:
        messagebox.showerror("Error", "Please fill all fields!")


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
button_generate = Button(text="Generate", width=10, command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=36, command=add_details)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
