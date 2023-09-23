from Design_patterns.TicTacToe.model.piece_type import PieceType
from Design_patterns.TicTacToe.model.playing_piece import PlayingPiece


class PlayingPieceO(PlayingPiece):
    def __init__(self, PieceType):
        super().__init__(PieceType.O)