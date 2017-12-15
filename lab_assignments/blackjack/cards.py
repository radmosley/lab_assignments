# #give cards suit and rank
# import random

# card_values = {
#     'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10
#     }

# suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

# class Card:
#     def __init__(self, suit, rank, value):
#         self.suit = suit
#         self.rank = rank

#     def __str__(self):
#         return '{} of {}'.format(self.rank, self.suit)

#     def __repr__(self):
#         return '{} of {}'.format(self.rank[0], self.suit)

# class Deck:
#     def __init__(self, suit, rank, value):
#         self.cards = [Card(suit, rank) for s in suit for r in rank]
#         self.shuffle()

#     def __str__(self):
#         deck_cards = ''
#         for cards in self.cards:
#             deck_cards = deck_cards + str(card) + ''
#         return deck_cards

#     def shuffle(self):
#         random.shuffle(self.cards)

#     def deal_card(self):
#         card = self.cards.pop(0)
#         return cards

# class Hand:
#     def __init__(self):
#         self.hand = []

#     def add_card(self, card):
#         self.hand.append(card)
#         return self.hand

#     def get_value(self):
#         aces = 0
#         value = 0
#         for card in self.hand:
#             if Card.is_ace():
#                 aces =+ 1
#             value += card.point
#         while (value > 21) and aces:
#             value -= 10
#             aces -= 1
#         return value

import random

card_values = {
    'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10
    }

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{} of {}'.format(self.rank[0], self.suit[0])

deck = []

for s in suits:
    for rank, value in card_values.items():
        deck.append(Card(s, rank, value))
random.shuffle(deck)
    return deck