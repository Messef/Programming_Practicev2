class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in range(3):
            print("| " + " | \n")

    @staticmethod #The next function doesn't have the 'self' parameter
    def print_board_nums():
       numbered_board = []
       for j in range(3):
        addon = [str(i) for i in range((j*3), (j+1)*3)]
        numbered_board+=addon
       print(numbered_board)
       for row in range(3):
            print(f"{numbered_board[row*3]} | " + f"{numbered_board[row*3+1]} | {numbered_board[row*3+2]} \n")
    def available_moves(self): 
        return (x for x, y in enumerate(self.board) if y == ' ')
myBoard = TicTacToe()
myBoard.print_board_nums()
#myBoard.print_board()
print(myBoard.available_moves())