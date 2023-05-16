from ....models.display import DisplayUI


class ChessDisplay(DisplayUI):
    def show_board(self):
        board_str = "\n"
        for box_raw_index in range(0, 8):
            for box in self.game.get_raw_board_by_index(box_raw_index):
                board_str += box.__str__()
            board_str += "\n"

        print(board_str)
