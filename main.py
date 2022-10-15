import random
class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __repr__(self):
        return self.val + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.deck = []

        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for suit in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
            for value in values:
                card = Card(suit, value)
                self.deck.append(card)