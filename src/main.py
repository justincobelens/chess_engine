import pygame
import sys

from const import *
from game import Game


class Main:

    def __init__(self):
        # create pygame object
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # set title of screen
        pygame.display.set_caption('Chess')

        # create game object
        self.game = Game()

    def mainloop(self):

        game = self.game
        screen = self.screen

        while True:
            # show the background
            game.show_background(screen)

            # show the pieces
            game.show_pieces(screen)


            # looping through events if user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
