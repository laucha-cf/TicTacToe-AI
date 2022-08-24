from player import HumanPlayer, ComputerPlayer
from game import TicTacToe, play

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    
    game = TicTacToe()
    
    play(game, x_player, o_player, print_game=True)