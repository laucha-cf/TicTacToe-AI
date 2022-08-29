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
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        valid_square = False
        square_val = None
        while not valid_square:
            input_val = input(self.letter + '\'s turn. Input next move (0-8):')
            #Validate input by:
            #Try to cast it to an integer
            #Check if the spot is available on the board
            try:
                square_val = int(input_val)
                if square_val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid Square. Try again')
                print('')
        
        return square_val
    
class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def get_move(self, game):
        #If all spots are available, choose random
        if game.count_empty_squares() == 9:
            square = random.choice(game.available_moves())
        else:
            #Minimax MOMENT
            square = self.minimax(game, self.letter)['position']
        return square
    
    def minimax(self, game_state, cur_player):
        maximizer = self.letter
        minimizer = 'O' if cur_player=='X' else 'X'
        
        #Base Case 1: Previous move is a winner
        if game_state.current_winner == minimizer:
            return {'position': None,
                    'score': 1 * (game_state.count_empty_squares()+1) if minimizer==maximizer 
                        else -1 * (game_state.count_empty_squares()+1)
                    }
        #Base Case 2: No empty squares. Nobody won
        elif not game_state.empty_squares():
            return {'position': None,
                    'score': 0}
        
        if cur_player == maximizer:
            #At each step, we should maximize the score
            best_score = {'position': None, 'score': -math.inf}
        else:
            #At each step, we should minimize the score
            best_score = {'position': None, 'score': math.inf}
        
        for possible_move in game_state.available_moves():
            #STEP 1: Make a move
            game_state.make_move(possible_move, cur_player)
            
            #STEP 2: Use minimax to simulate a game after making that move
            #Alternate players
            simulate_score = self.minimax(game_state, minimizer)
            
            #STEP 3: Undo the move
            #Empty the spot and reset winner
            game_state.board[possible_move] = ' '
            game_state.current_winner = None
            simulate_score['position'] = possible_move
            
            #STEP 4: Update the dictioneries IF necessary
            if cur_player == maximizer:
                if simulate_score['score'] > best_score['score']:
                    best_score = simulate_score
            else:
                if simulate_score['score'] < best_score['score']:
                    best_score = simulate_score
                    
        return best_score