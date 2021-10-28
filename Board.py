
class Board:
    def __init__(self) -> None:
        self.board = [8][8]

    def createBoard(self):
        for i in range(8):
            self.board[1][i] = "Black pawn"
