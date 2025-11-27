# Created by: Alex Ubuntu
# Date: 01.01.2026
# Purpose: A personal flashcard trainer to help with learning

# Import the random module
import random
# Import json module
import json

# JSON structure for user data for multiple users:
#{
#    "user1": {
#        "max_cards": 10, 
#        "name": "User 1",
#        "progress_history": [
#        {
#            "num_cards_practiced": 10,
#            "score": 0.8,
#        },
#        {
#            "num_cards_practiced": 10,
#            "score": 0.6,
#        },
#        {
#            "num_cards_practiced": 10,
#            "score": 0.5,
#        }]
#    },
#    "user2": {
#        "name": "User 2",
#        "max_cards": 30, 
#        "progress_history": [
#        {
#            "num_cards_practiced": 30,
#            "score": 0.8,
#        }]
#    },
#    "user3": {
#        "name": "User 3",
#        "max_cards": 16, 
#        "progress_history": [
#        {
#            "num_cards_practiced": 16,
#            "score": 0.5,
#        },
#        {
#            "num_cards_practiced": 16,
#            "score": 1.0,
#        }]
#    }
#}
user_filename = "users.json"

# Variable to limit the number of times the user
# can enter their username incorrectly before they
# are forced to create a new one.
MAX_USERNAME_ATTEMPTS = 3

# Welcome message
print("Welcome to your personal flashcard trainer!")

# Initialise username to None since we need to set it explicitly
# when the program starts
username = None
name = ""
# Absolute maximum number of cards so that the user can't ask for too many
ABSOLUTE_MAX_CARDS = 100
DEFAULT_MAX_CARDS = 20 # Set a default value for max_cards


# Check if it is the user's first time
print("Is it your first time using this app?")
# Input validation - ask question until answered correctly
while True:

    first_time = input("0: No \n1: Yes\n")
    # 0: It is not the user's first time, so they should have a username
    # 1: It is the user's first time, so they don't have a username yet

    if first_time!="0" and first_time!="1":
        # Any input other than 0 or 1 is not valid so we need to prompt the user again
        # with a clarifying message
        print(f"Please enter either 0, if you have never used the app before or 1, if you have.")
    else:
        # Irrespective of whether the user has used the app before, 
        # try to open the user_data file and load the data in it,
        # otherwise initialise with empty dictionary
        all_user_data = {}
        try: 
            with open(user_filename, 'r') as file:
                all_user_data = json.load(file)

            # Attempt to find name and max_cards in file or ask from user
            num_attempts = 0
            
            if first_time=="0":
                while num_attempts < MAX_USERNAME_ATTEMPTS:
                    username = input("Enter your username: ")
                    # If it's not the user's first time, we need to get their data
                    user_data = all_user_data.get(username)
                    
                    if isinstance(user_data, dict):
                        # If we find the data corresponding to the username, we can set the name
                        # and max_cards variables from the saved values or by asking the user
                        name = user_data.get("name") # Value stored in dictionary
                        if not name:
                            # If name not found, ask user for it
                            name = input("What is your name? ")
                            user_data["name"] = name
                        # If max_cards not found, set to default value - the existing 
                        # value of max_cards
                        max_cards = user_data.get("max_cards", DEFAULT_MAX_CARDS) # Value stored in dictionary
                    
                        # Save the user_data back to the master dictionary all_user_data
                        all_user_data[username] = user_data
                        # Save these values to file
                        with open(user_filename, 'w') as file:
                            json.dump(all_user_data, file, indent=4)
                        # Leave the loop
                        break
                    else:
                        print("We can't find you in our database, are you sure you've spelt it correctly?\n")
                        num_attempts += 1
                

            ## If either it is the user's first time or the maximum number of attempts has been 
            # reached, the user needs to create a new username
            if first_time=="1" or num_attempts >= MAX_USERNAME_ATTEMPTS:
                
                while True:
                    # Keep asking the user for a username until they 
                    # choose one that doesn't exist in all_user_data
                    username = input("Create a username: ")
                    # Check if the username is one of the keys in all_user_data
                    if username in all_user_data:
                        # If it already exists, prompt the user to create a different one
                        print("This username already exists, please create a different one")
                    else:
                        user_data = {}
                        name = input("What is your name? ")
                        user_data["name"] = name
                        # Since we already have default value for max_cards, don't ask
                        # user (they can always change it later by choosing Option 1 below)
                        user_data["max_cards"] = DEFAULT_MAX_CARDS

                        # Save this user_data to the master dictionary all_user_data with
                        # the username as the key
                        all_user_data[username] = user_data
                        with open(user_filename, 'w') as file:
                            json.dump(all_user_data, file, indent=4)
                        # Break out of loop
                        break
            # Break out of outer loop
            break                  
        except FileNotFoundError:
            # Since the file is not there, there is no existing user_data 
            # so we have to start with empty dictionary and ask for the username
            user_data = {}
            username = input("Create a username: ")
            name = input("What is your name? ")
            user_data["name"] = name
            # Since we already have default value for max_cards, don't ask
            # user (they can always change it later by choosing Option 1 below)
            user_data["max_cards"] = DEFAULT_MAX_CARDS

            # Save this user_data to the master dictionary all_user_data with
            # the username as the key
            all_user_data[username] = user_data
            with open(user_filename, 'w') as file:
                json.dump(all_user_data, file, indent=4)
            # Break out of loop
            break
    
# Function to get max_cards from file
def get_max_cards():
    all_user_data = {}
    user_data = {}
    # Initialise user_data with saved file data if available
    try: 
        with open(user_filename, 'r') as file:
            all_user_data = json.load(file)
            user_data = all_user_data[username]
            max_cards = user_data.get("max_cards", DEFAULT_MAX_CARDS)
            return max_cards
    except FileNotFoundError:
        # If no value found in file, return the default value
        return DEFAULT_MAX_CARDS
    
# Function for user to set and save a max_cards value to json
def set_max_cards():
    all_user_data = {}
    user_data = {}
    # Initialise user_data with saved file data if available
    try: 
        with open(user_filename, 'r') as file:
            all_user_data = json.load(file)
            user_data = all_user_data[username]
            
    except FileNotFoundError:
        pass

    while True:
        # Validation for input for maximum number of cards

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
                    
                # Confirm number maximum number of cards per session
                print(f"\nYou want to practice at most {entered_max_cards} cards per session")
                # Set the user_data dictionary "max_cards" field to the user entered value
                user_data["max_cards"] = entered_max_cards

                # Update all_user_data dictionary to include this new setting
                all_user_data[username] = user_data

                # Save all_user_data dictionary with the new value to json
                with open(user_filename, 'w') as file:
                    json.dump(all_user_data, file, indent=4)
                break
            else:
                ## Let the user know what the range should be
                print(f"\nPlease enter a valid number between 1 and {ABSOLUTE_MAX_CARDS}.")    
        else:
            print(f"\nPlease enter a whole number number over 0.") 


# Confirm name
print(f"\nYour name is {name}")

# Card and score variables
num_cards_completed = 0
num_cards_correct = 0
score = 0


# Set flashcards dictionary from file
# Initialize empty dictionary
flashcards = {}
file_separator = ','

# Open and read the file
flashcard_file = "flashcards.txt"
try:
    with open(flashcard_file, 'r') as file:
        lines = file.readlines()
except:
    # Handle scenario where file is not found 
    # and display comprehensible message to user.
    print(f"The file {flashcard_file} is missing. Please add it to initialise your flashcards.")
    exit()

# Process each line
# Each line has: question,answer
for line in lines:
    # Remove whitespace/newlines
    line = line.strip()
    
    # Split by ',' separator
    parts = line.split(file_separator)
    
    # Extract question and answer
    question = parts[0]
    answer = parts[1]
    
    # Add to dictionary
    flashcards[question] = answer

# Confirm loaded
print(f"{len(flashcards)} flashcards loaded!")


# Function to calculate and display score information
def display_score_info():

    # Handle case where no cards have been completed yet.
    if num_cards_completed <=0:
        print("You need to practice before you can get a score.")
    else:
        # Calculate score
        score = (num_cards_correct/num_cards_completed) * 100
        print(f"\nYou have answered {num_cards_correct} out of {num_cards_completed} correctly. Your score is {score}%.")

# Function to write score information to file
def write_score_info():
    # Calculate score
    score = (num_cards_correct/num_cards_completed) * 100
    data_to_append = {
        "num_cards_practiced": num_cards_completed,
        "score": score,
    }
    # TODO: Include date/time stamp?
    # Initialise all_user_data as empty dictionary
    all_user_data = {}
    # Initialise user_data as empty dictionary
    user_data = {}
    # Initialise score_data as empty dictionary
    score_data = []
    # Try opening the json file
    # Use user_file variable from above
    try:
        with open(user_filename, 'r') as file:
            # Load file contents if found
            all_user_data = json.load(file)
            user_data = all_user_data[username]
            # Use safe extraction to get the progress_history 
            # containing the list of score data for different sessions. 
            # If it isn't there, set to empty list.
            score_data = user_data.get("progress_history", [])
    except FileNotFoundError:
        # Otherwise do nothing so score_data remains an empty list
        pass

    # Append latest session data
    score_data.append(data_to_append)

    # Write out score_data with the latest session data appended
    # to json file
    with open(user_filename, 'w') as file:
        # Save the score data in the progress_history element
        user_data["progress_history"] = score_data
        # Save the user_data to the user's data in user_data
        all_user_data[username] = user_data
        json.dump(all_user_data, file, indent=4)

# Fetches progress history from json file
# Empty list returned if history or file not found
def get_progress_history():
    score_data = []
    # Open and read the file
    try:
        with open(user_filename, 'r') as file:
            # Load file contents if found
            all_user_data = json.load(file)
            user_data = all_user_data[username]
            # Use safe extraction to get the progress_history 
            # containing the list of score data for different sessions. 
            # If it isn't there, set to empty list.
            return user_data.get("progress_history", [])
        
    except FileNotFoundError:
        return []
        
        

while True:
    print("\nSelect an option by entering a number")
    print("1: Set the number of cards you wish to practice")
    print("2: Start flashcards")
    print("3: Show the current score")
    print("4: View progress history") # Option to view progress history
    print("5: Exit")
    
    
    choice = input("\nChoose an option: ")
    
    if choice == "1":

        set_max_cards() 

    elif choice == "2":
        max_cards = get_max_cards()
        
        # Reset the number of cards completed for each session
        num_cards_completed = 0
        num_cards_correct = 0

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
                break
        
        print("\nWell done on completing your practice session!")
        # Write score info out with each session completed
        write_score_info()
        display_score_info()

    elif choice == "3":

        display_score_info()

    elif choice == "4":
        
        score_data = get_progress_history()
        if not score_data:
            # Let user know if there is no progress history data yet
            print("We can't find any progress history for you yet.")
        else:
            print("How many sessions would you like to view?")
            num_sessions = int(input("Enter the number or 0 to show all: "))
            print("What order would you like to see them in?")
            print("1: Oldest")
            print("2: Most recent")
            order = input("Choose an option by entering 1 or 2: ")

            # If the user wants to see all sessions, set num_sessions
            # to the number of sessions available
            if num_sessions==0:
                num_sessions = len(score_data) 

            selected_sessions = score_data
            if order =="2":
                # Need to reverse order of list if 
                # most recent first is selected
                selected_sessions = selected_sessions[::-1]
                selected_sessions = selected_sessions[:num_sessions]
        
            #TODO: Add handling of invalid inputs

            # Extract num_cards_completed and score from each
            # session's dictionary structure
            for i, session in enumerate(selected_sessions):
                
                # Extract num_cards_completed and score
                # Name these variables something different 
                # (e.g. saved_cards_completed, saved_score) 
                # so they don't write over those being used by the rest of the program
                saved_cards_completed = session["num_cards_practiced"]
                saved_score = session["score"]

                # Include number (counting from 1 rather than 0) for readability 
                # But does not correspond to session number
                print(f"{i+1}: {saved_cards_completed} cards completed, score {saved_score}%")
                # TODO: Include date/time stamp?

    elif choice == "5":
        print(f"We hope you enjoyed your practice session today, {name}.")
        if num_cards_completed > 0:
            display_score_info()

            # Calculate score for feedback messages
            score = (num_cards_correct/num_cards_completed) * 100

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
        print("\nInvalid value entered. Please make sure you enter just a single digit (no other words): 1, 2, 3, 4 or 5 to select an option.")