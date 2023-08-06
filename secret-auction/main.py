from art import logo
import os

print(logo)

bids = dict()

print("Welcome to the secret auction program")
bidding_finished = True
while bidding_finished:
    name = input("What is your name?: ")
    price = 0
    while price <= 0:
        try:
            price = int(input("What's your bid?: $"))
        except:
            print("Please enter an integer")
        
    bids[name] = price

    bidding_finished = False if input("Are there any other bidders? Then type 'yes' or 'no' ").lower() == 'no' else True
    os.system('cls')

winner = ""
winning_bid = 0
for key, value in bids.items():
    if winning_bid < value:
        winner = key
        winning_bid = value

print(f"The winner is {winner} with a bid of ${winning_bid}")