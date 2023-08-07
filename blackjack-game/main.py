from art import logo
from random import choice
import os

def add_card(hand, cards):
    card = choice(cards)
    hand.append(card)
    cards.remove(card)

def print_scores(players_hand, dealers_hand, player_score):
    print(f"\tYour cards: {players_hand}, current score: {player_score}")
    print(f"\tComputer's first card: {dealers_hand[0]}")

def calculate_score(hand):
    score = 0
    has_ace = False

    for card in hand:
        if str(card) in 'JQK':
            score += 10
        elif str(card) == 'A':
            has_ace = True
        else:
            score += card

    if has_ace:
        ace = hand.count('A')
        while ace > 1:
            score += 1

        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    
    return score

def end_game(players_hand, dealers_hand, player_score, dealer_score, cards):
    
    if player_score <= 21:
        while dealer_score < 17:
            add_card(dealers_hand, cards)
            dealer_score = calculate_score(dealers_hand)
    
    print(f"\tYour final hand: {players_hand}, final score: {player_score}")
    print(f"\tComputer's final hand: {dealers_hand}, final score: {dealer_score}")

    if player_score > 21:
        print(f"You went over. You lose 😭")
    elif dealer_score > 21:
        print(f"Opponent went over. You win 😁")
    else:
        if player_score > dealer_score:
            print("You win 😃")
        elif dealer_score > player_score:
            print("You lose 😤")
        else:
            print("It's a draw 🙃")
        
while True if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y' else False:
    
    os.system('cls')
    print(logo)

    cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']*4

    dealers_hand = []
    players_hand = []

    player_score = 0
    dealer_score = 0

    for i in range(2):
        add_card(players_hand, cards)
        add_card(dealers_hand, cards)
    player_score = calculate_score(players_hand)
    dealer_score = calculate_score(dealers_hand)
    print_scores(players_hand, dealers_hand, player_score)

    while True:

        if player_score > 21:
            break

        hit = True if input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y' else False

        if hit:
            add_card(players_hand, cards)
            player_score = calculate_score(players_hand)
            print_scores(players_hand, dealers_hand, player_score)
        else:
            break
    
    end_game(players_hand, dealers_hand, player_score, dealer_score, cards)
