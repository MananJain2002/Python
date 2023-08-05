from hangman_art import *
import random, requests, json

# Getting different countries name from an api
response_api = requests.get('https://api.first.org/data/v1/countries')
data = response_api.text

parse_json = json.loads(data)['data']

countries = []
for key in parse_json.keys():
    countries.append(parse_json[key]['country'].split("(")[0].lower().strip())

chosen_word = random.choice(countries)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Game Starts
print(logo)
print("\n\n Guess the Country name")

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ['_']*word_length

letters = set()

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        continue
    elif guess in letters:
        print(f"You've already guessed {guess}")
        continue

    letters.add(guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The answer was {chosen_word}")

    print(stages[lives])

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
