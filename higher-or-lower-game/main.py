from art import logo, vs
import game_data, random, os

data = game_data.get_data()

game_is_on = True
score = 0

choice_a = random.choice(data)
while game_is_on:
    os.system('cls')

    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}.")
    else:
        print("Guess who has more number of instagram followers!")

    choice_b = random.choice(data)

    print(f"Compare A: {choice_a[0]}, a {choice_a[2]}, from {choice_a[3]}")
    print(vs)
    print(f"Against B: {choice_b[0]}, a {choice_b[2]}, from {choice_b[3]}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    while guess not in {'a', 'b'}:
        guess = input("Please choose 'A' or 'B': ").lower()

    followers_a = int(choice_a[1].split()[0])
    followers_b = int(choice_b[1].split()[0])

    answer = 'a' if followers_a > followers_b else 'b' if followers_b > followers_a else 'ab'

    if guess in answer:
        score += 1
        choice_a = choice_b
    else:
        print(f"Sorry that's wrong. Final score: {score}")
        game_is_on = False
