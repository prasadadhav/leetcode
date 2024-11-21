import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

rps = ["rock", "paper", "scissors"]
user_score, comp_score = 0, 0
game_on = 0

def evaluate_winner(user_input, comp_choice):
    global user_score, comp_score, game_on
    
    if user_input == comp_choice:
        result_label.config(text="It's a tie!")
    elif (user_input == "rock" and comp_choice == "scissors") or \
         (user_input == "scissors" and comp_choice == "paper") or \
         (user_input == "paper" and comp_choice == "rock"):
        user_score += 1
        result_label.config(text="You win this round!")
    else:
        comp_score += 1
        result_label.config(text="You lose this round!")

    game_on += 1

    if game_on == 3:
        display_winner()

def display_winner():
    global user_score, comp_score, game_on
    if user_score > comp_score:
        winner_text = "You win the game!"
    elif user_score < comp_score:
        winner_text = "You lose the game!"
    else:
        winner_text = "It's a tie!"

    result_label.config(text=winner_text)
    replay_button.pack(pady=20)

def replay():
    global user_score, comp_score, game_on
    user_score, comp_score, game_on = 0, 0, 0
    result_label.config(text="")
    comp_image_label.config(image="")
    replay_button.pack_forget()

# Example of where you update the round label
game_on = 0  # Track rounds

def play_game(user_choice):
    comp_choice = random.choice(rps)
    
    global game_on
    if game_on >= 3:
        return

    # Show computer's choice in grayscale
    comp_image_path = f"./Py_Easy_Apps/assets/{comp_choice}.jpg"
    comp_image = Image.open(comp_image_path).convert("L")
    comp_image = Image.open(comp_image_path).resize((150, 150), Image.Resampling.LANCZOS)
    comp_photo = ImageTk.PhotoImage(comp_image)
    comp_image_label.config(image=comp_photo)
    comp_image_label.image = comp_photo

    # Evaluate round winner
    evaluate_winner(user_choice, comp_choice)
    
    update_round_label(game_on)
    if game_on == 3:
        messagebox.showinfo("Game Over", "Best of 3 is done!")

# Setup Tkinter window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("600x800")
root.resizable(False, False)

# Display round label at the bottom
round_label = tk.Label(root, text="Round: 1", font=("Helvetica", 20))
round_label.pack(side=tk.BOTTOM, pady=10)

# Function to update the round label
def update_round_label(round_number):
    round_label.config(text=f"Round: {round_number}")

# Header
header_label = tk.Label(root, text="Rock, Paper, Scissors - Best of 3", font=("Helvetica", 20))
header_label.pack(pady=20)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=50)

for choice in rps:
    image_path = f"./Py_Easy_Apps/assets/{choice}.jpg"
    image = Image.open(image_path).resize((150, 150), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    button = tk.Button(button_frame, image=photo, command=lambda c=choice: play_game(c))
    button.image = photo
    button.pack(side=tk.LEFT, padx=20)

# Computer choice display
comp_label = tk.Label(root, text="Computer chose:", font=("Helvetica", 16))
comp_label.pack(pady=20)
comp_image_label = tk.Label(root)
comp_image_label.pack()


# Result display
result_label = tk.Label(root, text="", font=("Helvetica", 20))
result_label.pack(pady=20)

# Replay button
replay_button = tk.Button(root, text="Replay", font=("Helvetica", 16), command=replay)

# Run the application
root.mainloop()
