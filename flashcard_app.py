# Created by: Alex Ubuntu
# Date: 01.01.2026
# Purpose: A personal flashcard trainer to help with learning

# Welcome message
print("Welcome to your personal flashcard trainer!")

# Fetch from user and save to variable
name = input("What is your name? ")
max_cards = 20 # Set a default value for max_cards

# Confirm name
print(f"My name is {name}")

# Card and score variables
num_cards_completed = 0
num_cards_correct = 0
score = 0

while True:
    # Start on new line for readability using '\n'
    print("\nSelect an option by entering a number")
    print("1: Set the number of cards you wish to practice")
    print("2: Start flashcards")
    print("3: Show the current score")
    print("4: Exit")
    
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        # Fetch from user and save to variable
        max_cards = int(input("\nHow many cards would you like to practice each session? "))

        # Confirm number maximum number of cards per session
        print(f"\nI want to practice at most {max_cards} cards per session")

    elif choice == "2":
        print("\nStarting flashcards...")

    elif choice == "3":
        score = (num_cards_correct/num_cards_completed) * 100

        # Display score information
        print(f"\nYou have answered {num_cards_correct} out of {num_cards_completed} correctly. Your score so far is {score}%.")

        # Display feedback message based on score
        if score > 90 and score <= 100:
            print("Excellent work!")
        elif score > 70 and score <= 90:
            print("Good job!")
        elif score > 50 and score <= 70:
            print("Keep practicing!")
        elif score > 0 and score <= 50: 
            print("Need more study time!")
        else:
            print("Score lies outside range")
    
    elif choice == "4":
        print("\nExiting...")
        break
    
    else:
        # Clarify instruction to get valid input (Bonus Task)
        print("\nInvalid value entered. Please make sure you enter just a single digit: 1, 2, 3 or 4, to select an option.")