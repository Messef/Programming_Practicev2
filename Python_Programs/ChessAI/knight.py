from board import *

class Knight:
    def __init__(self, color, side, rawcoordinate, wantMove, moves):
        self.color = color
        self.side = side
        self.rawCoord = rawcoordinate
        self.wantMove = wantMove
        self.moves = True
    def get_coord(self):
        myCoord = f"n{self.color}{self.side}"
        for x, y in enumerate(myBoard.state):
            for z, a in enumerate(y):
                if myBoard.state[x][z] == myCoord:
                    self.rawCoord = [z, x]
                    break
        return  self.rawCoord
    def valid_move(self):
        self.get_coord()
        print(self.rawCoord)
        selfFile = self.rawCoord[0]
        selfRank = self.rawCoord[1]
        validFile = revFiles[self.wantMove[0]]-1
        validRank = self.wantMove[1]-1
        print(validFile, validRank)
        bool1 =  (abs(validFile-selfFile)==2 and abs(validRank-selfRank)==1) 
        bool2 = (abs(validFile-selfFile) == 1 and abs(validRank-selfRank) == 2) 
        if (bool1 or bool2 and myBoard.state[validRank][validFile][0] != self.color):
            return True
        return False, selfFile, selfRank, validFile, validRank, myBoard.state[validRank][validFile]
    def change_state(self):
        self.valid_move()
        selfFile = self.rawCoord[0]
        selfRank = self.rawCoord[1]
        validFile = revFiles[self.wantMove[0]]-1
        validRank = self.wantMove[1]-1
        if self.valid_move()== True:
            myBoard.state[validRank][validFile] = f"n{self.side}{self.color}"
            myBoard.state[selfRank][selfFile] = "es"

            return myBoard.state, True
        return False, "change"
BlackQKnight = Knight("b", "q", ["g", 8], ["c", 6], True)
WhiteKKnight = Knight("w", "k", "no coord found", ["f",3], True)
print(BlackQKnight.change_state())
print(myBoard.state)
print(BlackQKnight.get_coord())
BlackQKnight.wantMove = ["d", 4]
print(BlackQKnight.change_state())
#print(WhiteKKnight.change_state())
'''WhiteKKnight.wantMove = ["d", 4]
print(WhiteKKnight.rawCoord)
print(WhiteKKnight.change_state())'''
