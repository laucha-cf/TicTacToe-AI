from unittest.case import _AssertRaisesContext
from player import ComputerPlayer
from game import TicTacToe
import numpy as np
import unittest

class TestComputerPlayer(unittest.TestCase):
    def test_get_move_1(self):
        """Test if move is a valid square.
        """
        game = TicTacToe()
        new_board = np.array([' ',' ','X',' ',' ','O',' ',' ','X'])
        game.board = new_board
        player = ComputerPlayer('X')
        square = player.get_move(game)
        assert(square in [0,1,3,4,6,7])

    def test_get_move_2(self):
        """Test if move is a valid square.
        """
        game = TicTacToe()
        new_board = np.array(['O',' ','X',' ',' ','O','X',' ','X'])
        game.board = new_board
        player = ComputerPlayer('X')
        square = player.get_move(game)
        assert(square in [1,3,4,7])

    def test_get_move_3(self):
        """Test if move is a valid square. Just one spot available.
        """
        game = TicTacToe()
        new_board = np.array(['O','X','X','X',' ','O','X','O','X'])
        game.board = new_board
        player = ComputerPlayer('X')
        square = player.get_move(game)
        assert(square == 4)

    def test_get_move_4(self):
        """Test if move is a valid square. No valid square. Raise an error.
        """
        game = TicTacToe()
        new_board = np.array(['O','X','X','X','O','O','X','O','X'])
        game.board = new_board
        player = ComputerPlayer('X')
        with self.assertRaises(Exception):
            player.get_move(game)