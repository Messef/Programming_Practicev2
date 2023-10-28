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
        ['rw', 'nwq', 'bw', 'qw', 'kw', 'bw', 'nwq', 'rw'],
        ['pwa', 'pwb', 'pwc', 'pwd', 'pwe', 'pwf', 'pwg', 'pwh'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['pba', 'pbb', 'pbc', 'pbd', 'pbe', 'pbf', 'pbg', 'pbh'],
        ['rb', 'nbq', 'bb', 'qb', 'kb', 'bb', 'nbk', 'rb']
        ]
state = [
        ['rw', 'nwq', 'bw', 'qw', 'kw', 'bw', 'nwq', 'rw'],
        ['pwa', 'pwb', 'pwc', 'pwd', 'pwe', 'pwf', 'pwg', 'pwh'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
        ['pba', 'pbb', 'pbc', 'pbd', 'pbe', 'pbf', 'pbg', 'pbh'],
        ['rb', 'nbq', 'bb', 'qb', 'kb', 'bb', 'nbk', 'rb']
        ]
class Board:
    def __init__(self, initial_state, state):
        self.initial_state = initial_state
        self.state = state 
    def get_state(self):
        return self.state
    def coordState(self):
        pass
myBoard = Board(initial_state, state)
