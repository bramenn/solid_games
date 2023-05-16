import uuid
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from .box import Box
from .player import Player
from .transaction import Transaction


class Game(ABC):
    id: str

    created: datetime
    finished: datetime

    player_1: Player
    player_2: Player

    winner: Player

    board: List[Box]

    shift: Player

    moves: List[Transaction]

    def __init__(self, player_1: Player, player_2: Player) -> None:
        self.id = uuid.uuid4()
        self.created = datetime.now()
        self.player_1 = player_1
        self.player_2 = player_2
        self.board = []
        self.moves = []
        self.winner = None

    @property
    def dimension(self) -> int:
        return len(self.board) / 2

    def get_box_by_xy(self, x: int, y: int) -> Box | None:
        for box in self.board:
            if box.pos_x == x and box.pos_y == y:
                return box

    def get_raw_board_by_index(self, index: int) -> List[Box]:
        raw = []

        for box in self.board:
            if index == box.pos_y:
                raw.append(box)
        return raw

    def get_column_board_by_index(self, index: int) -> List[Box]:
        column = []
        for box in self.board:
            if index == box.pos_x:
                column.append(box)
        return column

    def check_move(self, move: Transaction) -> bool:
        box = self.get_box_by_xy(move.pos_x, move.pos_y)
        if move.player != self.shift:
            print(f"It is NOT your turn {move.player.get_nickname()}")
            return False
        elif (
            move.pos_x > self.dimension
            or move.pos_y > self.dimension
            or move.pos_x < 0
            or move.pos_y < 0
        ):
            print(f"This box does not exist")
            return False
        elif not box.is_vailable:
            print(f"This box is already filled")
            return False
        return True

    def register_move(self, move: Transaction):
        self.moves.append(move)

    def register_posints(self):
        self.shift.points += 1

    def change_shift(self):
        if self.shift == self.player_1:
            self.shift = self.player_2
        else:
            self.shift = self.player_1

    def init_shift(self):
        self.shift = self.player_1 if self.player_1.is_host else self.player_2

    @abstractmethod
    def make_move(self, move: Transaction):
        if not self.check_move(move):
            return

        box = self.get_box_by_xy(move.pos_x, move.pos_y)
        box.set_piece(piece=move.piece)

        if self.check_win():
            self.finsh_game()

        self.change_shift()
        self.register_move(move)

    @abstractmethod
    def init_game(self):
        self.load_board()
        self.init_shift()

    @abstractmethod
    def finsh_game(self):
        print(f"{self.shift.get_nickname()} You win!")
        self.shift.add_points(1)
        self.winner = self.shift
        self.finished = datetime.now()

    @abstractmethod
    def load_board(self):
        pass

    @abstractmethod
    def check_win(self) -> bool:
        pass

    @abstractmethod
    def play(self):
        pass
