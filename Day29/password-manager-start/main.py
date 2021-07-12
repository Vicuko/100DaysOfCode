from tkinter import *
from tkinter import messagebox

FONT_NAME = "Arial"
FONT_SIZE = 14

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showwarning(title="Fields uninformed", message=f"Please, don't leave any fields empty!")

    else:
        save_ok = messagebox.askokcancel(title=website, message=f"These are the details introduced: "
                                                      f"\nEmail: {email}"
                                                      f"\nPassword:{password}"
                                                      f"\nIs it ok to save?")

        if save_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                web_entry.delete(0, "end")
                email_entry.delete(0, "end")
                password_entry.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title(string="Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Create elements to be shown on the screen:
web_label = Label(text="Website:", font=(FONT_NAME, FONT_SIZE))
web_entry = Entry(width=35)
web_entry.focus()
# web_entry.insert(END, string="www.amazingwebsite.com")

email_label = Label(text="Email/Username:", font=(FONT_NAME, FONT_SIZE))
email_entry = Entry(width=35)
email_entry.insert(0, string="myamazingemail@amazing.com")

password_label = Label(text="Password:", font=(FONT_NAME, FONT_SIZE))
password_entry = Entry(width=24)
generate_button = Button(text="Generate")
add_button = Button(text="Add", width=33, command=save_password)

#Position elements on screen:
web_label.grid(row=1, column=0)
web_entry.grid(row=1, column=1, columnspan=2)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)

password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)

add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()