import pygame


class Screen(pygame.sprite.Sprite):
    def __init__(self, location):

        #i reference these multiple times throughout for buttons/images/other things
        display_width = 1440
        display_height = 900

        #these are the rgb values
        black = (0,0,0)
        white = (255,255,255)
        red = (255,0,0)

        #initialize screen
        pygame.init()
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Israeli Poker!')

        #initialize background
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pokerBackground.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        #Displays the welcome text
        self.font = pygame.font.Font(Arial, 36)
        self.font.bold()
        self.text = self.font.render("Welcome to Israeli Poker!", 1, white)
        self.textpos = text.get_rect()
        self.textpos.centerx = self.background.get_rect().centerx
        self.background.blit(text, textpos)

        #Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.update()

    def screenImages(self,x,y):
        #loads all the images
        newGame = pygame.image.load('button1.jpg').convert_alpha()
        Instructions = pygame.image.load('button2.jpg').convert_alpha()
        Quit = pygame.image.load('button3.jpg').convert_alpha()
        gameDisplay.blit(self.image, (x, y))
        self.x = display_width * 1
        self.y = display_height * 1

        gameDisplay.blit(newGame, (x, y))
        self.x = display_width * .45
        self.y = display_height * .4

        gameDisplay.blit(Instructions, (x, y))
        self.x = display_width * .45
        self.y = display_height * .6

        gameDisplay.blit(Quit, (x, y))
        self.x = display_width * .45
        self.y = display_height * .8

        #Event loop
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

            self.image(x,y)
            newGame(x,y)
            Instructions(x,y)
            Quit(x,y)

