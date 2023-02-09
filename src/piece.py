import os

from numpy import inf
from dataclasses import dataclass, field


@dataclass
class Piece:
    # param: value are the values of each piece and is later used for ai to play against

    name: str = field(default=str)
    color: str = field(default=str)
    value: float = field(default=float)

    moves: list = field(default_factory=list)
    moved: bool = field(default=False)

    texture: str = field(default=None, init=False)
    texture_rect: str = field(default=None, init=False)

    def __post_init__(self):
        # for the ai to make a distinction between the colors
        value_sign = 1 if self.color == 'white' else -1
        self.value = self.value * value_sign

        self.set_texture()

    # adding image to piece
    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )

    # tracks every move
    def add_moves(self, move):
        self.moves.append(move)


@dataclass
class Pawn(Piece):
    name: str = 'pawn'
    value: int = 1.0

    direction: int = field(init=False)

    def __post_init__(self):
        self.direction = -1 if self.color == 'white' else 1
        super().__post_init__()


@dataclass
class Knight(Piece):
    name: str = 'knight'
    value: int = 3.0

    def __post_init__(self):
        super().__post_init__()


@dataclass
class Bishop(Piece):
    name: str = 'bishop'
    value: int = 3.001

    def __post_init__(self):
        super().__post_init__()


@dataclass
class Rook(Piece):
    name: str = 'rook'
    value: int = 5.0

    def __post_init__(self):
        super().__post_init__()


@dataclass
class Queen(Piece):
    name: str = 'queen'
    value: int = 9.0

    def __post_init__(self):
        super().__post_init__()


@dataclass
class King(Piece):
    name: str = 'king'
    value: int = inf

    def __post_init__(self):
        super().__post_init__()
