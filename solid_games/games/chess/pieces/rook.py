from ..types import ChessPieceEnum
from .chess_pice import ChessPiece
from .color import Color


class Rook(ChessPiece):
    def __init__(self, color: Color) -> None:
        super().__init__(ChessPieceEnum.ROOK, color)

    def check_move(cls, pos_x: str, pos_y: str) -> bool:
        return super().check_move(pos_x, pos_y)

    def move(cls, pos_x: str, pos_y: str):
        pass
