from tkinter import *

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_SIZE = "20"
FONT_STYLE = "italic"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=30, bg=THEME_COLOR)

        self.right_img = PhotoImage(file="./images/true.png")
        self.wrong_img = PhotoImage(file="./images/false.png")

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.score = 0
        self.score_label = Label(text=f"Score:{self.score}", bg=THEME_COLOR, fg="white", font=(FONT_NAME, FONT_SIZE))
        self.canvas_text = self.canvas.create_text(150, 125, text="Amazon...", font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, bd=0)
        self.right_button = Button(image=self.right_img, highlightthickness=0, bd=0)

        # Place elements on window
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)
        self.window.mainloop()

