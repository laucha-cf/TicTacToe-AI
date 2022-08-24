import numpy as np
from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = np.full(fill_value=' ', shape=9) #Numpy array to simulate a 3x3 the board
        self.current_winner = None #Keep track of winner
        
    def print_board(self):
        #Show board as matrix
        print(self.board.reshape(3,-1))
            
    def print_board_nums(self):
        #Create temporary board with positions of posible movements to show
        number_board = np.arange(9).reshape(3,-1)
        for row in number_board:
            print(row)
            
    def available_moves(self):
        #Return array showing available moves
        available_list = []
        for i, e in enumerate(self.board):
            if type(e)!='numpy.int32':
                available_list.append(i)
        return available_list
            
    def count_empty_squares(self):
        return np.count_nonzero(self.board==' ')
    
    def empty_squares(self):
        return (self.count_empty_squares()>0)
    
    def make_move(self, square, letter):
        #If valid move, assign square to letter. Return True
        #If invalid move, return False
        if np.take(self.board, square) == ' ':
            self.board[square] = letter
            #assign a winner
            if self.winner(letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, letter):
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
            
        if game.current_winner:
            if print_game:
                print(f'{letter}\'  wins')
            return letter
            
        #After we made the move, we need to alternate players
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'
            
        if print_game:
            print('It\'s a tie!')
            
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    
    game = TicTacToe()
    
    play(game, x_player, o_player, print_game=True)