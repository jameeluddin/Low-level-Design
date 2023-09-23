from Design_patterns.TicTacToe.model.playing_piece import PlayingPiece


class Board:
    def __init__(self, size):
        self.size = size
        self.board =  [[None for i in range(size)] for j in range(size)]

    def add_piece(self, row, col, playing_piece):
        if self.board[row][col]:
            return False

        self.board[row][col] = playing_piece
        return True

    def get_free_cells(self):
        free_cells = [[(i,j) for j in range(self.size)] for i in range(self.size)]
        return free_cells

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]:
                    # print("self.board[i][j]", self.board[i][j])
                    print(f"{self.board[i][j]}    ", end=" ")
                else:
                    print(" | ", end=" ")
            print()









