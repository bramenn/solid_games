from abc import abstractmethod
from enum import Enum
from typing import List

from ....models import Box, MovaiblePiece
from .error import KingInCheckError, PieceWithOutMoves
from .color import Color


class ChessPiece(MovaiblePiece):
    is_king_check: bool
    allowed_boxes: List[Box]
    color: Color

    def __init__(
        self,
        _type: Enum = None,
        color: Color = None,
    ) -> None:
        super().__init__(_type)
        self.is_king_check = False

        if _type:
            self.color = color

    def move(cls, pos_x: str, pos_y: str):
        return super().move(pos_x, pos_y)

    def check_move(cls, pos_x: str, pos_y: str, board: List[Box]) -> bool:
        if cls.is_king_check:
            raise KingInCheckError()

        cls.load_allow_boxes(board=board)

        if cls.allowed_boxes < 1:
            raise PieceWithOutMoves()

    def load_empty_box(self, board: List[Box]):
        empty_boxs = []

        for box in board:
            if not box.piece:
                continue

            empty_boxs.append(box)

        return empty_boxs
    
    def get_name(self):
        return self.name if self.color == Color.BLACK else self.name.lower()

    @abstractmethod
    def load_allow_boxes(cls, board: List[Box]):
        cls.allowed_boxes = cls.load_empty_box(board=board)
