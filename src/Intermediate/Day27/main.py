from tkinter import *


def miles_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    kilometer_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometers Converts Project")
window.config(padx=100, pady=100)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(text="0")
kilometer_label.grid(column=2, row=1)

kilometer_results = Label(text="km")
kilometer_results.grid(column=1, row=1)

button = Button(text="Convert", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
