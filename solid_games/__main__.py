import random
from typing import Any, Tuple, Union

from .models import DisplayUI, Player, TicTacToe, TicTacToeDisplay

Game = Union[TicTacToe, Any]


class Program:
    @staticmethod
    def play_tictactoe(
        player_1: Player, player_2: Player
    ) -> Tuple[TicTacToe, TicTacToeDisplay]:
        test_game = TicTacToe(player_1=player_1, player_2=player_2)
        display = TicTacToeDisplay(game=test_game)
        return test_game, display

    @staticmethod
    def run():
        player_1 = Player("bramen")
        player_2 = Player("chelo")

        if random.randint(0, 1):
            player_1.is_host = True
        else:
            player_2.is_host = True

        test_game, display = Program.play_tictactoe(player_1, player_2)

        test_game.init_game()
        Program.play(game=test_game, display=display)

    @staticmethod
    def play(game: Game, display: DisplayUI):
        while True:
            display.show_game()
            game.play()
            if game.winner:
                break

        display.show_board()


Program.run()
