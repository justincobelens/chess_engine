import pygame
from dataclasses import dataclass, field

from const import *


@dataclass
class Dragger:
    # TODO
    # fix this type
    piece: any = field(default=0)
    dragging: bool = field(default=False)

    mouseX: int = field(default=0)
    mouseY: int = field(default=0)

    initial_row: int = field(default=0)
    initial_col: int = field(default=0)

    def update_blit(self, surface):
        pass

    def update_mouse(self, pos: tuple[int, int]):
        self.mouseX, self.mouseY = pos  # (xcor, ycor)

    def save_initial(self, pos: tuple[int, int]):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False
