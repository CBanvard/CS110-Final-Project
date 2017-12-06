import sys, pygame
import tkinter as tk

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
                    '''root = tk.Tk()
                    photo = tk.PhotoImage(file='gameBackground.png')
                    root.title('Israeli Poker')
                    label = tk.Label(root, image=photo)
                    label.pack()
                    root.mainloop()'''
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
        white = (255, 255, 255)
        pygame.init()
        display_width = 1200
        display_height = 700
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Israeli Poker')
        self.image = pygame.image.load('gameBackground.png')
        self.screen.blit(self.image, (0, 0))
        self.font = pygame.font.SysFont("Arial", 50)
        self.font.set_bold(True)
        self.TextRect = self.font.render("New Game", True, white)
        self.screen.blit(self.TextRect, (50, 50))
        pygame.display.flip()

        for event in pygame.event.get():
            #exits the game if user presses button to close window
            if event.type == pygame.QUIT: sys.exit()


def main():
    while 1:
        c = Controller((300,300))
main()

