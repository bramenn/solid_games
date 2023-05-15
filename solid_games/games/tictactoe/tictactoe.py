from typing import List

from ...models.move import Move

from ...models.box import Box
from ...models.game import Game
from .pieces import Piece
from .types import TicTacToePieceEnum


class TicTacToe(Game):
    def play(self):
        x, y = input(f"Player {self.shift.nickname} enter a transaction x,y: ").split(
            ","
        )

        piece = (
            Piece(TicTacToePieceEnum.X)
            if self.shift.is_host
            else Piece(TicTacToePieceEnum.O)
        )

        self.make_move(Move(self.shift, int(x), int(y), piece))

    def init_game(self):
        super().init_game()

    def get_diagonal_a(self):
        box_1 = self.get_box_by_xy(0, 0)
        box_2 = self.get_box_by_xy(1, 1)
        box_3 = self.get_box_by_xy(2, 2)

        return [box_1, box_2, box_3]

    def get_diagonal_b(self):
        box_1 = self.get_box_by_xy(0, 2)
        box_2 = self.get_box_by_xy(1, 1)
        box_3 = self.get_box_by_xy(2, 0)

        return [box_1, box_2, box_3]

    def load_board(self):
        for x in range(0, 3):
            for y in range(0, 3):
                self.board.append(Box(x, y))

    def check_list(self, boxes: List[Box]) -> bool:
        boalean_list = []

        for box in boxes:
            if box.get_piece() is None:
                return False

            print(box)
            boalean_list.append(box.get_piece().get_name())

        return len(set(boalean_list)) == 1

    def check_win(self) -> bool:
        for index in range(0, 3):
            # Win with a row
            if self.check_list(self.get_raw_board_by_index(index)):
                return True
            # Win with a column
            elif self.check_list(self.get_column_board_by_index(index)):
                return True
            # Win with diagonal left_down
            elif self.check_list(self.get_diagonal_a()):
                return True
            # Win with diagonal left_up
            elif self.check_list(self.get_diagonal_b()):
                return True

        return False

    def make_move(self, move: Move):
        return super().make_move(move)
