import hand
import collection

class Player

    def __init__(self):
        self.collection = Collection()
        self.hand = Hand()

    def player(self):
    #Dealing a player a hand of cards using thd deal function from the Hand class
        Player.deal.hand()

    def playCard(self, card):
        collection = collection + card

    def selectCard(self, hand):
        playerchoice = int(input("To choose card to play, please enter a number from 1-5 that corresponds to the card in your hand."))
        if playerchoice == 1:
            playCard(card1)
        elif playerchoice == 2:
            playCard(card2)
        elif playerchoice == 3:
            playCard(card3)
        elif playerchoice == 4:
            playCard(card4)
        elif playerchoice == 5:
            playCard(card5)
        else:
            print("Please select valid choice.")
