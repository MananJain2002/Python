from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip, json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = [choice(letters) for _ in range(nr_letters)] + [choice(symbols) for _ in range(nr_symbols)] + [choice(numbers) for _ in range(nr_numbers)]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website.strip()) == 0 or len(password.strip()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", mode="w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# -------------------------- Search SETUP ----------------------------- #

def find_password():
    website = website_entry.get()

    if len(website.strip()) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left website fields empty.")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                email = data[website]["email"]
                password = data[website]["password"]
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No Data File Found.")
        except KeyError:
            messagebox.showinfo(title="Oops", message="No datails for the website exists.")
        else:
            messagebox.showinfo(title=website, message=f"email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky='e')

username_label = Label(text="Email/Username: ")
username_label.grid(row=2, column=0, sticky='e')

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky='e')

#Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(0, "yourmail@email.com")

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

#Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()
