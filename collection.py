from deuces import deck
import player
import hand
class Collection:

    def __init__(self):
        '''
        Intizilizes the collection class
        param: Self, and the location of the gui in a tuple
        returns: None
        '''
        self.collection = []
        self.already_played = 0

    def addCard(self, card):
        '''
        Adds cards to the different collections which are columns inside of the game
        param: Self, and the card that is being played inside of the column
        returns: None
        '''
        if table.round_num = already_played:
            self.collection.append(card)
            self.already_played += 1
        else:
            print("Cannot play in this collection.")
