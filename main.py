import random
class Card():
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __repr__(self):
        return self.val + ' of ' + self.suit