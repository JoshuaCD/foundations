#I used the video guide to help get me started with this assignment

import itertools
from random import shuffle

#Define Helper Functions

def draw(temp):
    temp.append(deck.pop())

def value(hand):

    total = 0
    aces = 0

    for i in range(len(hand)):
        if (hand[i][1] == 'Jack' or hand[i][1] == 'Queen' or hand[i][1] == 'King'):
            total += 10

        elif hand[i][1] == 'Ace':
            total += 1
            aces += 1

        else:
            total += hand[i][1]

    while total <= 11:
        if aces >= 1:
            total += 10
            aces -= 1
        else: break

    return total


#Generate Deck
suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

deck = list(itertools.product(suits, ranks))
shuffle(deck)

#Generate hands
Player_Hand = []
Dealer_Hand = []


for _ in range(2):
    draw(Player_Hand)
    draw(Dealer_Hand)

#Start Game

print("Let's play blackjack!")
print("Your hand is {0} with a value of {1}.".format(Player_Hand, value(Player_Hand)))
print("The dealer is showing {0}".format(Dealer_Hand[0]))

#This is probably not ideal
action = 'null'

while True:


#Resolve Game

    if value(Player_Hand) > 21:
        print("Sorry, you went bust!")
        break

    elif (value(Player_Hand) == 21 or action == 's'):
        print("The dealer's hand is {0}.".format(Dealer_Hand))

        while value(Dealer_Hand) < 17:
            draw(Dealer_Hand)
            print("The dealer hits {0}.".format(Dealer_Hand))

        print("The dealer's hand score is {0}".format(value(Dealer_Hand)))

        if (value(Dealer_Hand) > 21):
            print("The dealer went bust, you win!")
            break

        if (value(Player_Hand) < value(Dealer_Hand)):
            print("Your hand score is {0} and the dealer's is {1}, sorry you lose."
                .format(value(Player_Hand), value(Dealer_Hand)))

        if (value(Player_Hand) > value(Dealer_Hand)):
            print("Your hand score is {0} and the dealer's is {1}, congratulations you win!"
                .format(value(Player_Hand), value(Dealer_Hand)))

        if (value(Player_Hand) == value(Dealer_Hand)):
            print("Your hand score is {0} and the dealer's is {1}, it's a draw."
               .format(value(Player_Hand), value(Dealer_Hand)))

        break

    elif action == 'h':
        draw(Player_Hand)
        print("Your hand is {0} with a value of {1}.".format(Player_Hand, value(Player_Hand)))
        action = 'null'

#Check for player action

    else:
        action = input("Type 'h' to hit or 's' to stand: ")

print("Thanks for playing!")
