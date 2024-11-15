from flask import Flask, request, jsonify, render_template
import random
import os

app = Flask(__name__)

# Initialize main variables
random_number = random.randint(1, 100)
number_of_guesses = 0
high_scores = []

# Load high scores from file if it exists
def load_high_scores():
    global high_scores
    if os.path.exists("high_scores.txt"):
        with open("high_scores.txt", "r") as file:
            for line in file:
                name, score = line.strip().split(",")
                high_scores.append((name, int(score)))
        high_scores.sort(key=lambda x: x[1])  # Sort by score (number of guesses)
        high_scores[:] = high_scores[:3]  # Keep only the top 3 scores

# Save high scores to file
def save_high_scores():
    with open("high_scores.txt", "w") as file:
        for name, score in high_scores:
            file.write(f"{name},{score}\n")

# Route to serve the main game page
@app.route('/')
def index():
    return render_template("guess_the_number.html")

# Route to start a new game
@app.route('/reset', methods=['POST'])
def reset_game():
    global random_number, number_of_guesses
    random_number = random.randint(1, 100)
    number_of_guesses = 0
    return jsonify(success=True)

# Route to handle guess submissions
@app.route('/guess', methods=['POST'])
def submit_guess():
    global number_of_guesses, random_number

    data = request.json
    user_guess = int(data.get("guess"))
    number_of_guesses += 1
    response = {}

    if user_guess == random_number:
        response['message'] = f"CONGRATULATIONS!!! You guessed correctly in {number_of_guesses} attempts."
        response['correct'] = True
        if len(high_scores) < 5 or number_of_guesses < high_scores[-1][1]:
            response['high_score'] = True
        else:
            response['high_score'] = False
    elif user_guess < random_number:
        response['message'] = "[Hint]: Your guess is too low."
        response['correct'] = False
    else:
        response['message'] = "[Hint]: Your guess is too high."
        response['correct'] = False

    return jsonify(response)

# Route to submit player's name for high score
@app.route('/submit_name', methods=['POST'])
def submit_name():
    global number_of_guesses

    data = request.json
    player_name = data.get("name")

    if len(player_name) == 3:
        high_scores.append((player_name, number_of_guesses))
        high_scores.sort(key=lambda x: x[1])  # Sort by number of guesses
        high_scores[:] = high_scores[:5]  # Keep only the top 3
        save_high_scores()  # Save the updated high scores

    return jsonify(success=True)

# Route to retrieve high scores
@app.route('/high_scores', methods=['GET'])
def get_high_scores():
    return jsonify(high_scores=high_scores)

# Initialize high scores on server start
load_high_scores()

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Use port 5001 or any other available port
