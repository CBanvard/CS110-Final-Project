from deuces import evaluator
from deuces import deck
import hand
import collection
import player

class Table:
    
    def __init__(self):
        '''
        Intizilizes the Player class and creates both players
        param: Self
        returns: None
        '''
        self.P1 = player.Player()
        self.P2 = player.Player()
        self.round_num = 0
    
    def gameFlow(self):
        '''
        Starts the game, and begins to call all the other classes
        param: Self
        returns: None
        '''
        for i in range(5):
            self.round_num += 1
            self.P1.hand.deal()
            self.P2.hand.deal()
            for i in range(5):
                self.P1.selectCard()
                self.P2.selectCard()
    
    def whoWins(self):
        '''
        After the game is finished this is called and it evaulates each collection against the other
        param: Self, which is each player
        returns: None
        '''
        evaluator = Evaluator()
        
        P1_hands_won = 0
        P2_hands_won = 0
        
        for i in range(5):
            if evaluator.evaluate(P1.collection[i]) > P2.collection[i]):
                P1_hands_won += 1
            elif evaluator.evaluate(P1.collection[i]) < P2.collection[i]):
                P2_hands_won += 1
            else:
                print("There was a tie.")
    
        if P1_hands_won > P2_hands_won:
            print("Player One Triumphs!")

        elif P1_hands_won < P2_hands_won:
            print("Player Two Prevails!")
        
        else:
            print("There was a tie...")

