import random
class Game(): 
    def __init__(self, difficulty = 3, board = [], guess = 1, flag = False, minesLocation = [], showBoard = [], cor = 0):
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
        #print("doneee")
        if self.flag == True:
            self.showBoard[self.guess] = "f"
            #print("here1")
            self.displayBoard()
            self.takeGuess()
            return None
        
        elif self.cor == (len(self.board) - len(self.minesLocation)):
            #print("here")
            self.realDisplay()
            return True
        else:
         try:
            if self.board[self.guess] == "m":
                #print("you lose!")
                self.realDisplay()
                #self.board[self.guess] = "    M     "
                return False
            elif self.showBoard[self.guess] != " " and self.showBoard[self.guess] != "f" :
             print(f"another num1 {self.showBoard[self.guess]}")
             self.takeGuess()
            else:
                #print("ok, good guess")
                self.showBoard[self.guess] = self.board[self.guess]
                self.displayBoard()
                self.cor+=1
                self.takeGuess()
                return None
            
         except IndexError:
             print("another num")
             self.takeGuess()
        
    def displayBoard(self):
        rep = ''
        if self.difficulty == 1:
            for i in range(8):
                for x in range(8):
                    rep+=f"| {self.showBoard[(i*8)+x]} |"
                    if x==7: rep+="\n"
        elif self.difficulty == 2:
            for i in range(16):
                rep+="\n"
                for x in range(16):
                    rep+=f"| {self.showBoard[(i*16)+x]} |"
            #rep+=f"| {i*16+x} |"
        else:
            for i in range(16):
                rep+="\n"
                for x in range(30):
                    rep+=f"|{self.showBoard[(i*30)+x]}|"
            #rep+=f"| {i*16+x} |"
            rep+="\n"
        print(rep)
    def realDisplay(self):
        rep = ''
        if self.difficulty == 1:
            for i in range(8):
                rep+="\n"
                for x in range(8):
                    rep+=f"| {self.board[(i*8)+x]} |"
        elif self.difficulty == 2:
            for i in range(16):
                print(len(self.board))
                rep+="\n"
                for x in range(16):
                    rep+=f"|{self.board[(i*16)+x]}|"
            #rep+=f"| {i*16+x} |"
        else:
            for i in range(16):
                rep+="\n"
                for x in range(30):
                    rep+=f"|{self.board[(i*30)+x]}|"
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
            #print("here")
            self.guess = self.guess[1:]
            self.guess = int(self.guess)
            self.guess-=1
            self.flag = True
            self.guessHandler()

        else:
            #print("here2")
            self.guess-=1
            self.flag = False
            self.guessHandler()
            
    


myGame = Game()

myGame.generator()

myGame.takeGuess()
result = myGame.guessHandler()
rep = ''
while result == None:
    myGame.takeGuess()
    myGame.guessHandler()
if result: print('you win')
else: print('lose')

#myGame.realDisplay()


