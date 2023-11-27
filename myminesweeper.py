import time
import random
class Game(): 
    def __init__(self, difficulty = 1, board = [], guess = 1, flag = False, minesLocation = [], showBoard = [], cor = 0):
        self.board = board
        self.difficulty = difficulty
        self.guess = guess
        self.flag = flag
        self.minesLocation = minesLocation
        self.showBoard = showBoard
        self.cor = cor
    def generator(self):
        if self.difficulty == 1: 
            for x in range(8):
                for y in range(8):
                    self.board.append(0)
                    self.showBoard.append(' ')

            while len(set(self.minesLocation)) < 10:
                myInt = random.randint(0, 63)
                self.board[myInt] = "m"
                self.minesLocation.append(myInt)

        elif self.difficulty == 2:
            for x in range(16):
                for y in range(16):
                    self.board.append(0)
                    self.showBoard.append(' ')
            while len(set(self.minesLocation))<40:

                myInt = random.randint(0, 255)
                self.board[myInt] = "m"
                self.minesLocation.append(myInt)

        else: 
            for x in range(16):
                for y in range (30):
                    self.board.append(0)
                    self.showBoard.append(' ')
            while len(set(self.minesLocation))<100:
                myInt = random.randint(0, 479)
                self.board[myInt] = "m"
                self.minesLocation.append(myInt)
                
        self.minesLocation = set(self.minesLocation)
        self.minesLocation = sorted(self.minesLocation)
        self.numberGenerator()

    def numberGenerator(self):
      if self.difficulty == 1:
        for x in self.minesLocation:
            store_x = x
            for i in (-9, -8, -7, -1, 1, 7, 8, 9):
                x = store_x
                if (x%8 == 0 and (i == -1 or i == 7 or i == -9)) or ((x-7)%8 == 0 and (i==1 or i == -7 or i ==9)):
                    continue
                x+=i
                if x < 0 or x >= len(self.board):
                    continue
                if type(self.board[x]) == str:
                    continue
                self.board[x]+=1
      elif self.difficulty == 2:
          for x in self.minesLocation:
              store_x = x
              for i in (-17,-16, -15, 1, -1, 15, 16, 17):
                x = store_x
                if (x%16 == 0 and (i == -1 or i == 15 or i == -17)) or ((x-15)%16 == 0 and (i==1 or i == -15 or i ==17)):
                    continue
                x+=i
                if x < 0 or x >= len(self.board):
                    continue
                if type(self.board[x]) == str:
                    continue
                self.board[x]+=1
      else: 
          for x in self.minesLocation:
              store_x = x
              for i in (-31,-30, -29, -1, 1, 29, 30, 31):
                x = store_x
                if (x%30 == 0 and (i == -1 or i == 29 or i == -31)) or ((x-29)%30 == 0 and (i==1 or i == -29 or i ==31)):
                    continue
                x+=i
                if x < 0 or x >= len(self.board):
                    continue
                if type(self.board[x]) == str:
                    continue
                #print(i, store_x, x)
                self.board[x]+=1

      #print(self.minesLocation)
        
    def guessHandler(self):
        #self.displayBoard()
        self.takeGuess()
        self.displayBoard()
        if self.flag == True:
            self.showBoard[self.guess] = "f"
            return None
        
        elif self.cor == (len(self.board) - len(self.minesLocation)):
            return True
        else:
            if self.board[self.guess] == "m":
                print("you lose!")
                print(self.board)
                return False
            else:
                print("ok, good guess")
                self.showBoard[self.guess] = self.board[self.guess]
                return None
        
    def displayBoard(self):
        rep = ''
        if self.difficulty == 1:
            for i in range(8):
                for x in range(8):
                    rep+=f"| {self.showBoard[(i*8)+x]} |"
                    if x==7: rep+="\n"
        elif self.difficulty == 2:
            rep+="\n"
            for i in range(16):
                for x in range(16):
                    rep+=f"| {self.showBoard[(i*16)+x]} |"
            #rep+=f"| {i*16+x} |"
        else:
            for i in range(16):
                for x in range(30):
                    rep+=f"|{self.showBoard[(i*30)+x]}|"
            #rep+=f"| {i*16+x} |"
            rep+="\n"
        print(rep)
    def takeGuess(self):
        if self.difficulty == 1:
            between = "1 - 64"
        elif self.difficulty == 2:
            between = "1 - 256"
        else:
            between = "1 - 480"
        self.guess = input(f"Enter a guess between {between} or type f, which stands for flag, and then your guess(like f4): ")
        try:
            self.guess = int(self.guess)
        except ValueError:
            self.guess = self.guess[1:]
            self.guess = int(self.guess)
            self.guess-=1
            self.flag = True

        else:
            self.guess-=1
            self.flag = False
    


myGame = Game()
myGame.generator()
result = myGame.guessHandler()
rep = ''
myGame.takeGuess()
while result == None:
    myGame.takeGuess()
if result == True: print('you win')
else: print('lol')



