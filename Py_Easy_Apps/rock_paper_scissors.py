import random

rps = ["rock", "paper", "scissors"]

# global user_score
# global comp_score

user_score, comp_score = 0, 0

"""
Here we process the input
"""
def user_input_func() -> str:
    user_input = input("rock! paper!! scissors!!!:  ")
    user_input = user_input.strip()
    user_input = user_input.lower()
    
    if user_input not in rps:
        print("Type either rock, paper or scissors")
        print("you might have made a spelling mistake")
        return ""
    
    return user_input

"""
Here we evaluate who won the round
"""
def evaluate_winner(user_input: str, 
                    comp_choice: str, 
                    user_score: int,
                    comp_score: int) -> str:
    print("\nYou played: ", user_input)
    print("Computer played: ", comp_choice)
    
    if user_input == comp_choice or user_input == "":
        return ["Game continues", 0, 0]
    
    elif user_input == "rock" and comp_choice == "scissors":
        user_score += 1
        return ["You win the round :)!!! ", 1, 0]
    
    elif user_input == "scissors" and comp_choice == "paper":
        user_score += 1
        return ["You win the round :)!!! ", 1, 0]
    
    elif user_input == "paper" and comp_choice == "rock":
        user_score += 1
        return ["You win the round :)!!! ", 1, 0]
    
    elif comp_choice == "rock" and user_input == "scissors":
        comp_score += 1
        return ["You lose the round :(", 0, 1]
    
    elif comp_choice == "scissors" and user_input == "paper":
        comp_score += 1
        return ["You lose the round :(", 0, 1]
    
    elif comp_choice == "paper" and user_input == "rock":
        comp_score += 1
        return ["You lose the round :(", 0, 1]
    
    else: return ["Something went wrong", 0, 0]

"""
here we check who won over all
"""
def game_decider(user_score: int, comp_score: int) -> str:
    
    if user_score > comp_score:
        return "\nYou win from best of 3!!!!"
    elif user_score < comp_score:
        return "\nYou lose from best of 3!!!"
    else:
        return "\nIt's a tie *-*"
    
    
game_on = 0


while game_on < 3:
    
    
    if game_on == 0:
        print("Best of three")
    
    comp_choice = random.choice(rps)
    user_input = user_input_func()
    
    evaluator = evaluate_winner(user_input, 
                                comp_choice,
                                user_score,
                                comp_score)
    
    if evaluator[0] == "Game continues" or evaluator[0] == "Something went wrong":
        continue
    else:
        print(evaluator[0])
        game_on += 1
        
    if game_on == 3:
        game_outcome = game_decider(evaluator[1], evaluator[2])
        print(game_outcome)
    
