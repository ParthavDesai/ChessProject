from Piece.py import Piece


class QueenPiece(Piece):

    def __init__(self,team,pieceType,status):
        self.team = team
        self.pieceType = "Queen"
        self.status = status

    def getStatus(self):
        return self.status
    def getTeam(self):
        return self.team
    def getPieceType(self):
        return self.pieceType