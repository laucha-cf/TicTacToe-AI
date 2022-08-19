
import math
import random

# Father class
class Player:
    def __init__(self, letter):
        #Letter can be X or O
        self.letter = letter

    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        #Get a random empty spot for the next move
        square = random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        square_val = None
        while not valid_square:
            input_val = input(self.letter + '\'s turn. Input next move (0-9):')
            #Validate input by:
            #Try to cast it to an integer
            #Check if the spot is available on the board
            try:
                square_val = int(input_val)
                if square_val not in game.available():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Try again')
        
        return square_val