import random

number_list = [i for i in range(1, 101)]
random_number = random.choice(number_list)

# For debug
# random_number = 10

user_guess = 1
number_of_guesses = 0

while 1:
    # get user input
    user_guess = input("Enter guess:")
    number_of_guesses += 1
    
    # convert the user gues into int else restart loop
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("[WARNING]: Enter an integer")
        continue
    
    # check if it is in valid range
    if 1 > user_guess or user_guess > 100:
        print("[WARNING]: Your number is out of range")
        print("[WARNING]: Enter a guess between 1 and 100")
        # here we skip the rest of the while loop and go back to the top
        continue
    
    if user_guess == random_number:
        print("\nCONGRATULATIONS!!!.")
        print("You guessed corrctly.")
        print("The correct random number is:", user_guess)
        print("You took ", number_of_guesses, " guesses")
        break
    elif user_guess < random_number:
        print("[Hint]: Your guess is lower")
        continue
    else:
        print("[Hint]: Your guess is higher")
        continue

