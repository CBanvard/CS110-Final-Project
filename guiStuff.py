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
        #loads all the images
        gameDisplay.blit(self.image, (x, y))
        self.x = display_width * 1
        self.y = display_height * 1

    def button(msg, x, y, w, h, ic, ac, action=None):
        # more rgb values
        red = (200, 0, 0)
        bright_red = (255, 0, 0)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        print(click)
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

        smallText = pygame.font.SysFont("Arial", 40)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)

        button("Play Game!", 300, 450, 100, 50, red, bright_red, game_loop)
        button("Instructions", 300, 650, 100, 50, red, bright_red, instructions)
        button("QuitGame", 300, 850, 100, 50, red, bright_red, quitgame)

    def game_loop(self):







    def instructions(self):





    def quitgame(self):
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return


def main():
    self.image(x,y)
main()
