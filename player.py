import hand
import collection
class Player:

    def __init__(self):
        '''
        Intizilizes the player class which creates both players
        param: Self
        returns: None
        '''
        self.collection = []
        for i in range(5):
            self.collection.append(collection.Collection())
        self.hand = hand.Hand()

    def playCard(self, card, collectionchoice):
        '''
        Calls the Collection class and then decides if the player will play the card
        param: Self, The card that the person is playing, and the collection they decided to choose
        
        returns: None
        '''
        self.collection[collectionchoice-1].addCard(card)
        del hand[cardchoice-1]

    def selectCollection(self, collectionchoice):
        '''
        Lets the player choose which collection they wish to play the card in
        param: Self, and the index of the collection so it knows which collection to play on
        returns: The collection the player chose
        '''
        return self.collection[collectionchoice - 1]

    def selectCard(self, hand, cardchoice):
        '''
        Lets the player choose which card they want to play
        param: Self, hand, which is the players hand which contains the cards, cardchoice which is the card that the player chooses
        returns: The card they chose
        '''
        if 1<=cardchoice<=5:
            playCard(hand[cardchoice-1], selectCollection())
        else:
            print("Please input valid card choice.")
