import tkinter

window = tkinter.Tk()
window.title("My first Tkinter window")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="My super label text", font=("Arial", 24, "italic"))
my_label.pack(expand=True)

window.mainloop()