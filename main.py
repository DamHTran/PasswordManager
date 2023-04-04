from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #



# ---------------------------- UI SETUP ------------------------------- #

# Create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Create canvas with logo pic
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Create label and inputs box
website_label = Label(text="Website: ", bg="white")
website_label.grid(row=1, column=0)

website_entry = Entry(window, width=52)
# To put the cursor at the beginning
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Email/Username: ", bg="white")
username_label.grid(row=2, column=0)

username_entry = Entry(window, width=52)
username_entry.insert(0, "thdam3012@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)

password_entry = Entry(window, width=33)
password_entry.grid(row=3, column=1)

# Create button
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
