from .base import PieceError


class BoxFilled(PieceError):
    def __init__(self, message: str = "The box is already occupie") -> None:
        super().__init__(message)


class BoxDoesNotExist(PieceError):
    def __init__(self, message: str = "The box does not exist") -> None:
        super().__init__(message)
