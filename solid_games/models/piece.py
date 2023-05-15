from enum import Enum
from typing import Any


class Piece:
    name: str
    type: Any
    pos_x: str
    pos_y: str

    def __init__(self, _type: Enum = None) -> None:
        self.type = _type
        self.name = _type.name if _type else "_"

    def set_type(self, _type: Any):
        self.type = _type

    def get_name(self):
        return self.name

    def set_pos_xy(self, pos_x: str, pos_y: str):
        self.pos_x = pos_x
        self.pos_y = pos_y
