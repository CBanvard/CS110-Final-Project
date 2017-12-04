import pygame

class Screen:
    def __init__(self, location):
        # these are the rgb values
        black = (0, 0, 0)
        white = (255, 255, 255)

        #i reference these multiple times throughout for buttons/images/other things
        display_width = 1200
        display_height = 700

        #initialize screen
        pygame.init()
        self.screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption('Israeli Poker!')

        #initialize background
        self.image = pygame.image.load('pokerBackground.xcf')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        #Displays the welcome text
        self.font = pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
        self.font.set_bold(True)
        self.text = self.font.render("Welcome to Israeli Poker!", 1, white)
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(self.text, self.textpos)

        #Blit everything to the screen
        pygame.display.flip()

    def screenImages(self, x, y):
        #loads all the images
        gameDisplay.blit(self.image, (x, y))
        self.x = display_width * 1
        self.y = display_height * 1

    def button(self, msg, x, y, w, h, ic, ac, action= None):
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

        smallText = pygame.font.SysFont("C:\Windows\Fonts\Arial.ttf", 40)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        gameDisplay.blit(textSurf, textRect)

        button("Play Game!", 300, 250, 100, 50, red, bright_red, game_loop)
        button("Instructions", 300, 450, 100, 50, red, bright_red, instructions)
        button("QuitGame", 300, 650, 100, 50, red, bright_red, quitgame)

    #def game_loop(self):
    #def instructions(self):

        running = True
        try:
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
            pygame.quit()
        except SystemExit:
            pygame.quit()

def main():
    c = Screen((300,300))
    #button("Play Game!", 300, 450, 100, 50, red, bright_red, game_loop)
    #button("Instructions", 300, 650, 100, 50, red, bright_red, instructions)
    #button("QuitGame", 300, 850, 100, 50, red, bright_red, quitgame)
main()
