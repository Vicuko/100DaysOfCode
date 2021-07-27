from tkinter import *

FRONT_COLOR = "#FFFFFF"
BACKGROUND_COLOR = "#B1DDC6"

FONT_NAME = "Arial"
TITLE_FONT_SIZE = 40
TITLE_FONT_STYLE = "italic"
WORD_FONT_SIZE = 60
WORD_FONT_STYLE = "bold"

window = Tk()
window.title(string="Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

#Functions for logic
def wrong_function():
    pass

def right_function():
    pass

def switch_background():
    # To replace image:
    # self.canvas.itemconfig(self.image_on_canvas, image = ...)
    pass

#Elements to be shown on the screen
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front)
title_label = Label(text="Title", font=(FONT_NAME, TITLE_FONT_SIZE, TITLE_FONT_STYLE), bg=FRONT_COLOR)
word_label = Label(text="Word", font=(FONT_NAME, WORD_FONT_SIZE, WORD_FONT_STYLE), bg=FRONT_COLOR)
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=wrong_function)
right_button = Button(image=right_img, highlightthickness=0, bd=0, command=right_function)

#Place elements on window
canvas.grid(row=0, column=0, columnspan=2)
title_label.place(x=400, y=150, anchor="center")
word_label.place(x=400, y=263, anchor="center")
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

window.mainloop()