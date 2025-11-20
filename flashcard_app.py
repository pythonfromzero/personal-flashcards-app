# Created by: Alex Ubuntu
# Date: 01.01.2026
# Purpose: A personal flashcard trainer to help with learning

# Import the random module
import random

# Welcome message
print("Welcome to your personal flashcard trainer!")

# Fetch from user and save to variable
name = input("What is your name? ")
max_cards = 20 # Set a default value for max_cards

# Confirm name
print(f"\nMy name is {name}")

# Card and score variables
num_cards_completed = 0
num_cards_correct = 0
score = 0

# Set absolute maximum number of cards so that the user can't ask for too many
ABSOLUTE_MAX_CARDS = 100

# Flashcards list
flashcards = {'dog': 'Mammalia', 'cat': 'Mammalia', 'pig': 'Mammalia', 'parrot': 'Aves', 'cow': 'Mammalia'}

# Function to calculate and display score information
def display_score_info():
    score = (num_cards_correct/num_cards_completed) * 100
    print(f"\nYou have answered {num_cards_correct} out of {num_cards_completed} correctly. Your score is {score}%.")

while True:
    print("\nSelect an option by entering a number")
    print("1: Set the number of cards you wish to practice")
    print("2: Start flashcards")
    print("3: Show the current score")
    print("4: Exit")
    
    
    choice = input("\nChoose an option: ")
    
    if choice == "1":

        while True:
            # More stringent validation for input for maximum number of cards
            
            # Fetch input from user but don't attempt to convert the input string 
            # to int until certain it will work 
            entered_max_cards = input("\nHow many cards would you like to practice each session? ")

            # Check if input string represents an integer
            if entered_max_cards.isdigit():

                # Convert to integer data type
                entered_max_cards = int(entered_max_cards)
            
                # Check if value is within the value range 
                # (between 1 and the absolute maximum number of cards)
                if entered_max_cards > 0 and entered_max_cards < ABSOLUTE_MAX_CARDS:
                    
                    # Set the max_cards variable with the user's preference
                    max_cards = entered_max_cards
                    # Confirm number maximum number of cards per session
                    print(f"\nI want to practice at most {max_cards} cards per session")
                    break
                else:
                    ## Let the user know what the range should be (Bonus task).
                    print(f"\nPlease enter a valid number bewteen 1 and {ABSOLUTE_MAX_CARDS}.")    
            else:
                print(f"\nPlease enter a whole number number over 0.")

            

    elif choice == "2":
        

        # Create a list from the flashcards dictionary items
        flashcards_list = list(flashcards.items())
        # Shuffle the list
        random.shuffle(flashcards_list)
        # Using a for loop means that the number of flashcards displayed
        # is limited by the number of items in flashcards so the user
        # may end up practicing fewer cards than they specified  
        for q, a in flashcards_list:
            # Ask user question and save response into variable
            user_answer = input(f"\nWhat class are {q}s in? ")
            
            # Increment the count of cards completed
            num_cards_completed += 1
            # Display user's answer and correct answer
            print(f"Your answer: {user_answer}, Correct answer: {a}")
            
            # Response deemed to be correct even if given in different case
            if user_answer.lower() == a.lower():
                
                # Increment count of cards answered correctly
                num_cards_correct += 1
                print("Correct")
            else:
                print("Incorrect")
            
            # Check if number of cards completed has hit the user's
            # preferred maximum number of cards
            if num_cards_completed >= max_cards:
                print("\nWell done on completing your practice session!")
                display_score_info()
                break
        
        print("\nWell done on completing your practice session!")
        display_score_info()
    elif choice == "3":

        # Handle case where no cards have been completed yet.
        if num_cards_completed <=0:
            print("You need to practice before you can get a score.")
            continue
        

        display_score_info()

    
    elif choice == "4":
        print(f"We hope you enjoyed your practice session today, {name}.")
        
        display_score_info()

        # Display feedback message based on score
        if score > 90 and score <= 100:
            print("Excellent work!")
        elif score > 70 and score <= 90:
            print("Good job!")
        elif score > 50 and score <= 70:
            print("Keep practicing!")
        elif score > 0 and score <= 50: 
            print("Need more study time!")
        
        print("Look forward to seeing you again soon!")
        break
    
    else:
        # Clarify instruction to get valid input
        print("\nInvalid value entered. Please make sure you enter just a single digit (no other words): 1, 2, 3 or 4, to select an option.")