from board import *
class Pawn:
    def __init__(self, color, file, coordinate, rawcoordinate, wantMove, moves):
        self.color = color
        self.file = file
        self.coord = coordinate
        self.rawCoord = rawcoordinate
        self.wantMove = wantMove
        self.moves = moves
    def get_coord(self):
        myCoord = f"p{self.color}{self.file}"
        for x, y in enumerate(myBoard.state):
            for z, a in enumerate(y):
                if myBoard.state[x][z] == myCoord:
                    self.coord = files[z+1]+str(x+1)
                    self.rawCoord = [z+1, x+1]
                    break
        return self.coord, self.rawCoord
    def valid_move(self):
        selfFile = self.rawCoord[0]-1
        selfRank = self.rawCoord[1]-1
        validFile = revFiles[self.wantMove[0]]-1
        validRank = self.wantMove[1]-1
        bool1 =  (abs(validFile-selfFile)==0 and abs(validRank-selfRank)==2 and self.moves) 
        bool2 = (abs(validFile-selfFile) == 0 and abs(validRank-selfRank) == 1) 
        bool3 = (abs(validFile-selfFile) == 1 and abs(validRank-selfRank) == 1)
        if (bool1 or bool2 or bool3) and myBoard.state[validRank][validFile] == "e":
            return True
        return "cannot move there"
    def change_state(self):
        self.get_coord()
        self.valid_move()
        selfFile = self.rawCoord[0]-1
        selfRank = self.rawCoord[1]-1
        validFile = revFiles[self.wantMove[0]]-1
        validRank = self.wantMove[1]-1
        if Pawn.valid_move(self)== True:
            myBoard.state[validRank][validFile] = f"p{self.color}{self.file}"
            myBoard.state[selfRank][selfFile] = "e"
            self.moves = False
            return myBoard.state

        return False

