from tkinter import *

window = Tk()
window.title("Miles to Km convertor")
window.config(padx=20, pady=20)


def compute():
    miles = float(mile_input.get())
    km = miles * 1.609
    miles_outcome_km.config(text=f"{km}")


mile_input = Entry()
mile_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

miles_km = Label(text="Km")
miles_km.grid(row=1, column=2)

miles_outcome_km = Label(text="0")
miles_outcome_km.grid(row=1, column=1)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=1, column=0)

calculate = Button(text="Calculate", command=compute)
calculate.grid(row=2, column=1)

window.mainloop()
