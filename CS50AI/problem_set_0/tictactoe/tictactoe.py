"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_num = 0
    o_num = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_num += 1
            elif cell == O:
                o_num += 1
    if x_num > o_num:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    import copy
    board_copy = copy.deepcopy(board)
    if terminal(board) == True:
        raise ValueError("Game is over.")
    elif board_copy[action[0]][action[1]] != None or action[0] >= len(board) or action[1] >= len(board[0]) or action[0] < 0 or action[1] < 0:
        raise ValueError("Invalid input")
    else:
        if player(board) == O:
            board_copy[action[0]][action[1]] = O
        else:
            board_copy[action[0]][action[1]] = X
    return board_copy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Three winning cases: horizontally, vertically, diagonally
    # Horizontal
    for row in board:
        if all(cell == X for cell in row):
            return X
        elif all(cell == O for cell in row):
            return O

    # Vertical
    for i in range(len(board[0])):
        if all(row[i] == X for row in board):
            return X
        elif all(row[i] == O for row in board):
            return O

    # Diagonal
    # From left
    if all(board[i][i] == X for i in range(len(board[0]))):
        return X
    elif all(board[i][i] == O for i in range(len(board[0]))):
        return O
    # From right
    if all(board[len(board) - 1 - i][i] == X for i in range(len(board))):
        return X
    elif all(board[len(board) - 1 - i][i] == O for i in range(len(board))):
        return O

    # No winner(game in progress or tied)
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # True if have winner or tied
    if winner(board) != None:
        return True
    elif all(cell != None for row in board for cell in row):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    elif terminal(board) == True and winner(board) == None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    alpha = float('-inf')
    beta = float('inf')

    def max_value(board, alpha, beta):
        v = float('-inf')
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = max(v, min_value(result(board, action), alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(board, alpha, beta):
        v = float('inf')
        if terminal(board):
            return utility(board)
        for action in actions(board):
            v = min(v, max_value(result(board, action), alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    if player(board) == X:
        return max(actions(board), key=lambda action: min_value(result(board, action), alpha, beta))
    else:
        return min(actions(board), key=lambda action: max_value(result(board, action), alpha, beta))
