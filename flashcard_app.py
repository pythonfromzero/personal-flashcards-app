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
print(f"I want to practice at most {max_cards} cards per session ({type(max_cards)})")
# For the real app, remove (type(max_cards)) since there's no need for this to be displayed
