moveCounter = 0 
files = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h'

}
revFiles = {
   'a':  1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8 

}
initial_state = [
        ['rw', 'nw', 'bw', 'qw', 'kw', 'bw', 'nw', 'rw'],
        ['pwa', 'pwb', 'pwc', 'pwd', 'pwe', 'pwf', 'pwg', 'pwh'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['pba', 'pbb', 'pbc', 'pbd', 'pbe', 'pbf', 'pbg', 'pbh'],
        ['rb', 'nb', 'bb', 'qb', 'kb', 'bb', 'nb', 'rb']
        ]
state = [
        ['rw', 'nw', 'bw', 'qw', 'kw', 'bw', 'nw', 'rw'],
        ['pwa', 'pwb', 'pwc', 'pwd', 'pwe', 'pwf', 'pwg', 'pwh'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['pba', 'pbb', 'pbc', 'pbd', 'pbe', 'pbf', 'pbg', 'pbh'],
        ['rb', 'nb', 'bb', 'qb', 'kb', 'bb', 'nb', 'rb']
        ]
class Board:
    def __init__(self, initial_state, state):
        self.initial_state = initial_state
        self.state = state 
    def get_state(self):
        return self.state
    def coordState(self):
        pass

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
    def change_state(self):
        if King.valid_move(self)== True:
            myBoard.state[revFiles[self.wantMove[0]]-1][self.wantMove[1]-1]
            return "y"
        return "n"
myBoard = Board(initial_state, state)


                   


myKing = King("b", "no coord found", "no coord found", ["e", 8])
myPawn = Pawn("w", "e", "no coord found", "no coord found",["e", 4], True)
print(myKing.get_coord())
print(myKing.valid_move())
print(myKing.change_state())
print(myPawn.get_coord())
print(myPawn.valid_move())
print(myPawn.change_state())