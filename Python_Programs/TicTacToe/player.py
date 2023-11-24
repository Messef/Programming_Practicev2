import random
class Player:
    def __init__(self, letter): 
        self.letter = letter;
    def get_move(self, game): 
        pass

class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter) # Inheritance
    
    def get_move(self, game):
        list = []
        for y in game.available_moves():
            list.append(y)
        x = random.randint(0, len(list)-1)
        square = list[x]
        return square
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) # Inheritance
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = int(input(self.letter + "\'s turn. Please input a move(0-8): "))
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("not valid. try again.")

        return val
class smartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter) # Inheritance
    def minimax(self):
        pass
    def get_move(self, game):
        list = []
        for y in game.available_moves():
            list.append(y)
        if len(list) == 9:
            x = random.randint(0, len(list)-1)
        else:
            square = self.minimax(game, self.letter)
        return square
    def minimax(self, state, letter):
        max_player = self.letter
        other_player = "X" if self.letter == "O" else "O"
        if state.current_winner == other_player:
            return {
                'position': None,
                'score': 1*(state.num_empty_squares() + 1) if other_player == max_player else -1*(state.num_empty_squares() + 1)
            }
        
        elif not state.empty_squares():
            return {'position': None, 'score': 0}
        # Work on it later
