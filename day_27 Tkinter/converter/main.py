from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)


def miles_to_kilometers():
    miles = float(input_mile.get())
    kilometers = miles * 1.60934
    label_ans.config(text=f"{kilometers:.2f}")


input_mile = Entry(width=10, font="Arial,40")
input_mile.grid(row=1, column=2)

label_mile = Label(text="Miles", font="Arial,40")
label_mile.grid(row=1, column=3)

label_equal = Label(text="is equal to", font="Arial,40")
label_equal.grid(row=2, column=1)

label_ans = Label(text="0", font="Arial,40")
label_ans.grid(row=2, column=2)

label_kilometer = Label(text="Kilometers", font="Arial,40")
label_kilometer.grid(row=2, column=3)

button = Button(text="Calculate", command=miles_to_kilometers, font="Arial,40")
button.grid(row=3, column=2)

window.mainloop()
