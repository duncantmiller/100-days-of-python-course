import tkinter as tk
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    """save password file"""
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title="Sorry", message="Please don't leave any fields empty.")
    else:
        is_okay = messagebox.askokcancel(
            title=website, message=f"These are the details: \nEmail:{email}\nPassword:{password}\n"
                                    "Is it okay to save?"
        )
        if is_okay:
            with open("passwords.txt", "a") as file:
                entry = f"{website} | {email} | {password}\n"
                file.write(entry)
            clear_fields()

def populate_email_entry():
    """inserts default email"""
    email_entry.insert(0, "duncan@foomail.com")

def clear_fields():
    """clear out the field entries"""
    for entry in [website_entry, email_entry, password_entry]:
        entry.delete(0, len(entry.get()))
        populate_email_entry()

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

generate_password_button = tk.Button(text="Generate Password")
add_button = tk.Button(text="Add", width=37, command=save)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
