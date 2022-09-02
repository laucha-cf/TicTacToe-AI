from modules.player import HumanPlayer, ComputerPlayer, SmartComputerPlayer
from modules.game import TicTacToe, play

if __name__ == '__main__':
    """
    x_wins = 0
    o_wins = 0
    ties = 0
    n = 1000
    
    for _ in range(n):
        x_player = SmartComputerPlayer('X')
        o_player = ComputerPlayer('O')
        game = TicTacToe()
        result = play(game, x_player, o_player, print_game=False)
        
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1
    
    print(f'--RESULTS--')
    print(f'After {n} games we can see...')
    print(f'X Wins: {x_wins}')
    print(f'O Wins: {o_wins}')
    print(f'Ties: {ties}')
    """
    
    x_player = SmartComputerPlayer('X')
    o_player = HumanPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, print_game=True)