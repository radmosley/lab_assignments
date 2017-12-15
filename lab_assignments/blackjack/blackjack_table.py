import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print('{} of {}'.format(self.suit, self.value))

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ['spades', 'clubs', 'diamonds', 'hearts']:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
    
    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()
         

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self
 
    def showhand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

deck_1 = Deck()
deck_1.shuffle()

player_1 = Player("Player 1")
player_1.draw(deck_1).draw(deck_1)
player_1.showhand()

dealer_1 = Player("Dealer 1")
dealer_1.draw(deck_1).draw(deck_1)
dealer_1.showhand()