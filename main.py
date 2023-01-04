from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_time
    window.after_cancel(flip_time)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_bg, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_time = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back)


window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_time = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_right = PhotoImage(file="images/right.png")
card_wrong = PhotoImage(file="images/wrong.png")
card_bg = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

button_right = Button(image=card_right, bg=BACKGROUND_COLOR, highlightthickness=0, border=0, command=next_card)
button_right.grid(column=1, row=1)
button_wrong = Button(image=card_wrong, bg=BACKGROUND_COLOR, highlightthickness=0, border=0, command=next_card)
button_wrong.grid(column=0, row=1)


next_card()


window.mainloop()