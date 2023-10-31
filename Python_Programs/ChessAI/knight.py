from board import *
class Knight:
    def __init__(self, color, side, coordinate, rawcoordinate, wantMove):
        self.color = color
        self.side = side
        self.coord = coordinate
        self.rawCoord = rawcoordinate
        self.wantMove = wantMove
    def get_coord(self):
        myCoord = f"n{self.color}{self.side}"
        for x, y in enumerate(myBoard.state):
            for z, a in enumerate(y):
                if myBoard.state[x][z] == myCoord:
                    self.coord = files[z+1]+str(x+1)
                    self.rawCoord = [z, x]
                    break
        return self.coord, self.rawCoord
    def valid_move(self):
        self.get_coord()
        selfFile = self.rawCoord[0]
        selfRank = self.rawCoord[1]
        validFile = revFiles[self.wantMove[0]]-1
        validRank = self.wantMove[1]-1

        bool1 =  (abs(validFile-selfFile)==2 and abs(validRank-selfRank)==1) 
        bool2 = (abs(validFile-selfFile) == 1 and abs(validRank-selfRank) == 2) 
        if (bool1 or bool2 and myBoard.state[validRank][validFile] == "e"):
            return True
        return False, selfFile, selfRank, validFile, validRank, myBoard.state[validRank][validFile]
    def change_state(self):
        self.valid_move()
        selfFile = self.rawCoord[0]
        selfRank = self.rawCoord[1]
        validFile = revFiles[self.wantMove[0]]-1
        validRank = self.wantMove[1]-1
        if Knight.valid_move(self)== True:
            myBoard.state[validRank][validFile] = f"n{self.side}{self.color}"
            myBoard.state[selfRank][selfFile] = "e"

            return myBoard.state, True
        return False
