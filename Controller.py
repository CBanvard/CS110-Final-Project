import sys, pygame
import tkinter as tk
import deuces
import random
import hand

class Controller:
    def __init__(self, location):
        #these are the rgb values
        white = (255, 255, 255)
        #i reference these multiple times throughout for buttons/images/other things
        display_width = 1200
        display_height = 700

        '''initialize screen'''
        pygame.init()
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Israeli Poker!')

        #initialize background images
        self.image = pygame.image.load('pokerBackground.png')
        self.image = pygame.transform.scale(self.image, (1400, 850))
        self.screen.blit(self.image, (0, 0))

        self.image3 = pygame.image.load('image3.png')
        self.screen.blit(self.image3, (625, 150))

        #Displays the welcome text
        self.font = pygame.font.SysFont("Arial", 50)
        self.font.set_bold(True)
        self.text = self.font.render("Welcome to Israeli Poker!", 1, white)
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(self.text, self.textpos)

        #Creates the Play Game button
        self.TextRect = self.font.render("Play Game!", True, white)
        self.screen.blit(self.TextRect, (200,200))

        #Creates the Instructions button
        self.TextRect = self.font.render("Instructions", True, white)
        self.screen.blit(self.TextRect, (200,300))

        #Creates the Quit Game button
        self.TextRect = self.font.render("Quit Game", True, white)
        self.screen.blit(self.TextRect, (200,400))

        #Updates the screen
        pygame.display.flip()


        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            #exits the game if user presses button to close window
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 > mouse[0] > 200 and 240 > mouse[1] > 200:
                    GameScreen((300,300))
                if 450 > mouse[0] > 200 and 340 > mouse[1] > 300:
                    root = tk.Tk()
                    photo = tk.PhotoImage(file= 'instructions.png')
                    root.title('Instructions')
                    label = tk.Label(root, image = photo)
                    label.pack()
                    root.mainloop()
                if 450 > mouse[0] > 200 and 440 > mouse[1] > 400:
                    sys.exit()

class GameScreen:
    def __init__(self, location):
        while True:
            white = (255, 255, 255)
            display_width = 1200
            display_height = 700
            self.screen = pygame.display.set_mode((display_width, display_height))
            pygame.display.set_caption('Israeli Poker')
            self.image = pygame.image.load('gameBackground.png')
            self.screen.blit(self.image, (0, 0))
            self.font = pygame.font.SysFont("Arial", 30)
            self.font.set_bold(True)
            self.TextRect = self.font.render("Back to Main Screen", True, white)
            self.screen.blit(self.TextRect, (10, 10))
            self.TextRect = self.font.render("Your hand", True, white)
            self.screen.blit(self.TextRect, (515, 565))
            self.TextRect = self.font.render("Their hand", True, white)
            self.screen.blit(self.TextRect, (510, 115))
            pygame.display.flip()

            for event in pygame.event.get():
                #exits the game if user presses button to close window
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 > mouse[0] > 10 and 30 > mouse[1] > 10:
                        while 1:
                            Controller((300,300))


            imageList = ['2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', '10c', '10d', '10h', '10s', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs', 'Kc', 'Kd', 'Kh', 'Ks', 'Ac', 'Ad', 'Ah', 'As']
            P1hand = []
            P2hand = []
            for i in range(5):
                p1randomCard = random.choice(imageList)
                p2randomCard = random.choice(imageList)
                imageList.remove(p1randomCard)
                imageList.remove(p2randomCard)
                P1hand.append(p1randomCard + '.png')
                P2hand.append(p2randomCard + '.png')
                self.image = pygame.image.load(P1hand[i])
                self.screen.blit(self.image, (350 + (100*i), 25))
                self.cardRect = (350 + (100*i), 25, 70, 100)
                self.image = pygame.image.load(P2hand[i])
                self.screen.blit(self.image, (350 + (100 * i), 600))
                self.cardRect2 = (350 + (100 * i), 600, 70, 100)

            while True:
                for event in pygame.event.get():
                    # exits the game if user presses button to close window
                    mouse = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if 300 > mouse[0] > 10 and 30 > mouse[1] > 10:
                            while 1:
                                Controller((300, 300))

                pygame.display.flip()
