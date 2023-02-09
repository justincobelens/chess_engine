import pygame

from const import *
from board import Board


class Game:

    def __init__(self):
        self.board = Board()


    def show_background(self, surface):
        for row in range(ROWS):
            for col in range(COLS):

                # alternating colors per square
                if (row + col) % 2 == 0:
                    color = (234, 235, 200)  # light green
                else:
                    color = (119, 154, 88)  # dark green

                # defining the rectangle of the screen
                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                # drawing screen
                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):

                # check for piece on square
                if self.board.squares[row][col].has_piece():

                    # setting new variable to make it more readable
                    piece = self.board.squares[row][col].piece

                    # loading image into pygame
                    img = pygame.image.load(piece.texture)

                    # getting coords of the center of the square
                    img_center = col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2

                    # adding image to screen
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)
