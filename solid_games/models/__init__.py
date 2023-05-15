from typing import Union

from .display import DisplayUI
from ..games import ChessPieceEnum, TicTacToe, TicTacToePieceEnum, TicTacToeDisplay
from .move import Move
from .player import Player

TypePice = Union[TicTacToePieceEnum, ChessPieceEnum]
