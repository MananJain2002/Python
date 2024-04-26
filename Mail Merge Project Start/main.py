PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as f:
    names = [name.strip() for name in f.readlines()]

with open("./Input/Letters/starting_letter.txt", mode="r") as f:
    letter = f.read()
    for name in names:
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
            f.write(new_letter)