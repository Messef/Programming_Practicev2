myMove = input = ("piece and move:")
counter = 0
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
initial_state = [
        ['r1w', 'nw', 'bw', 'qw', 'kw', 'bw', 'nw', 'r2w'],
        ['pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb'],
        ['r1b', 'nb', 'bb', 'qb', 'kb', 'bb', 'nb', 'r2b']
        ]
state = [
        ['rw', 'nw', 'bw', 'qw', 'kw', 'bw', 'nw', 'rw'],
        ['pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw', 'pw'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb', 'pb'],
        ['rb', 'nb', 'bb', 'qb', 'kb', 'bb', 'nb', 'rb']
        ]
class Board:
    def __init__(self, initial_state, state):
        self.initial_state = initial_state
        self.state = state 
    def get_state(self):
        return self.initial_state
    def coordState(self):
        pass
    
myBoard = Board(initial_state, state)
class King: 
    def __init__(self, color, coordinate, rawcoordinate, wantMove):
        self.color = color
        self.coord = coordinate
        self.rawCoord = rawcoordinate
        self.wantMove = wantMove
    def get_coord(self):
        myCoord = f"k{self.color}"
        print(myCoord)
        for x, y in enumerate(myBoard.state):
            print(y)
            for z, a in enumerate(y):
                if myBoard.state[x][z] == myCoord:
                    self.coord = files[z+1]+str(x+1)
                    self.rawCoord = [z+1, x+1]
                    break
        return self.coord
    def valid_move(self):
        pass
                   


myKing = King("w", "no coord found", "no coord found", "e2")

print(myKing.get_coord())