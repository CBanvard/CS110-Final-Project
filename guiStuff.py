import pygame

class Screen(pygame.sprite.Sprite):
    def __init__(self, location):

        # these are the rgb values
        black = (0, 0, 0)
        white = (255, 255, 255)

        #i reference these multiple times throughout for buttons/images/other things
        display_width = 1440
        display_height = 900

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
        #more rgb values
        red = (200, 0, 0)
        bright_red = (255, 0, 0)

        #loads all the images
        gameDisplay.blit(self.image, (x, y))
        self.x = display_width * 1
        self.y = display_height * 1

        mouse = pygame.mouse.get_pos()
        #draws button1
        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (150, 450, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (150, 450, 100, 50))

        smallText = pygame.font.Font("Arial.ttf", 20)
        textSurf, textRect = text_objects("Play Game!", smallText)
        textRect.center = ((150 + (100 / 2)), (450 + (50 / 2)))
        gameDisplay.blit(textSurf, textRect)

        #draws button2
        if 150 + 100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (150, 750, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (150, 750, 100, 50))

        textSurf, textRect = text_objects("Instructions", smallText)
        textRect.center = ((150 + (100 / 2)), (750 + (50 / 2)))
        gameDisplay.blit(textSurf, textRect)

        # draws button3
        if 150 + 100 > mouse[0] > 150 and 950 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red, (150, 950, 100, 50))
        else:
            pygame.draw.rect(gameDisplay, red, (150, 950, 100, 50))

        textSurf, textRect = text_objects("Quit Game", smallText)
        textRect.center = ((150 + (100 / 2)), (750 + (50 / 2)))
        gameDisplay.blit(textSurf, textRect)

        pygame.display.update()

        #Event loop
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return

def main():
    self.image(x,y)
main()
