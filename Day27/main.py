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

def button_clicked():
    my_label["text"] = "This button just got clicked!"
    # my_label.config(text="This button just got clicked!")

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Input field

input = Entry(width=10)
input.pack()




window.mainloop()