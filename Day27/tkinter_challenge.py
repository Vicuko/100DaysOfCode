from tkinter import *

window = Tk()
window.title(string = "Challenge Window")
window.minsize(width=500, height=300)

label = Label(text="Label 1", font=("Arial", 24, "italic"))
label.grid(row=0, column=0)

button1 = Button(text="Button 1")
button1.grid(row=1, column=1)

button2 = Button(text="Button 2")
button2.grid(row=0, column=2)

entry = Entry(width=30)
entry.grid(row=2, column=3)









window.mainloop()
