from abc import ABC, abstractmethod

from .game import Game


class DisplayUI(ABC):
    game: Game

    def __init__(self, game: Game) -> None:
        self.game = game

    @abstractmethod
    def show_board(self):
        pass

    def show_players(self):
        print(
            f"""
                Player # 1: {self.game.player_1.nickname}\t {self.game.player_1.points}
                Player # 2: {self.game.player_2.nickname}\t {self.game.player_1.points}
            """
        )

    def show_game(self):
        print(
            f"""
                Game ID: {self.game.id}
                Creation: {self.game.created}
                Shift: {self.game.shift.nickname}
                # moves: {len(self.game.moves)}
            """
        )
        self.show_board()
