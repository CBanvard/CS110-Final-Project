import hand
import card
import collection
class Player

    def __init__(self):
        self.collection = []
        for i in range(5):
            self.collection.append(Collection())
        self.hand = Hand()

    def playCard(self, card, collectionchoice):
        self.collection[collectionchoice-1].addCard(card)

    def selectCollection(self, collectionchoice):
        return self.collection[collectionchoice - 1]

    def selectCard(self, hand, cardchoice)
                  
            if 1 <= charchoice <= 5:
                  print("Please input a valid choice.")
            else:
                  playCard(hand[cardchoice-1], selectCollection())
