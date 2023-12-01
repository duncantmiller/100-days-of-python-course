import tkinter as tk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
email_entry.insert(0, "duncan@foomail.com")
password_entry.grid(column=1, row=3)

generate_password_button = tk.Button(text="Generate Password")
add_button = tk.Button(text="Add", width=37)
generate_password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
