# Created by: Alex Ubuntu
# Date: 01.01.2026
# Purpose: A personal flashcard trainer to help with learning

# Welcome message
print("Welcome to your personal flashcard trainer!")

# Fetch from user and save to variable
name = input("What is your name? ")

# Confirm name
print(f"My name is {name}")

# Fetch from user and save to variable
max_cards = int(input("How many cards would you like to practice each session? "))

# Confirm number maximum number of cards per session
print(f"I want to practice at most {max_cards} cards per session")

# Card and score variables
num_cards_completed = 10
num_cards_correct = 5
score = (num_cards_correct/num_cards_completed) * 100

# Display score information
print(f"You have answered {num_cards_correct} out of {num_cards_completed} correctly. Your score so far is {score}%.")

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
