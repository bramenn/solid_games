from .....models import PieceError


class KingInCheckError(PieceError):
    def __init__(self, message: str = "The king is in check") -> None:
        super().__init__(message)


class PieceWithOutMoves(PieceError):
    def __init__(self, message: str = "The piece has no moves") -> None:
        super().__init__(message)
