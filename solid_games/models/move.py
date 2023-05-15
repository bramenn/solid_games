import uuid
from datetime import datetime

from .piece import Piece
from .player import Player


class Move:
    id: str

    date: datetime

    player: Player
    piece: Piece

    def __init__(self, player: Player, pos_x: str, pos_y: str, piece: Piece) -> None:
        self.id = uuid.uuid4()
        self.date = datetime.now()
        self.player = player
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.piece = piece
