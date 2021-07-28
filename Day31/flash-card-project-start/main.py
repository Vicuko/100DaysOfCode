from tkinter import *
import pandas as pd
import random

FRONT_COLOR = "#000000"
BACK_COLOR = "#FFFFFF"
BACKGROUND_COLOR = "#B1DDC6"

FONT_NAME = "Arial"
TITLE_FONT_SIZE = 40
TITLE_FONT_STYLE = "italic"
WORD_FONT_SIZE = 60
WORD_FONT_STYLE = "bold"
timer = None

window = Tk()
window.title(string="Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

csv_data = pd.read_csv("./data/french_words.csv")
words_data = csv_data.to_dict(orient="records")
print(words_data)

current_word = 0

#Functions for logic
def show_new_word():
    global current_word
    global timer
    if words_data:
        current_word = random.randint(0,len(words_data)-1)
        french_word = words_data[current_word]["French"]

        #Update canvas content:
        canvas.itemconfig(title, text="French", fill=FRONT_COLOR)
        canvas.itemconfig(word, text=french_word, fill=FRONT_COLOR)
        canvas.itemconfig(canvas_image, image=card_front)

        timer = window.after(3000, show_back)

def show_back():
    # global timer
    # window.after_cancel(timer)
    english_word = words_data[current_word]["English"]

    # Update canvas content:
    canvas.itemconfig(title, text="English", fill=BACK_COLOR)
    canvas.itemconfig(word, text=english_word, fill=BACK_COLOR)
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(canvas_image, image = card_back)

def wrong_function():
    # window.after_cancel(timer)
    show_new_word()

def right_function():
    # window.after_cancel(timer)
    show_new_word()

#Elements to be shown on the screen
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="Title", font=(FONT_NAME, TITLE_FONT_SIZE, TITLE_FONT_STYLE))
word = canvas.create_text(400, 263, text="Word", font=(FONT_NAME, WORD_FONT_SIZE, WORD_FONT_STYLE))
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, command=wrong_function)
right_button = Button(image=right_img, highlightthickness=0, bd=0, command=right_function)

#Place elements on window
canvas.grid(row=0, column=0, columnspan=2)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

window.mainloop()