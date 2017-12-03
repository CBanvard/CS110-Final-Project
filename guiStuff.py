import pygame
import main

height = 1000
width = 1000

class Screen:
    def __init__(self):
        deck = collection.Deck()
        self.images = {}
        self.scale = .5
        self.cardSize = (width / 5, width / 5)
        self.Lctn = pygame.image.load('backGround') #stillneedtofind
        self.cardBack = pygame.image.load('cardBack') #stillneedtofind

        pygame.font.init()
        font = pygame.font.Font(Arial, 24)
        loadText = font.render('Loading!', 1)
        loadSize = font.size('Loading!')
        loadBack = (width / 2 - loadSize[0] / 2, height / 2 - loadSize[0] / 2)

        screen.blit(self.Lctn, (-300, 100))
        screen.blit(loadText, loadBack)


    def first_init(self):
    # menu graphics
        self.font2 = pygame.font.Font('font/Calibri, 100')
        self.font.bold()

        self.startText = self.font2.render('Welcome to Israeli Poker!, 1')
        self.startSize = self.font2.size('Welcome to Israeli Poker!')
        self.startLoc = (width / 2 - self.startSize[0] / 2, self.buffer)

        self.startButton = self.font.render(" Start ", 1, BLACK)
        self.buttonSize = self.font.size(" Start ")
        self.buttonLctn = (width / 2 - self.buttonSize[0] / 2, HEIGHT / 2 - self.buttonSize[1] / 2)

        self.buttonRect = pygame.Rect(self.buttonLoc, self.buttonSize)
        self.buttonRectOutline = pygame.Rect(self.buttonLoc, self.buttonSize)
        self.state = 0

    def main(self):
        # options menu (1,2,3,4 for the different keys)
        if self.state == 0:
            self.start_up()
        elif self.state == 1:
            self.play()
        elif self.state == 2:
            self.results()
        elif self.state == 3:
            self.new_game()

    def start_up(self):

        for userInput in pygame.event.get():
            if userInput.input == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # when the user clicks the start button, change to the playing state
            elif userInput.input == pygame.MOUSEBUTTONDOWN:
                if userInput.input == 1:
                    mouseRect = pygame.Rect(event.pos, (1, 1))
                    if mouseRect.colliderect(self.buttonRect):
                        self.state += 1
                        self.play_init()
                        return

    def play(self):
        for userInput in pygame.event.get():
            if userInput.input == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # when the user clicks on a card, change its color to signify a selection has occurred
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: #creates rectangle
                    mouseRect = pygame.Rect(event.pos, (1, 1))
                    for card in range(len(self.poker.playerHand)):
                        cardRect = pygame.Rect(self.cardLoc[card],
                                               (int(self.scale * self.cardSize[0]), int(self.scale * self.cardSize[1])))
                        if cardRect.colliderect(mouseRect):
                            self.poker.playerHand[card].selected = not self.poker.playerHand[card].selected
                            break

                    # check if we clicked the replaceButton
                    if mouseRect.colliderect(self.buttonRect):
                        self.poker.replace(self.poker.playerHand)
                        self.poker.computerReplace()
                        self.round += 1
                        if self.round == 2:
                            self.state += 1
                            self.results_init()
                            return




