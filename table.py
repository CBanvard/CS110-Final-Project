from deuces import evaluator
from deuces import deck
import hand
import collection
import player

class Table:

    def __init__(self):
        self.P1 = player.Player()
        self.P2 = player.Player()
        self.round_num = 0

    def gameFlow(self):
        for i in range(5):
            self.round_num += 1
            for i in range(5):
                self.P1.selectCard()
                self.P2.selectCard()
    
    def whoWins(self):
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

        if P1_hands_won < P2_hands_won:
            print("Player One Triumphs!")

        elif P1_hands_won > P2_hands_won:
            print("Player Two Prevails!")
        
        else:
            print("There was a tie...")
