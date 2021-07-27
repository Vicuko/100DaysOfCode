from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title(string="Flash Cards")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Create elements to be shown on the screen:
web_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
web_entry = Entry(width=24)
search_button = Button(text="Search", width=6, command=search_password)
web_entry.focus()
# web_entry.insert(0, string="www.amazingwebsite.com")

email_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
email_entry = Entry(width=35)
email_entry.insert(0, string="manolo@amazing.com")

password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
password_entry = Entry(width=24)
generate_button = Button(text="Generate", command=generate_password)
add_button = Button(text="Add", width=33, command=save_password)

#Position elements on screen:
web_label.grid(row=1, column=0)
web_entry.grid(row=1, column=1)
search_button.grid(row=1, column=2)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)

password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)

add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()