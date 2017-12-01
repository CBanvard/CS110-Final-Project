import hand
import collection
class Player:

    def __init__(self):
        self.collection = []
        for i in range(5):
            self.collection.append(collection.Collection())
        self.hand = hand.Hand()

    def playCard(self, card, collectionchoice):
        self.collection[collectionchoice-1].addCard(card)
        del hand[cardchoice-1]

    def selectCollection(self, collectionchoice):
        return self.collection[collectionchoice - 1]

    def selectCard(self, hand, cardchoice):
        if 1<=cardchoice<=5:
            playCard(hand[cardchoice-1], selectCollection())
        else:
            print("Please input valid card choice.")
