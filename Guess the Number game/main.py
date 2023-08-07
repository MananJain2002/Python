from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = 'hard' if input("Choose a difficulty. Type 'easy' or 'hard': ").lower() == 'hard' else 'easy'

lives = 10 if difficulty == 'easy' else 5

number = random.randint(1, 100)

while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")

    try:
        guess = int(input("Make a guess: "))
    except:
        print("Enter an integer please")

    if abs(guess-number) > 10:
        if guess > number:
            print("Too high.")
        else:
            print("Too low.")
    else:
        if guess > number:
            print("Your number is a bit high")
        elif guess < number:
            print("Your number is a bit low")
        else:
            print(f"You got it! The answer was {number}.")
            break
    print("Guess again.")
    lives -= 1

if lives == 0:
    print("You've run out of guesses, you lose.") 
