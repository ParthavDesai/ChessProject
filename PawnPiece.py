from Piece.py import Piece


class PawnPiece(Piece):

    def __init__(self,team,pieceType,status):
        self.team = team
        self.pieceType = "Pawn"
        self.status = status

    def getStatus(self):
        return self.status
    def getTeam(self):
        return self.team
    def getPieceType(self):
        return self.pieceType