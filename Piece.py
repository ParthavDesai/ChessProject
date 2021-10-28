class PieceInterface:
    def getPositions(self) -> List:
        pass

    def getTeam(self) -> str:
        pass
    #dead or alive
    def getStatus(self) -> bool:
        pass
    
    def move(self) -> None:
        pass

    def isAllowed(self, *positions) -> bool:
        pass

    def getPieceType(self) -> str:
        pass
