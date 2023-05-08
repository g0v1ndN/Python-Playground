# Import required modules
import random
import string

# Define function to generate password
def generate_password(min_length, numbers=True, special_characters=True):
    # Define character sets to be used for generating password
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # Determine which character sets to use based on user input
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Initialize variables for password generation and criteria checking
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    # Loop until password meets criteria and is long enough
    while not meets_criteria or len(pwd) < min_length:
        # Generate a new random character and add it to the password
        new_char = random.choice(characters)
        pwd += new_char

        # Check if the new character is a number or special character
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        # Determine if the password meets the specified criteria
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    # Return the generated password
    return pwd

# Get user input for password criteria
min_length = int(input("Specify the minimum length required for the password. "))
has_number = input("Do you want the password to include numbers? (y/n)").lower() == "y"
has_special = input("Do you want the password to include special characters? (y/n)").lower() == "y"

# Generate and print the password
pwd = generate_password(min_length, has_number, has_special)
print ("Here is the password generated: ", pwd)
