from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(10)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    tenth_mins = count//600
    mins = (count % 600) // 60
    tenth_seconds= (count % 60) // 10
    seconds = (count % 60) % 10
    counter_text = f"{tenth_mins}{mins}:{tenth_seconds}{seconds}"

    canvas.itemconfig(timer_text, text=counter_text)
    if count > 0:
        window.after(1000, count_down, count - 1)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string="Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Here we are going to use the canvas widget from tkinter.
# Here we create a canvas with the size of the image we are going to use (slightly bigger to have even numbers)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# The way tkinter canvas works is it needs the image to be stored in a PhotoImage object to later be used in the canvas:
pomodoro_picture = PhotoImage(file="./tomato.png")
# Here we include the image and indicate the x and y position to show it in the window. Slightly to the right given the image wasn't originally centered.
canvas.create_image(100, 112, image=pomodoro_picture)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
checkmark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
reset_button = Button(text="Reset", highlightthickness=0)

title_label.grid(row=0, column=1)
start_button.grid(row=2, column=0)
checkmark.grid(row=2, column=1)
reset_button.grid(row=2, column=2)




window.mainloop()
