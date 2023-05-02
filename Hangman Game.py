import random

print("Welcome to my Hangman game!")
print("-------------------------------------------")

word_dictionary = ["algorithm","bytecode","debugging","encryption","firewall","hackathon","kernel","overflow","query","runtime"]

### Choose a random word
random_word = random.choice(word_dictionary)

for x in random_word:
    print("_", end=" ")

def print_hangman(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1): 
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")

def print_word(guessed_letters):
    counter=0
    right_letters=0
    for char in random_word:
        if(char in guessed_letters):
            print(char, end=" ")
            right_letters+=1
        else:
            print("_", end=" ")
        counter+=1
    return right_letters

def print_lines():
    print("\r")
    for char in random_word:
        print("\u203E", end=" ")

def print_win_message():
  print("\nCongrats, you won!")

def print_loss_message():
    print("\nGame Over! The word was: ", random_word)

length_of_word_to_guess = len(random_word)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print()
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    ### Prompt user for input
    letter_guessed = input("\n\nGuess a letter: ")
    ### User is right
    if(letter_guessed in random_word):
        print_hangman(amount_of_times_wrong)
        ### Print word
        current_letters_guessed.append(letter_guessed)
        current_letters_right = print_word(current_letters_guessed)
        print_lines()
    ### User was wrong
    else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letter_guessed)
        ### Update the drawing
        print_hangman(amount_of_times_wrong)
        ### Print word
        current_letters_right = print_word(current_letters_guessed)
        print_lines()
if current_letters_right == length_of_word_to_guess:
  print_win_message()
if current_letters_right != length_of_word_to_guess:
  print_loss_message()
