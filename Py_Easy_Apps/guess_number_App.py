import tkinter as tk
import random
import os

# Initialize main variables
random_number = random.randint(1, 100)
number_of_guesses = 0
high_scores = []

# Load high scores from file if it exists
def load_high_scores():
    global high_scores
    if os.path.exists("./high_scores.txt"):
        with open("high_scores.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                high_scores.append((name, int(score)))
        high_scores.sort(key = lambda x:x[1])  # Sort by score (number of guesses)
        high_scores = high_scores[:5]  # Keep only the top 3 scores

# Save high scores to file
def save_high_scores():
    with open("high_scores.txt", "w") as file:
        for name, score in high_scores:
            file.write(f"{name},{score}\n")

# Function to reset the game
def reset_game():
    global random_number, number_of_guesses
    random_number = random.randint(1, 100)
    number_of_guesses = 0
    message_label.config(text="Enter your guess (1-100):")
    entry.delete(0, tk.END)
    entry.pack(pady=10)
    submit_button.pack(pady=10)
    play_again_button.pack_forget()  # Hide the play again button
    name_entry.pack_forget()         # Hide name entry if shown before
    save_high_scores()               # Save scores before restarting

# Function to handle user's guess
def submit_guess(event=None):
    global number_of_guesses
    user_guess = entry.get()
    number_of_guesses += 1

    # Try to convert user input to an integer
    try:
        user_guess = int(user_guess)
    except ValueError:
        message_label.config(text="[WARNING]: Enter an integer.")
        return

    # Check if the guess is within range
    if user_guess < 1 or user_guess > 100:
        message_label.config(text="[WARNING]: Enter a guess between 1 and 100.")
        return

    # Check if the guess is correct, too low, or too high
    if user_guess == random_number:
        # Display win message
        message_label.config(text=f"CONGRATULATIONS!!!\nYou guessed correctly in {number_of_guesses} attempts.")
        entry.pack_forget()
        submit_button.pack_forget()
        
        # Check if current score qualifies as a high score
        if len(high_scores) < 3 or number_of_guesses < high_scores[-1][1]:
            message_label.config(text="New High Score.\n Enter Player name in 3 characters.")
            name_entry.pack(pady=10)  # Show name entry field if it's a high score
            play_again_button.pack(pady=10)
        else:
            display_high_scores()
            play_again_button.pack(pady=10)
    elif user_guess < random_number:
        message_label.config(text="[Hint]: Your guess is too low.")
    else:
        message_label.config(text="[Hint]: Your guess is too high.")
    
    entry.delete(0, tk.END)  # Clear the entry field after each guess

# Display high scores
def display_high_scores():
    high_scores_text = "High Scores:\n"
    for i, (name, score) in enumerate(high_scores, start=1):
        high_scores_text += f"{i}. {name}: {score} guesses\n"
    message_label.config(text=high_scores_text)

# Function to submit the player's name for high score
def submit_name():
    global number_of_guesses
    
    player_name = name_entry.get()
    if len(player_name) == 3:
        high_scores.append((player_name, number_of_guesses))
        high_scores.sort(key=lambda x: x[1])  # Sort by number of guesses
        high_scores[:] = high_scores[:3]  # Keep only the top 3
        display_high_scores()
        name_entry.delete(0, tk.END)  # Clear the name entry field
        name_entry.pack_forget()  # Hide the name entry field
        save_high_scores()  # Save the updated high scores

# Set up the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("600x400")

# Define font settings
font_settings = ("Arial", 20)

# Load high scores at the start
load_high_scores()

# Add a label to display messages
message_label = tk.Label(root, text="Enter your guess (1-100):", font=font_settings)
message_label.pack(pady=10)

# Entry field for user input
entry = tk.Entry(root, font=font_settings)
entry.pack(pady=10)
entry.bind("<Return>", submit_guess)

# Submit button for guesses
submit_button = tk.Button(root, text="Submit", command=submit_guess, font=font_settings)
submit_button.pack(pady=10)

# Play again button (hidden initially)
play_again_button = tk.Button(root, text="Play Again", command=reset_game, font=font_settings)

# Name entry for high score (hidden initially)
name_entry = tk.Entry(root, font=font_settings)
name_entry.bind("<Return>", lambda event: submit_name())  # Submit name on Enter key

root.mainloop()
