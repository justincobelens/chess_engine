from dataclasses import dataclass, field
from piece import Piece


@dataclass
class Square:
    row: int
    col: int
    piece: Piece = field(default=None)

    def has_piece(self):
        return self.piece is not None
