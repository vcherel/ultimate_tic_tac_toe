from enum import Enum


class Strategy(Enum):
    RANDOM = 'random'
    RANDOM_BEST = 'random_best'
    MCTS = 'mcts'


# RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (175, 250, 175)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Variables:
    """
    This class contains all the variables that are used in all different files
    """
    def __init__(self, file_path='parameters.txt'):
        # From call of the script main.py
        self.nb_games = None  # Number of games to play
        self.display_game = None
        self.depth_board = None


        # From file parameters.txt
        self.size_board = None

        self.player1_auto = None
        self.player1_strategy = None
        
        self.player2_auto = None
        self.player2_strategy = None


        # Read values from file
        self.read_parameters(file_path)
                

        # Other variables
        self.size_board = 100
        self.screen_size = None
        self.screen = None

        self.text_victory = None  # A tuple (text, textRect)

        self.finished = None  # True if the game is finished
        self.winner = None  # True : circle won, False : cross won
        self.actual_player = None  # The player that is playing
        
        self.list_result = []  # All the results of the games

        self.simulating = False  # True if the game is simulating (for MCTS)
        self.previous_mcts = None  # The previous MCTS node that was selected

        self.debug = False  # Variable to use when debugging



    def read_parameters(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('#') or line.strip() == '':
                    # Skip comments and empty lines
                    continue

                key, value = line.strip().split(':')
                key = key.strip()

                if key == 'size_board':
                    self.size_board = int(value.strip())
                elif key == 'player1_auto':
                    self.player1_auto = value.strip() == 'True'
                elif key == 'player1_strategy':
                    self.player1_strategy = Strategy(value.strip())
                elif key == 'player2_auto':
                    self.player2_auto = value.strip() == 'True'
                elif key == 'player2_strategy':
                    self.player2_strategy = Strategy(value.strip())
                else:
                    print(f'Unknown parameter: {key}')
            
        # Stop the program if two player have the strategy mcts
        if self.player1_strategy == Strategy.MCTS and self.player2_strategy == Strategy.MCTS:
            print('Error: Both players cannot have the strategy MCTS')
            exit()


    def get_current_team(self):
        return self.actual_player.get_team()
    

    def set_simulating(self, simulating):
        self.simulating = simulating
    
    def set_finished(self, finished):
        if self.simulating:
            return
        else:
            self.finished = finished

    def set_winner(self, winner):
        if self.simulating:
            return
        else:
            self.winner = winner


    def set_screen(self, screen):
        self.screen = screen
    
    def set_screen_size(self, screen_size):
        self.screen_size = screen_size

    def set_text_victory(self, text, textRect):
        self.text_victory = (text, textRect)

    def set_depth_board(self, depth_board):
        self.depth_board = depth_board


    def add_to_list_result(self, result):
        self.list_result.append(result)


    def decrease_nb_games(self):
        self.nb_games -= 1


    def update_previous_mcts(self, path_played):
        if self.previous_mcts is not None:
            for child in self.previous_mcts.childs:
                if child.previous_box_played.get_path() == path_played:
                    self.previous_mcts = child
                    return
            
            self.previous_mcts = None
            return


variables = Variables()