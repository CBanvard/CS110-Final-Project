import random
from deuces import deck
class Hand:

    def __init__(self):
        '''
        Intizilizes Hand class, which creates the hand for each player
        param: Self,
        returns: None
        '''
        self.hand = []

    def deal(self):
        '''
        Deals out the cards to each players hand randomly
        param: Self, and the location of the gui in a tuple
        returns: None
        '''
        hand.append(deck.draw(5))
