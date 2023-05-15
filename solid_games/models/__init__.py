from typing import Union

from ..games import (ChessPieceEnum, TicTacToe, TicTacToeDisplay,
                     TicTacToePieceEnum)
from .display import DisplayUI
from .move import Move
from .player import Player

TypePice = Union[TicTacToePieceEnum, ChessPieceEnum]
