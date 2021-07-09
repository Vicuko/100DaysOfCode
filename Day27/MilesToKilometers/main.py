from tkinter import *

window = Tk()
window.title(string="Miles-Km Converter")
window.config(padx=40, pady=20, width=500, height=300)

conversion_direction = 1
AVAILABLE_UNITS = ["Miles", "Km"]

# TODO 2: Create a function and bind it to the button to calculate the result of the conversion
def convert_units():
    if (user_input.get()):
        u_input = float(user_input.get())

        if conversion_direction:
            u_output = round(u_input * 1.609344, 3)
        else:
            u_output = round(u_input / 1.609344, 3)
        result.config(text=str(u_output))
    else:
        result.config(text="0")

# TODO 3: Create an additional button to switch the units for conversion
def switch_units():
    global conversion_direction
    new_init_unit = AVAILABLE_UNITS[conversion_direction]
    new_out_unit = AVAILABLE_UNITS[conversion_direction - 1]
    conversion_direction = abs(conversion_direction - 1)
    initial_units.config(text=new_init_unit)
    final_units.config(text=new_out_unit)

# TODO 1: Include the following elements to be shown in the grid:
#     Entry field for introducing the miles
#     Text field for the unit (miles) to the right of the entry
#     Text field including the phrase "is equal to"
#     Text field for the conversion result
#     Text field for the conversion result units
#     Button to calculate the resulting units
user_input = Entry(width=10)
user_input.insert(END, string="0.0")
initial_units = Label(text="Miles")
is_equal_text = Label(text="is equal to")
result = Label(text="0", width=10)
final_units = Label(text="Km")
calculate_button = Button(text="Convert", command=convert_units)
switch_button = Button(text="Switch", command=switch_units)

user_input.grid(row=0, column=1)
initial_units.grid(row=0, column=2)
is_equal_text.grid(row=1, column=0)
result.grid(row=1, column=1)
final_units.grid(row=1, column=2)
calculate_button.grid(row=2, column=1)
switch_button.grid(row=3, column=1)










window.mainloop()