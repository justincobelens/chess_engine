import pygame
import sys

from const import *
from game import Game
from board import Board


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

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            # show the background
            game.show_background(screen)

            # show the pieces
            game.show_pieces(screen)


            # looping through events
            for event in pygame.event.get():

                # if click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)
                    # print(event.pos)

                    # convert clicked coords to square row and col number
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    # if clicked square has a piece ?
                    if board.squares[clicked_row, clicked_row].has_piece():
                        piece = board.squares[clicked_row, clicked_row].piece
                        dragger.save_initial(event.pos)

                # if mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    pass

                # if click release
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass


                # if user wants to quit
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
