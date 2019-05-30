# Zak Gelfond
# computing ID: zlg8dt

import random
from random import shuffle
import sys

num_of_players = input("How many players are you? ")

# first_input = int(sys.argv[1]) #here we use int() to convert the string input into an integer
#
# # now we can use first_input
# print(first_input)
#
players = []

# for i in range(int(first_input)):
#     x = input("What is player "+str(i+1)+"'s name? ")
#     players.append(x)

for i in range(int(num_of_players)):
    x = input("What is player "+str(i+1)+"'s name? ")
    players.append(x)

class Cards():
    def __init__(self, value, color):
        self.value = value
        self.color = color


suits = ['clubs', 'spades', 'hearts', 'diamonds']
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
deck = [Cards(value, suit) for value in range(1, 14) for suit in suits]

print(deck)
