import sys, pygame
from PIL import Image

class Screen:
    def __init__(self, location):
        # these are the rgb values
        black = (0, 0, 0)
        white = (255, 255, 255)

        clock = pygame.time.Clock()

        #i reference these multiple times throughout for buttons/images/other things
        display_width = 1200
        display_height = 700

        #initialize screen
        pygame.init()
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Israeli Poker!')

        #initialize background
        self.image = pygame.image.load('pokerBackground.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.screen.blit(self.image, (0, 0))

        # Displays the welcome text
        self.font = pygame.font.SysFont("Arial", 50)
        self.font.set_bold(True)
        self.text = self.font.render("Welcome to Israeli Poker!", 1, white)
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(self.text, self.textpos)

        self.TextRect = self.font.render("Play Game!", True, white)
        self.TextRect.get_rect()
        self.screen.blit(self.TextRect, (200,200))

        self.TextRect = self.font.render("Instructions", True, white)
        self.TextRect.get_rect()
        self.screen.blit(self.TextRect, (200,300))

        self.TextRect = self.font.render("Quit Game", True, white)
        self.TextRect.get_rect()
        self.screen.blit(self.TextRect, (200,400))

        # Blit everything to the screen
        pygame.display.flip()

        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            #exits the game if user presses button to close window
            if event.type == pygame.QUIT: sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 450 > mouse[0] > 200 and 240 > mouse[1] > 200:
                    print("Play Game! -", mouse)
                    my_table = table.Table()
                    my_table.gameFlow()
                if 450 > mouse[0] > 200 and 340 > mouse[1] > 300:
                    print("Instructions -", mouse)
                    img = Image.open('instructions.png')
                    img.show()
                if 450 > mouse[0] > 200 and 440 > mouse[1] > 400:
                    print("Quit Game -", mouse)
                    sys.exit()

