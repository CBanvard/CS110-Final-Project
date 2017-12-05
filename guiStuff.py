import sys, pygame

class MainScreen:
    def __init__(self):
        #loads all the reference variables
        pygame.init()
        self.width = 1200
        self.height = 700
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Israeli Poker!')

        self.background = pygame.image.load('pokerbackground.png')
        self.screen.blit(self.background, (0, 0))
        self.image3 = pygame.image.load('image3.png')
        self.screen.blit(self.image3, (625, 150))
        self.font = pygame.font.SysFont("Arial", 50)
        self.font.setbold(True)

    def start_init(self):
        white = (255, 255, 255)
        #printsimages
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.image3, (625, 150))

        self.text = self.font.render("Welcome to Israeli Poker!", 1, white)
        self.textpos = self.text.get_rect()
        self.textpos.centerx = self.screen.get_rect().centerx
        self.screen.blit(self.text, self.textpos)

        self.TextRect = self.font.render("Play Game!", True, white)
        self.TextRect.get_rect()
        self.screen.blit(self.TextRect, (200, 200))

        self.TextRect = self.font.render("Instructions", True, white)
        self.TextRect.get_rect()
        self.screen.blit(self.TextRect, (200, 300))

        self.TextRect = self.font.render("Quit Game", True, white)
        self.TextRect.get_rect()
        self.screen.blit(self.TextRect, (200, 400))

    def state_loop(self):
        self.state = 0
        while True:
            if self.state == 0:
                self.gameloop()
            elif self.state == 1:
                self.instructions()
            elif self.state == 2:
                sys.exit()

    def main_loop(self):
        

    def instructions(self):
        self.screen.blit(self.background, (0, 0))
        self.image2 = pygame.image.load('instructions.png')
        self.rect2 = self.image2.get_rect()
        self.rect2.left, self.rect2.top = location
        self.screen.blit(self.image2, (150, 75))

        self.TextRect = self.font.render("Return to Menu!", True, white)
        self.TextRect.get_rect()
        self.screen.blit(self.TextRect, (400, 200))

'''
        if 450 > mouse[0] > 200 and 240 > mouse[1] > 200:
            if rect.collidepoint(200, 200):
                mainloop()

        if 450 > mouse[0] > 200 and 340 > mouse[1] > 300:
            if rect.collidepoint(200, 300):
                instructions()

        if 450 > mouse[0] > 200 and 440 > mouse[1] > 400:
            if rect.collidepoint(200, 400):
                sys.exit()

        pygame.display.flip()

'''

def main():
        c = MainScreen(300, 300)
main()
