"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 10        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def mc_trial(board, player):
    """
    See function description in assignment details
    """
    if board.check_win() != None:
        return
    empty_squares = board.get_empty_squares()
    squares = empty_squares[random.randrange(len(empty_squares))]
    board.move(squares[0], squares[1], player)
    mc_trial(board, provided.switch_player(player))


def mc_update_scores(scores, board, player):
    """
    See function description in assignment details
    """
    winner = board.check_win()
    if winner == provided.DRAW:
        return
    machine_win = winner == player
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            player_here = board.square(row, col)
            if player_here == provided.EMPTY:
                continue
            machine_here = player_here == player
            if machine_win and machine_here:
                scores[row][col] += SCORE_CURRENT
            elif machine_win and not machine_here:
                scores[row][col] -= SCORE_OTHER
            elif not machine_win and machine_here:
                scores[row][col] -= SCORE_CURRENT
            else:
                scores[row][col] += SCORE_OTHER


def get_best_move(board, scores):
    """
    See function description in assignment details
    """
    empty = board.get_empty_squares()
    if len(empty) == 0:
        return
    best_move = None
    best_score = None
    for square in empty:
        if best_move == None or scores[square[0]][square[1]] > best_score:
            best_move = square
            best_score = scores[square[0]][square[1]]
    return best_move


def mc_move(board, player, trials):
    """
    See function description in assignment details
    """
    scores = [[0 for dummy in range(board.get_dim())] \
        for dummy in range(board.get_dim())]
    for dummy in range(trials):
        board_clone = board.clone()
        mc_trial(board_clone, player)
        mc_update_scores(scores, board_clone, player)
    return get_best_move(board, scores)


# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
