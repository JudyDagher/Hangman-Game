import tkinter as tk
import random
 
# WORD LISTS

easy_words = ["apple", "arrow", "banana", "beach", "bear", "bird", "bottle", "candy", "carrot","chair", "cheese", "cherry", "circle", "clock", "cloud", "cookie", "dance","doctor", "dress", "eagle", "earth", "family", "fire", "flower", "garden","ghost", "guitar", "heart", "honey", "horse", "island", "jacket", "kitten","ladder", "lemon", "mirror", "monkey", "moon", "music", "ocean", "onion","orange", "panda", "paper", "pencil", "pepper", "pillow", "puppy", "rabbit","river", "salad", "school", "sheep", "smile", "spider", "spoon", "summer","table", "tiger", "tomato", "window", "winter", "zebra"]
medium_words = ["backpack", "branch", "bridge", "camera", "candle", "castle", "coffee", "copper","crown", "desert", "dolphin", "dragon", "dream", "engine", "feather", "forest","giant", "hammer", "jungle", "library", "maple", "mountain", "palace", "pocket","potato", "queen", "rainbow", "rocket", "shadow", "silver", "storm", "wizard"]
hard_words = ["island", "magic", "mirror", "music", "jacket", "dragon","dream", "mountain", "planet"]

# ASCII HANGMAN (6 stages)

hangman_stages = [
    """
     ___
    |/      
    |       
    |      
    |       
    |      
    |
    |_
    """,
    """
     ___
    |/      |
    |      
    |      
    |       
    |      
    |
    |_
    """,
    """
     ___
    |/      |
    |      (_)
    |      
    |       
    |      
    |
    |_
    """,
    """
     ___
    |/      |
    |      (_)
    |       |
    |       |
    |      
    |
    |_
    """,
    """
     ___
    |/      |
    |      (_)
    |      \|
    |       |
    |      
    |
    |_
    """,
    """
     ___
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
    |_
    """,
    """
     ___
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / 
    |
    |_
    """
]

# FUNCTIONS
def choose_word(level="easy"):
    if level == "easy":
        return random.choice(easy_words)
    elif level == "medium":
        return random.choice(medium_words)
    else:
        return random.choice(hard_words)

def check_guess(word, letter, hidden, wrong_letters):
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                hidden[i] = letter
    else:
        wrong_letters.append(letter)

# MAIN GAME + GUI
window = tk.Tk()
window.title("Hangman Game")
window.geometry("800x900")
# Colors
BG = "#FFD9EC"
TEXT = "#3D003D"
BUTTON_BG = "#FF8BB5"
BUTTON_FG = "white"

window.configure(bg=BG)

# Game variables
word = ""
hidden_word = []
wrong_letters = []
attempts_left = 6

# WIDGETS
difficulty_var = tk.StringVar(value="easy")

difficulty_label = tk.Label(window, text="Choose Difficulty:",font=("Arial", 20),bg=BG, fg=TEXT)
difficulty_label.pack(pady=10)

difficulty_menu = tk.OptionMenu(window, difficulty_var, "easy", "medium", "hard")
difficulty_menu.config(font=("Arial", 16), bg=BUTTON_BG, fg=BUTTON_FG)
difficulty_menu.pack(pady=5)

ascii_label = tk.Label(window, text=hangman_stages[0],font=("Courier", 20),bg=BG, fg=TEXT)
ascii_label.pack(pady=10)

word_label = tk.Label(window, text="",font=("Arial", 40),bg=BG, fg=TEXT)
word_label.pack(pady=10)

attempts_label = tk.Label(window, text=f"Attempts left: {attempts_left}",font=("Arial", 20),bg=BG, fg=TEXT)
attempts_label.pack()

wrong_label = tk.Label(window, text="Wrong letters: ",font=("Arial", 20),bg=BG, fg=TEXT)
wrong_label.pack(pady=5)

guess_entry = tk.Entry(window, width=5,font=("Arial", 20),bg="white", fg=TEXT)
guess_entry.pack(pady=10)

# GAME LOGIC
def start_game():
    global word, hidden_word, wrong_letters, attempts_left
    start_button.pack_forget()

    level = difficulty_var.get()
    word = choose_word(level)
    hidden_word = ["_"] * len(word)
    wrong_letters = []
    attempts_left = 6

    word_label.config(text=" ".join(hidden_word))
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    wrong_label.config(text="Wrong letters: ")
    ascii_label.config(text=hangman_stages[0])

def submit_guess():
    global attempts_left

    letter = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        return

    if letter in hidden_word or letter in wrong_letters:
        return

    check_guess(word, letter, hidden_word, wrong_letters)

    if letter not in word:
        attempts_left -= 1

    word_label.config(text=" ".join(hidden_word))
    wrong_label.config(text="Wrong letters: " + ", ".join(wrong_letters))
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    ascii_label.config(text=hangman_stages[6 - attempts_left])

    if "_" not in hidden_word:
        word_label.config(text="YOU WON!")
        ascii_label.config(text="🎉")
        start_button.pack(pady=10)

    if attempts_left == 0:
        word_label.config(text=f"You lost! Word: {word}")
        ascii_label.config(text=hangman_stages[-1])

# BUTTONS
start_button = tk.Button(window, text="Start Game",command=start_game,font=("Arial", 20),bg=BUTTON_BG, fg=BUTTON_FG)
start_button.pack(pady=10)

submit_button = tk.Button(window, text="Guess",command=submit_guess,font=("Arial", 20),bg=BUTTON_BG, fg=BUTTON_FG)
submit_button.pack(pady=10)

window.mainloop()