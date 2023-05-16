from copy import copy
from typing import List
from ...models import Box, Game, Transaction
from .pieces import Bishop, Color, King, Knight, Pawn, Qeen, Rook, ChessPiece

PIECE_MAP: List[ChessPiece] = [
    Rook(Color.BLACK),
    Knight(Color.BLACK),
    Bishop(Color.BLACK),
    Qeen(Color.BLACK),
    King(Color.BLACK),
    Bishop(Color.BLACK),
    Knight(Color.BLACK),
    Rook(Color.BLACK),
]


class Chess(Game):
    def make_move(self, move: Transaction):
        return super().make_move(move)

    def init_game(self):
        return super().init_game()

    def finsh_game(self):
        return super().finsh_game()

    def load_board(self):
        for x in range(0, 8):
            for y in range(0, 8):
                piece = None
                
                if y == 0 or y == 7:
                    
                    piece = copy(PIECE_MAP[x])

                    if y == 7:
                        piece.color = Color.WHITE

                elif y == 1 or y == 6:
                    piece = Pawn(Color.WHITE if y == 6 else Color.BLACK)                

                if piece:
                    piece.set_pos_xy(x,y)

                self.board.append(Box(x, y, piece=piece))

    def check_win(self) -> bool:
        return super().check_win()

    def play(self):
        x, y = input(
            f"Player {self.shift.get_nickname()} enter a transaction x,y: "
        ).split(",")

        # self.make_move(Transaction(self.shift, int(x), int(y), piece))
