import sys, pygame

class Screen:
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

        #initialize background
        self.image = pygame.image.load('pokerbackground.png')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.screen.blit(self.image, (0, 0))

        self.image4 = pygame.image.load('cardBack.png')

        self.image3 = pygame.image.load('image3.png')
        self.rect3 = self.image3.get_rect()
        self.rect3.left, self.rect3.top = location
        self.screen.blit(self.image3, (625, 150))

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

        #adds sound
        sound = pygame.mixer.music.load('Elevator-music.mp3')
        pygame.mixer.music.play(-1)

        # Blit everything to the screen
        pygame.display.flip()

'''
    def scoreboard(self):




    def play_game(self):
        self.screen.blit(self.image, (0, 0))











    def instructions(self):
        self.screen.blit(self.image, (0, 0))
        self.image2 = pygame.image.load('instructions.png')
        self.rect2 = self.image2.get_rect()
        self.rect2.left, self.rect2.top = location
        self.screen.blit(self.image2, (150, 75))

    def results(self):
'''


def main():
    while 1:
        c = Screen((300,300))
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            #exits the game if user presses button to close window
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 450 > mouse[0] > 200 and 240 > mouse[1] > 200:
                    print("Play Game! -", mouse)
                if 450 > mouse[0] > 200 and 340 > mouse[1] > 300:
                    print("Instructions -", mouse)
                if 450 > mouse[0] > 200 and 440 > mouse[1] > 400:
                    sys.exit()
main()
