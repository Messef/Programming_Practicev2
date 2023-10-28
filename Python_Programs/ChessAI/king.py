from board import *


class King: 
    def __init__(self, color, coordinate, rawcoordinate, wantMove):
        self.color = color
        self.coord = coordinate
        self.rawCoord = rawcoordinate
        self.wantMove = wantMove
    def get_coord(self):
        myCoord = f"k{self.color}"
        for x, y in enumerate(myBoard.state):
            for z, a in enumerate(y):
                if myBoard.state[x][z] == myCoord:
                    self.coord = files[z+1]+str(x+1)
                    self.rawCoord = [z+1, x+1]
                    break
        return self.coord, self.rawCoord
    def valid_move(self):
        selfFile = self.rawCoord[0]
        selfRank = self.rawCoord[1]
        validFile = revFiles[self.wantMove[0]]
        validRank = self.wantMove[1]
        bool1 =  (abs(validFile-selfFile)==1 and abs(validRank-selfRank)==0) 
        bool2 = (abs(validFile-selfFile) == 0 and abs(validRank-selfRank) == 1) 
        bool3 = (abs(validFile-selfFile) == 1 and abs(validRank-selfRank) == 1)
        if (bool1 or bool2 or bool3) and myBoard.state[validRank-1][validFile-1] == "e":
            return myBoard.state
        return "cannot move there"

WhiteKing = King("b", "no coord found", "no coord found", ["e", 8])

