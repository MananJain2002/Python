from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}  # Stores the current flashcard being displayed
to_learn = {}  # Stores the flashcards to be learned

try:
    data = pd.read_csv("./data/words_to_learn.csv")  # Try to read the flashcards from a file
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")  # If the file is not found, read the original flashcards
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # If the file is found, read the flashcards from the file

def is_known():
    to_learn.remove(current_card)  # Remove the current flashcard from the list of flashcards to be learned

    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)  # Save the updated list of flashcards to a file

    next_card()  # Display the next flashcard

def flip_card():
    global current_card
    canvas.itemconfig(card_background, image=card_back_img)  # Change the background image to the back of the flashcard
    canvas.itemconfig(card_title, text="English", fill="white")  # Change the title text to "English"
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")  # Display the English word

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous flip timer

    current_card = choice(to_learn)  # Select a random flashcard from the list of flashcards to be learned
    canvas.itemconfig(card_background, image=card_front_img)  # Change the background image to the front of the flashcard
    canvas.itemconfig(card_title, text="French", fill="black")  # Change the title text to "French"
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")  # Display the French word
    
    flip_timer = window.after(3000, flip_card)  # Start a new flip timer to automatically flip the flashcard after 3 seconds

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)  # Start the initial flip timer to automatically flip the flashcard after 3 seconds

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)  # Create the background image of the flashcard
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  # Create the title text of the flashcard
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))  # Create the word text of the flashcard
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, bd=0, command=next_card)  # Create the "unknown" button
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, bd=0, command=is_known)  # Create the "known" button
known_button.grid(row=1, column=1)

next_card()  # Display the first flashcard

window.mainloop()  # Start the main event loop
