from .piece import Piece


class Box:
    pos_x: int
    pos_y: int

    piece: Piece

    def __init__(self, pos_x: int, pos_y: int, piece: Piece = None) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.piece = piece

    def get_piece(self) -> Piece:
        return self.piece

    def set_piece(self, piece: Piece):
        self.piece = piece

    @property
    def is_vailable(self) -> bool:
        return not bool(self.piece if self.piece and self.piece.name != "_" else False)

    def __str__(self) -> str:
        return f"\t({self.pos_x},{self.pos_y})[{self.piece.get_name() if self.piece else '_'}]"
