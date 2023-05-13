import random

def play_game():
    """
    Plays a game of number guessing with the user.
    """
    # Print some introductory messages.
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 tries to guess the number.")
    
    # Generate a random secret number between 1 and 100.
    secret_number = random.randint(1, 100)
    
    # Create an empty list to store the user's guesses.
    guesses = []
    
    # Loop 10 times (maximum), prompting the user for a guess each time.
    while len(guesses) < 10:
        guess = input("Guess a number: ")
        
        # Validate that the input is a number.
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        # Check if the user has already guessed this number.
        if guess in guesses:
            print("You already guessed that number! Try again.")
            continue
        
        # Add the user's guess to the list of guesses.
        guesses.append(guess)
        
        # Check if the user has guessed the secret number.
        if guess == secret_number:
            print("Congratulations, you guessed the number!")
            print(f"It took you {len(guesses)} tries.")
            return  # Exit the function.
        elif guess < secret_number:
            print("Too low! Guess again.")
        else:
            print("Too high! Guess again.")
    
    # If the user has used up all 10 guesses, reveal the secret number.
    print("Sorry, you ran out of guesses!")
    print(f"The secret number was {secret_number}.")

# Call the play_game function to start the game.
play_game()
