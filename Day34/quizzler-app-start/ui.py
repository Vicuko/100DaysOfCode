from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_SIZE = "20"
FONT_STYLE = "italic"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.true_img = PhotoImage(file="./images/true.png")
        self.false_img = PhotoImage(file="./images/false.png")

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white", font=(FONT_NAME, FONT_SIZE))
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, width=260, text="Amazon...", fill=THEME_COLOR, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
        self.false_button = Button(image=self.false_img, highlightthickness=0, bd=0, command=lambda: self.answer_click("False"))
        self.true_button = Button(image=self.true_img, highlightthickness=0, bd=0, command=lambda: self.answer_click("True"))

        # Place elements on window
        self.score_label.grid(row=0, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=next_question)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_click(self, result: str):
        self.give_feedback(self.quiz.check_answer(result))

    def give_feedback(self, correct):
        canvas_bg_color = "green" if correct else "red"
        self.canvas.config(bg=canvas_bg_color)
        self.window.after(1000, lambda: self.get_next_question())

