from tkinter import *

window = Tk()
window.title("My first Tkinter window")
window.minsize(width=500, height=300)

#Label

my_label = Label(text="My super label text", font=("Arial", 24, "italic"))
my_label.pack()

#Several ways to update the text content:
my_label["text"]="Bla bla bla2"
my_label.config(text="New Text")

#Button

button = Button(text="Click Me")
button.pack()




window.mainloop()