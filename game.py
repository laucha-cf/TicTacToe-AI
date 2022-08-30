import numpy as np
import time
class TicTacToe():
    """Represents a game of Tic Tac Toe and It's features
    """
    def __init__(self):
        #Numpy array to simulate a 3x3 the board
        self.board = np.full(fill_value=' ', shape=9) 
        #Keep track of winner
        self.current_winner = None 
        
    def print_board(self):
        """Show board as matrix
        Args:
            None
        Return:
            None
        """
        print(self.board.reshape(3,-1))
            
    def print_board_nums(self):
        """Show posible movements in board
        Args:
            None
        Return:
            None
        """
        number_board = np.arange(9).reshape(3,-1)
        for row in number_board:
            print(row)
            
    def available_moves(self):
        """Return list with available moves
        Args:
            None
        Return:
            available moves (list)
        """
        available_list = []
        for i, e in enumerate(self.board):
            if (e==' '):
                available_list.append(i)
        return available_list
            
    def count_empty_squares(self):
        """Count number of empty squares in the board
        Args:
            None
        Return:
            Number of empty squares (int)
        """
        return np.count_nonzero(self.board==' ')
    
    def empty_squares(self):
        """Say if there are empty squares in the board
        Args:
            None
        Return:
            True / False (bool)
        """
        return (self.count_empty_squares()>0)
    
    def make_move(self, square, letter):
        """Assign the letter of the player to the square.
        If valid move, assign square to letter. Return True.
        If invalid move, return False
        Args:
            square (int): square where player wants to move
            letter (str): letter of the player
        Return:
            True / False (bool)
        """
        if np.take(self.board, square) == ' ':
            self.board[square] = letter
            #assign a winner
            if self.winner(letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, letter):
        """Check if a player is a winner
        Args:
            letter (str): letter of a player
        Return:
            True / False (bool)
        """
        #Winner if 3 in a row
        board_reshaped = self.board.reshape(3,-1)
        
        for i in range(3):
            #Check for the row
            if np.all(board_reshaped[i, :]==letter):
                return True
            #Check for the column
            if np.all(board_reshaped[:, i]==letter):
                return True

        #Check for the diagonal
        main_diagonal = np.diagonal(board_reshaped)
        second_diagonal = np.fliplr(board_reshaped).diagonal()
        if np.all(main_diagonal==letter) or np.all(second_diagonal==letter):
            return True
        #If all fail, we don´t have a winner
        return False
        
    
def play(game, x_player, o_player, print_game=True):
    """Start a game between two players
    Args:
        game (TicTacToe)
        x_player, o_player (Player)
        print_game (bool): default True. Show the game at every step
    Return:
        None
    """
    if print_game:
        game.print_board_nums()
        
    letter = 'X'
        
    while game.empty_squares():
        if print_game:
            print(f'Available Moves: {game.available_moves()}')
        
        if letter == 'O':
            move = o_player.get_move(game)
        else:
            move = x_player.get_move(game)
        
        if game.make_move(move, letter):
            print(f'{letter} makes a move to square {move}')
            game.print_board()
            print('')
        
        if print_game:
            time.sleep(1) #Just a little pause between players
        
        if game.current_winner:
            if print_game:
                print(f'{letter}\'  wins')
            return letter
            
        #After we made the move, we need to alternate players
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'

        
    #No squares remaining to play and nobody won        
    if print_game:
        print('It\'s a tie!')