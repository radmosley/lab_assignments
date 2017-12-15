import cards 
import random

print(Card())

class Deck(Card):
    deck = []
    for s in suits:
        for rank, value in card_values.items():
            deck.append(Card(s, rank, value))
        random.shuffle(deck)
        return deck

print(Deck())