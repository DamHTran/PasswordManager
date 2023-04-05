from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_passport():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    password = password_entry.get()
    username = username_entry.get()

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave the field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message="Is it okay to save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website} | {username} | {password} \n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        else:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


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
generate_password_button = Button(text="Generate Password", command=generate_passport)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
