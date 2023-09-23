from Design_patterns.TicTacToe.model.playing_piece import PlayingPiece


class PlayingPieceX(PlayingPiece):
    def __init__(self, PieceType):
        super().__init__(PieceType.X)
