import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip
import json

LETTERS = list(string.ascii_letters)
NUMBERS = [str(num) for num in list(range(0, 10))]
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
LETTER_COUNT = 10
NUMBER_COUNT = 5
SYMBOL_COUNT = 5

def search():
    """search for the website in stored data and return password information"""
    try:
        message = password_information()
    except KeyError:
        message = "Website not found in vault"
    except FileNotFoundError:
        message = "Vault is empty, no websites are saved yet"
    finally:
        messagebox.showinfo(title=website(), message=message)

def password_information():
    """retrieve password information from data file"""
    with open("passwords.json", "r") as file:
        data = json.load(file)
        password_data = data[website()]
        return f"Email: {password_data['email']}\nPassword: {password_data['password']}"

def generate_random():
    """generate a random string"""
    random_password = []
    random_password += ([random.choice(LETTERS) for _ in range(LETTER_COUNT)])
    random_password += ([random.choice(NUMBERS) for _ in range(NUMBER_COUNT)])
    random_password += ([random.choice(SYMBOLS) for _ in range(SYMBOL_COUNT)])
    random.shuffle(random_password)
    return "".join(random_password)

def generate_password():
    """populate password field with random password and copy to clipboard"""
    new_password = generate_random()
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)

def website():
    """gets website entry"""
    return website_entry.get().lower()

def email():
    """gets email entry"""
    return email_entry.get()

def password():
    """gets password entry"""
    return password_entry.get()

def is_valid():
    """checks to see if all fields are filled in"""
    return len(website()) > 0 and len(email()) > 0 and len(password()) > 0

def entry_data():
    """json format of data to write to file"""
    return {
        website(): {
            "email": email(),
            "password": password()
        }
    }

def retrieve_data():
    """retrieve and update data from file if exists otherwise send entry data"""
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            data.update(entry_data())
            return data
    except FileNotFoundError:
        return entry_data()

def save_to_file():
    """saves the entry to the file"""
    data = retrieve_data()
    with open("passwords.json", "w") as file:
        json.dump(data, file, indent=4)

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

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = tk.Canvas(width=200, height=200)
image = tk.PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=image)
canvas.grid(column=1, row=0)

website_label = tk.Label(text="Website")
email_label = tk.Label(text="Email")
password_label = tk.Label(text="Password")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

website_entry = tk.Entry(width=22)
email_entry = tk.Entry(width=39)
password_entry = tk.Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry.grid(column=1, row=2, columnspan=2)
populate_email_entry()
password_entry.grid(column=1, row=3)

generate_password_button = tk.Button(text="Generate Password", command=generate_password)
add_button = tk.Button(text="Add", width=37, command=save)
search_button = tk.Button(text="Search", width=13, command=search)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)
search_button.grid(column=2, row=1)

window.mainloop()
