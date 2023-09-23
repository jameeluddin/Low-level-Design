from collections import deque

from Design_patterns.TicTacToe.model.board import Board
from Design_patterns.TicTacToe.model.piece_type import PieceType
from Design_patterns.TicTacToe.model.player import Player
from Design_patterns.TicTacToe.model.playing_piece import PlayingPiece
from Design_patterns.TicTacToe.model.playing_piece_o import PlayingPieceO
from Design_patterns.TicTacToe.model.playing_piece_x import PlayingPieceX


class Game:
    def __init__(self):
        self.game_board = None
        self.players = deque()
        self.initialize_game()
        self.winner = False

    def initialize_game(self):
        # crossPiece = PlayingPiece(PieceType)
        PlayingPiece.X = "X"
        PlayingPiece.O= "O"
        player1 = Player("Player1", PlayingPiece.X)
        player2 = Player("Player2", PlayingPiece.O)

        self.players.append(player1)
        self.players.append(player2)

        self.game_board = Board(3)

    def start_game(self):

        while not self.winner:
            player_turn = self.players.popleft()
            self.game_board.print_board()
            freeSpaces = self.game_board.get_free_cells()

            if len(freeSpaces) == 0:
                self.winner = True
                continue

            print("Player:" + player_turn.name + " Enter row,column: ", end=" ")
            ip = input()
            values = ip.split(",")
            ip_row = values[0]
            ip_col = values[1]

            print("player_turn", player_turn)
            print("player_turn.playing_piece", player_turn.playing_piece)

            piece_added_successfully = self.game_board.add_piece(int(ip_row), int(ip_col), player_turn.playing_piece)
            if not piece_added_successfully:
                print("Incorrect position chosen, try again")
                self.players.appendleft(player_turn)
                continue

            self.players.append(player_turn)

            winner = self.is_there_winner(int(ip_row), int(ip_col), player_turn.playing_piece)
            if winner:
                return player_turn.name

    def is_there_winner(self, ip_row, ip_col, piece_type):
        row_match = True
        column_match = True
        diagonal_match = True
        anti_diagonal_match = True

        for i in range(self.game_board.size):
            if self.game_board.board[ip_row][i] is None or self.game_board.board[ip_row][i] != piece_type:
                row_match = False

        for i in range(self.game_board.size):
            if self.game_board.board[i][ip_col] is None or self.game_board.board[i][ip_col] != piece_type:
                column_match = False
        j = 0
        for i in range(self.game_board.size):
            if self.game_board.board[i][j] is None or self.game_board.board[i][j] != piece_type:
                diagonal_match = False
            j += 1

        j = self.game_board.size - 1
        for i in range(self.game_board.size):
            if self.game_board.board[i][j] is None or self.game_board.board[i][j] != piece_type:
                anti_diagonal_match = False
            j -= 1

        return row_match or column_match or diagonal_match or anti_diagonal_match
