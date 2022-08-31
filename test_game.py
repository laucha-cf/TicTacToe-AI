from game import TicTacToe
import numpy as np

#TEST available_moves
def test_available_moves_1():
    """Test board with all movements available
    """
    game = TicTacToe()
    assert(game.available_moves() == [0,1,2,3,4,5,6,7,8])

def test_available_moves_2():
    """Test board with some movements available
    """
    game = TicTacToe()
    new_board = np.array([' ',' ','X',' ',' ','O',' ',' ','X'])
    game.board = new_board
    assert(game.available_moves() == [0,1,3,4,6,7])
    
def test_available_moves_3():
    """Test board with no movements available. Board is full
    """
    game = TicTacToe()
    new_board = np.array(['X','O','X','O','O','O','X','O','X'])
    game.board = new_board
    assert(game.available_moves() == [])

#TEST count_empty_squares
def test_count_empty_squares_1():
    """Test empty board
    """
    game = TicTacToe()
    assert(game.count_empty_squares() == 9)
    
def test_count_empty_squares_2():
    """Test board with some squares filled
    """
    game = TicTacToe()
    new_board = np.array([' ',' ','X',' ',' ','O',' ',' ','X'])
    game.board = new_board
    
    assert(game.count_empty_squares() == 6)

def test_count_empty_squares_3():
    """Test full board
    """
    game = TicTacToe()
    new_board = np.array(['X','O','X','O','O','O','X','O','X'])
    game.board = new_board
    assert(game.count_empty_squares() == 0)

#TEST empty_squares
def test_empty_squares_1():
    """Test empty board
    """
    game = TicTacToe()
    assert(game.empty_squares() == True)
    
def test_empty_squares_2():
    """Test board with some squares filled
    """
    game = TicTacToe()
    new_board = np.array([' ',' ','X',' ',' ','O',' ',' ','X'])
    game.board = new_board
    assert(game.empty_squares() == True)
    
def test_empty_squares_3():
    """Test full board
    """
    game = TicTacToe()
    new_board = np.array(['X','O','X','O','O','O','X','O','X'])
    game.board = new_board
    assert(game.empty_squares() == False)
    
#TEST make_move
def test_make_move_1():
    """Test empty board
    """
    game = TicTacToe()
    assert(game.make_move(4, 'X')==True)

def test_make_move_2():
    """Test board with some squares filled
    """
    game = TicTacToe()
    new_board = np.array([' ',' ','X',' ',' ','O',' ',' ','X'])
    game.board = new_board
    assert(game.make_move(2, 'X')==False)

def test_make_move_3():
    """Test board with some squares filled
    """
    game = TicTacToe()
    new_board = np.array([' ',' ','X',' ',' ','O',' ',' ','X'])
    game.board = new_board
    assert(game.make_move(3, 'X')==True)
    
def test_make_move_4():
    """Test full board
    """
    game = TicTacToe()
    new_board = np.array(['X','O','X','O','O','O','X','O','X'])
    game.board = new_board
    assert(game.make_move(3, 'O')==False)

#TEST winner
def test_winner_1():
    """Test empty board
    """
    game = TicTacToe()
    assert(game.winner('O')==False)

def test_winner_2():
    """Test if 'O' player is winner. Full board.
    """
    game = TicTacToe()
    new_board = np.array(['X','O','X',
                          'O','O','O',
                          'X','O','X'])
    game.board = new_board
    assert(game.winner('O')==True)

def test_winner_3():
    """Test if 'X' player is winner. Full board.
    """
    game = TicTacToe()
    new_board = np.array(['X','O','X',
                          'O','O','O',
                          'X','O','X'])
    game.board = new_board
    assert(game.winner('X')==False)
    
def test_winner_4():
    """Test if 'X' player is winner. Some squares filled.
    """
    game = TicTacToe()
    new_board = np.array([' ',' ','X',
                          ' ','X','O',
                          'X',' ','X'])
    game.board = new_board
    assert(game.winner('X')==True)
    
def test_winner_5():
    """Test if 'O' player is winner. Some squares filled.
    """
    game = TicTacToe()
    new_board = np.array([' ',' ','X',
                          ' ','X','O',
                          'X',' ','X'])
    game.board = new_board
    assert(game.winner('O')==False)