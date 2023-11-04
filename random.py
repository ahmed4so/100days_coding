# Import the random module to generate a random number
import random

# Display a welcome message for the game
print("====================== Guess the number game ===============================")

# Generate a random number between 5 and 10 (inclusive)
number = random.randint(5, 10)

# Instruct the user to guess a number between 5 and 10
print("Guess a number between 5 and 10")

# Initialize the number of attempts and the maximum number of attempts allowed
attempts = 0
max_attempts = 3

# Create a loop that allows the user to guess the number within the maximum attempts
while attempts < max_attempts:
    # Get the user's guess as an integer
    input_user = int(input("Guess the number: "))

    # Check if the user's guess is equal to the randomly generated number
    if input_user == number:
        print("Your guess is right :)")  # Display a success message
        break  # Exit the loop since the user guessed correctly

    # If the user's guess is higher than the random number, provide a hint to try a lower number
    elif input_user > number:
        print("Try a lower number ")

    # If the user's guess is lower than the random number, provide a hint to try a higher number
    else:
        print("Try a higher number ")

    # Increment the number of attempts
    attempts += 1

    # If the user has used all the allowed attempts, display the correct number and a message
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {number}. Better luck next time!")
