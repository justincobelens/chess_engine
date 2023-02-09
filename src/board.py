from dataclasses import dataclass, field
from const import *
from square import Square
from piece import *


@dataclass
class Board:
    squares: list = field(init=False)

    def __post_init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for _ in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    # private methods
    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        # places pawns at row 1 and 6
        # places other pieces at row 0 and 7

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

