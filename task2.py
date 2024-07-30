# # Numbwr guessing game between user and computer

# import random
# number = random.randint(1,50) 
# guess = int(input("Guess a number between 1 and 50: "))

# while guess != number:
#   if guess < number:
#     print("your guess number is too low.")
#   elif guess > number:
#     print("your guess number is too high.")
#     count = count + 1;
  
  
#   guess = int(input("Guess agian:"))

# print("Great!! you guessed it right.")

import random

def number_guessing_game():
    number_to_guess = random.randint(1, 50)
    attempts = 0
    guessed_correctly = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 50. Can you guess it?")

    while not guessed_correctly:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

number_guessing_game()
