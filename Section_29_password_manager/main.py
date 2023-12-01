import tkinter as tk
from tkinter import messagebox
import random
import string

LETTERS = list(string.ascii_letters)
NUMBERS = [str(num) for num in list(range(0, 10))]
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    """generate a random password and populate password field"""
    random_password = []
    random_password += ([random.choice(LETTERS) for _ in range(10)])
    random_password += ([random.choice(NUMBERS) for _ in range(5)])
    random_password += ([random.choice(SYMBOLS) for _ in range(5)])
    random.shuffle(random_password)

    password_entry.insert(0, "".join(random_password))

# ---------------------------- SAVE PASSWORD ------------------------------- #

def website():
    """gets website entry"""
    return website_entry.get()

def email():
    """gets email entry"""
    return email_entry.get()

def password():
    """gets password entry"""
    return password_entry.get()

def is_valid():
    """checks to see if all fields are filled in"""
    return len(website()) > 0 and len(email()) > 0 and len(password()) > 0

def save_to_file():
    """saves the entry to the file"""
    with open("passwords.txt", "a") as file:
        entry = f"{website()} | {email()} | {password()}\n"
        file.write(entry)

def is_okay_to_save():
    """ask user if they are okay to save"""
    return messagebox.askokcancel(
            title=website(), message=f"These are the details:\nWebsite:{website()}\n"
                                     f"Email:{email()}\nPassword:{password()}\nIs it okay to save?"
    )

def save_and_reset_if_okay():
    """make sure user is okay with entry then save and reset"""
    if is_okay_to_save():
        save_to_file()
        reset_fields()

def populate_email_entry():
    """inserts default email"""
    email_entry.insert(0, "duncan@foomail.com")

def reset_fields():
    """clear out the field entries"""
    for entry in [website_entry, email_entry, password_entry]:
        entry.delete(0, len(entry.get()))
    populate_email_entry()

def save():
    """save password file"""
    if is_valid():
        save_and_reset_if_okay()
    else:
        messagebox.showinfo(title="Sorry", message="Please don't leave any fields empty.")
# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website")
email_label = tk.Label(text="Email")
password_label = tk.Label(text="Password")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry = tk.Entry(width=39)
email_entry = tk.Entry(width=39)
password_entry = tk.Entry(width=22)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry.grid(column=1, row=2, columnspan=2)
populate_email_entry()
password_entry.grid(column=1, row=3)

generate_password_button = tk.Button(text="Generate Password", command=generate_password)
add_button = tk.Button(text="Add", width=37, command=save)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
