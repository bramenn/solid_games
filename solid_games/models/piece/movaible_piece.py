from abc import abstractmethod

from .error import PieceError
from .piece import Piece


class MovaiblePiece(Piece):
    @abstractmethod
    def move(cls, pos_x: str, pos_y: str):
        print(
            f"The {cls.get_name()} will try to put himself in the box: {pos_x, pos_y}"
        )

        try:
            cls.check_move(pos_x=pos_x, pos_y=pos_y)
        except PieceError as e:
            print(e)

    @abstractmethod
    def check_move(cls, pos_x: str, pos_y: str) -> bool:
        pass
