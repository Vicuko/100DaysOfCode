from tkinter import *
from tkinter import messagebox
from random import randint, choice, choices, shuffle
import pyperclip

FONT_NAME = "Arial"
FONT_SIZE = 14

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8,10)
    nr_symbols = randint(2,4)
    nr_numbers = randint(2,4)

    random_letters = choices(letters, k=nr_letters)
    random_symbols = choices(symbols, k=nr_symbols)
    random_numbers = choices(numbers, k=nr_numbers)

    password_list = random_letters + random_symbols + random_numbers

    # password_list += ([choice(letters) for _ in range(nr_letters)])
    # password_list += ([choice(symbols) for _ in range(nr_letters)])
    # password_list += ([choice(numbers) for _ in range(nr_letters)])

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, string=password)
    pyperclip.copy(password)

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
                # email_entry.delete(0, "end")
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
web_entry.grid(row=1, column=1, columnspan=2)

email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1, columnspan=2)

password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)

add_button.grid(row=4, column=1, columnspan=2)





window.mainloop()