from tkinter import *
from tkinter import messagebox
import pyperclip
from modules.database import Database
from modules.password_generator import PasswordGenerator

# ---------------------------- CONSTANTS ------------------------------- #

LOGO_IMAGE_PATH = "_internal/art/logo.png"

FONT_NAME = "Rockwell"
LABEL_FONT = (FONT_NAME, 13, "bold")

BLACK = "#252A34"
TEAL = "#08D9D6"
GREY = "#EAEAEA"

PAD_X = 5
PAD_Y = 3

# ---------------------------- VARIABLES ------------------------------- #

program_running = True
add_confirmation = False
overwrite_confirmation = False

# ---------------------------- OBJECTS ------------------------------- #

database = Database()
password_generator = PasswordGenerator()

# ---------------------------- FUNCTIONS ------------------------------- #


def save_data_to_database():
    global add_confirmation, overwrite_confirmation

    # save text from entry's to variables
    website_text = website_entry.get().lower()
    email_text = email_entry.get().lower()
    password_text = password_entry.get()

    # if a field is left empty, show the user a message box to let him know to not leave fields empty
    if len(website_text) < 1 or len(email_text) < 1 or len(password_text) < 1:
        messagebox.showerror(title="You left empty fields!", message="Please don't leave any fields empty!")
        return

    if database.is_password_in_database(website_text, email_text):
        # get the old password from the database
        old_password = database.get_password()
        # ask the user if he wants to overwrite the existing password
        overwrite_confirmation = messagebox.askokcancel(title="Data already in database!",
                                                        message=f"There is already an existing password linked with "
                                                                f"this account: "
                                                                f"\nEmail: {email_text}"
                                                                f"\nOld password: {old_password}"
                                                                f"\nDo you want to change the password?")
    else:
        # ask the user if he is sure he wants to save the details. If yes, then this variable turns True
        add_confirmation = messagebox.askokcancel(title="Are you sure?", message=f"These are the details entered: "
                                                                                 f"\nEmail: {email_text}"
                                                                                 f"\nPassword: {password_text}"
                                                                                 f"\nDo you want to save this data?")
    if add_confirmation or overwrite_confirmation:
        if overwrite_confirmation:
            # if an account exists in the database, just overwrite the password
            database.add_new_data(website_text, email_text, password_text, overwrite_data=True)
        else:
            # if not, append it to the data list
            database.add_new_data(website_text, email_text, password_text)

        # clear the text in the inputs
        website_entry.delete(0, END)
        password_entry.delete(0, END)

        # show a message box to the user informing him that his details have been saved
        messagebox.showinfo(title="Saving complete!", message="Your password has been saved!")


def check_for_password():
    # save text from entry's to variables
    website_text = website_entry.get().lower()
    email_text = email_entry.get().lower()

    # if there is a password linked to the provided details, insert the password in the password field
    if database.is_password_in_database(website_text, email_text):
        password = database.get_password()

        # copy the generated password to the clipboard
        pyperclip.copy(password)

        # delete the existing text in the password field
        password_entry.delete(0, END)
        # insert the password
        password_entry.insert(0, password)

        # show a message box informing the user that the data is in the database
        messagebox.showinfo(title="Password found!", message="There is a password linked to this data!"
                                                             "\nPassword copied to the clipboard!")

    # if not, tell the user that there is no such password in the database
    else:
        # delete the existing text in the password field
        password_entry.delete(0, END)

        messagebox.showinfo(title="No password in database!", message="There is no password linked to this account in "
                                                                      "the database")


def generate_password():
    # get the desired length of the password from the password entry
    password_length = int(password_length_entry.get())

    # generate a random password and save it to the password variable
    password = password_generator.generate_password(password_length)

    # copy the generated password to the clipboard
    pyperclip.copy(password)

    # clear the password entry and then insert the newly generated password in there
    password_entry.delete(0, END)
    password_entry.insert(0, password)


def clear_email_entry():
    email_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

# window setup
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BLACK)

# canvas setup
lock_img = PhotoImage(file=LOGO_IMAGE_PATH)

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=BLACK)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# labels setup
website_label = Label(text="Website:", font=LABEL_FONT, bg=BLACK, fg=GREY)
website_label.grid(column=0, row=1, sticky="E")

email_label = Label(text="Email/Username:", font=LABEL_FONT, bg=BLACK, fg=GREY)
email_label.grid(column=0, row=2, sticky="E")

password_label = Label(text="Password:", font=LABEL_FONT, bg=BLACK, fg=GREY)
password_label.grid(column=0, row=3, sticky="E")

# inputs setup
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="W", padx=PAD_X, pady=PAD_Y)

email_entry = Entry(width=32)
email_entry.insert(0, "xxjakubszewczykxx@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="W", padx=PAD_X, pady=PAD_Y)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, sticky="W", padx=PAD_X, pady=PAD_Y)

password_length_entry = Entry(width=2, font=(FONT_NAME, 17, "bold"))
password_length_entry.insert(0, "15")
password_length_entry.grid(column=3, row=3, sticky="W", padx=PAD_X, pady=PAD_Y)

# buttons setup
search_button = Button(text="Search", width=12, bg=TEAL, fg=GREY, font=LABEL_FONT, command=check_for_password)
search_button.grid(column=2, row=1, columnspan=2, sticky="W", padx=PAD_X, pady=PAD_Y)

clear_button = Button(text="Clear", width=12, bg=TEAL, fg=GREY, font=LABEL_FONT, command=clear_email_entry)
clear_button.grid(column=2, row=2, columnspan=2, sticky="W", padx=PAD_X, pady=PAD_Y)

generate_button = Button(text="Generate", width=8, bg=TEAL, fg=GREY, font=LABEL_FONT, command=generate_password)
generate_button.grid(column=2, row=3, sticky="W", padx=PAD_X, pady=PAD_Y)

add_button = Button(text="Add", width=31, bg=TEAL, fg=GREY, font=LABEL_FONT, command=save_data_to_database)
add_button.grid(column=1, row=4, columnspan=3, sticky="E", padx=PAD_X, pady=PAD_Y)

window.mainloop()
