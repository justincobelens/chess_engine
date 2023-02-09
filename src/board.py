import numpy as np

from const import *
from square import Square
from piece import *


class Board:

    def __init__(self):
        # creating a 2d-array for each column that represent the squares
        self.squares = np.zeros((8, 8))
        self.squares = [[0]*8]*8

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    # private methods
    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        # by default
        # row 1 and 6 only has pawns
        # row 0 and 7 only has other pieces

        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color=color))

        # knights
        self.squares[row_other][1] = Square(row_other, 1, Knight(color=color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color=color))

        # bishops
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color=color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color=color))

        # rooks
        self.squares[row_other][0] = Square(row_other, 0, Rook(color=color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color=color))

        # queen
        self.squares[row_other][3] = Square(row_other, 3, Queen(color=color))

        # king
        self.squares[row_other][4] = Square(row_other, 4, King(color=color))

# squares = np.zeros((8, 8))
# print(squares[0][0])
#
# squares = [[0]*8]*8
# print(squares[0][0])