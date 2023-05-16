from typing import List

from solid_games.models import Box

from ....models import Box
from ..types import ChessPieceEnum
from .chess_pice import ChessPiece
from .color import Color


class King(ChessPiece):
    in_check: bool
    firts_move = bool = False

    def __init__(self, color: Color, in_check: bool = False) -> None:
        super().__init__(ChessPieceEnum.KING, color=color)
        self.in_check = in_check

    def check_move(cls, pos_x: str, pos_y: str) -> bool:
        return super().check_move(pos_x, pos_y)

    def move(cls, pos_x: str, pos_y: str):
        pass

    def load_allow_boxes(cls, board: List[Box]):
        super().load_allow_boxes(board)

        allowed_boxes = []

        for box in cls.allowed_boxes:
            distance_x = abs(cls.pos_x - box.pos_x)
            distance_y = abs(cls.pos_y - box.pos_y)

            if distance_x == 1 or distance_y == 1:
                allowed_boxes.append(box)

        cls.allowed_boxes = allowed_boxes
