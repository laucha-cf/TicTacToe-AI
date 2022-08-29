from player import HumanPlayer, ComputerPlayer, SmartComputerPlayer
from game import TicTacToe, play

if __name__ == '__main__':
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    
    game = TicTacToe()
    
    play(game, x_player, o_player, print_game=True)