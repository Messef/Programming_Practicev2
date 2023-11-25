import time
import math
from Python_Programs.TicTacToe.myplayer import *
class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.current_winner = None

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
    def empty_squares(self): 
        return ' ' in self.board
    def get_winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False
        '''col_num = square
        store_square = square
        while (square>0): 
            square -= 3
        square = store_square
        checkList = []
        checkList.append(self.board[col_num])
        checkList.append(self.board[col_num + 3])
        checkList.append(self.board[col_num + 6])
        MY WAY ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
        '''
        col_num = square % 3
        myCol = [self.board[col_num+i * 3] for i in range(3)]
        if all(spot == letter for spot in myCol): #checks if there is one letter in a column, the "all" keyword checks to see if everything is true
            return True, "column"
        
        #Diagonal?
        if square % 2 == 0:
            diag1 = [self.board[i] for i in range(0, 4, 8)]
            if all([spot == letter for spot in diag1]):
                
                return True, "diagonal1", diag1, self.board
            #diag2 = [self.board[i] for i in range(2, 4, 6)]
            diag2 = []
            for i in range(2, 4, 6):
                diag2.append(self.board[i])
                
            if all([spot == letter for spot in diag2]):
                return True, "diagonal2", diag2, self.board
            
        return False my CODE^^^^^^^^^^^^^^^^^^^^^^^^'''
    def available_moves(self): 
        return (x for x, y in enumerate(self.board) if y == ' ')
    def num_empty_squares(self):
        # return len(self.available_moves) -->Generator cannot be counted in length
        return self.board.count(" ")# is the best
    '''def make_move(self, player): 
        return self.board[player.get_move] == player.letter --> My code'''
    def make_move(self, square, letter):
        #print(square, type(square))
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.get_winner(square, letter):
                self.current_winner = letter
            return True
        return False

def game(game, x_player, o_player, print_game = True):
    if print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
            letter == "X"
        else:
            square = x_player.get_move(game)
            letter == "O"
        #print(square, type(square)) <--- This one was to debug the thing
        if game.make_move(square, letter): 
            if print_game: 
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("\n")
            if game.current_winner:
                if print_game: 
                    print(letter + " wins!")
                    print(game.get_winner(square, letter))
                return letter
            letter = 'O' if letter == 'X' else "X"
        if print_game==True:
            #time.sleep(2)
            pass
    if print_game:
            print("It's a tie!!")
if __name__ == '__main__':
    otherCompPlayer = RandomComputer("O")
    x_wins = 0
    o_wins = 0
    ties = 0
    compPlayer = MyComputerPlayer("X")
    t = TicTacToe()
    for i in range(1000):
        result = game(t, otherCompPlayer, compPlayer, print_game = False)
        if result == "X":
         x_wins+=1
        elif result == "O":
            o_wins+=1
        else:
            ties+=1
    print(f"\n My computer won {o_wins} times and the other computer won {x_wins} times. There were {ties} ties\n")
    

