import sys, pygame
import tkinter as tk
import deuces
import random

class Controller:
    def __init__(self, location):
        # these are the rgb values
        white = (255, 255, 255)
        #i reference these multiple times throughout for buttons/images/other things
        display_width = 1200
        display_height = 700

        #initialize screen
        pygame.init()
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Israeli Poker!')

        #initialize backgroundimages
        self.image = pygame.image.load('pokerBackground.png')
        self.screen.blit(self.image, (0, 0))

        self.image3 = pygame.image.load('image3.png')
        self.screen.blit(self.image3, (675, 150))

        # Displays the welcome text
        self.font = pygame.font.SysFont("Arial", 50)
        self.font.set_bold(True)
        self.text = self.font.render("Welcome to Israeli Poker!", 1, white)
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(self.text, self.textpos)

        self.TextRect = self.font.render("Play Game!", True, white)
        self.screen.blit(self.TextRect, (200,200))

        self.TextRect = self.font.render("Instructions", True, white)
        self.screen.blit(self.TextRect, (200,300))

        self.TextRect = self.font.render("Quit Game", True, white)
        self.screen.blit(self.TextRect, (200,400))

        # Blit everything to the screen
        pygame.display.flip()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            #exits the game if user presses button to close window
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 450 > mouse[0] > 200 and 240 > mouse[1] > 200:
                    print("Play Game! -", mouse)
                    GameScreen((300,300))
                if 450 > mouse[0] > 200 and 340 > mouse[1] > 300:
                    print("Instructions -", mouse)
                    root = tk.Tk()
                    photo = tk.PhotoImage(file= 'instructions.png')
                    root.title('Instructions')
                    label = tk.Label(root, image = photo)
                    label.pack()
                    root.mainloop()
                if 450 > mouse[0] > 200 and 440 > mouse[1] > 400:
                    print("Quit Game -", mouse)
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
            self.screen.blit(self.TextRect, (515, 525))
            self.TextRect = self.font.render("Their hand", True, white)
            self.screen.blit(self.TextRect, (510, 115))
            #pygame.draw.lines(self.image, white, True, (50,50), 1)
            pygame.display.flip()

            for event in pygame.event.get():
                #exits the game if user presses button to close window
                mouse = pygame.mouse.get_pos()
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print("Quit Game -", mouse)
                    if 300 > mouse[0] > 10 and 30 > mouse[1] > 10:
                        while 1:
                            Controller((300,300))

            imageList = ['2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', '10c', '10d', '10h', '10s', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs', 'Kc', 'Kd', 'Kh', 'Ks', 'Ac', 'Ad', 'Ah', 'As']
            newList = [c + '.png' for c in imageList]
            self.image = pygame.image.load(random.choice(newList))
            self.screen.blit(self.image, (350, 25))
            self.screen.blit(self.image, (450, 25))
            self.screen.blit(self.image, (550, 25))
            self.screen.blit(self.image, (650, 25))
            self.screen.blit(self.image, (750, 25))

            self.screen.blit(self.image, (350, 600))
            self.screen.blit(self.image, (450, 600))
            self.screen.blit(self.image, (550, 600))
            self.screen.blit(self.image, (650, 600))
            self.screen.blit(self.image, (750, 600))

            pygame.display.flip()



def main():
    while 1:
        Controller((300,300))
main()

