
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
        pass


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        pass