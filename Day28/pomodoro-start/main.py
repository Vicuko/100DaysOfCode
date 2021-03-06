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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    print(reps)
    if reps % 8 == 0:
        text_description = "Break"
        text_color = RED
        counter = long_break_sec
    elif reps % 2 == 0:
        text_description = "Break"
        text_color = PINK
        counter = short_break_sec
    else:
        text_description = "Work"
        text_color = GREEN
        counter = work_sec
    title_label.config(text=text_description, fg=text_color)
    count_down(counter)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    tenth_mins = int(count//600)
    mins = int((count % 600) // 60)
    tenth_seconds = int((count % 60) // 10)
    seconds = int((count % 60) % 10)
    counter_text = f"{tenth_mins}{mins}:{tenth_seconds}{seconds}"

    canvas.itemconfig(timer_text, text=counter_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        #Now we update the number of work rounds completed:
        checkmark.config(text=("✔" * (reps//2)))

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
checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)

title_label.grid(row=0, column=1)
start_button.grid(row=2, column=0)
checkmark.grid(row=2, column=1)
reset_button.grid(row=2, column=2)




window.mainloop()
