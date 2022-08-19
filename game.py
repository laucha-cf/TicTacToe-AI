import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.full(fill_value=' ', shape=9) #Numpy array to simulate a 3x3 the board
        self.current_winner = None #Keep track of winner
        
    def print_board(self):
        #Show board as matrix
        print(self.board.reshape(3,-1))
            
    def print_board_nums():
        #Create temporary board with positions of posible movements to show
        number_board = np.arange(9).reshape(3,-1)
        for row in number_board:
            print(row)
            
    def available_moves(self):
        #Return array showing available moves
        return self.board == ' '
    
    def count_empty_squares(self):
        return np.count_nonzero(self.board==' ')
    
    def empty_squares(self):
        return (self.count_empty_squares()>0)
    
    def make_move(self, square, letter):
        if np.take(self.board, square) == ' ':
            self.board[square] = letter
            #assign a winner
            return True
        return False
    
def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()
        
    letter = 'X'
        
    while game.empty_squares():
        if letter == 'O':
            move = o_player.get_move(game)
        else:
            move = x_player.get_move(game)
            
        if game.make_move(move, letter):
            print(f'{letter} makes a move to square {move}')
            game.print_board()
            print('')
            
        #After we made the move, we need to alternate players
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'