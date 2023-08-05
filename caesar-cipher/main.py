from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):

    code = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter) + shift
            code += alphabet[position if position < 26 else position-26]
        else:
            code += letter
    print(f"The {direction} text is {code}")

print(logo)

while True:

    choice = {'encode', 'decode'}
    direction = ""

    while direction not in choice:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))%26

    caesar(text, shift, direction)

    user_input = ""
    valid_input = {'yes', 'no'}

    while user_input not in valid_input:
        user_input = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    
    if user_input == 'no':
        print("Goodbye!")
        break
