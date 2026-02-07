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
    

    countX = 0
    countO = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                countX += 1

            if board[i][j] == O:
                countO +=1


    if countX == countO:
        return X
    else:
        return O

    


def actions(board):
    
    possibleActions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.add((i,j))
    return possibleActions


def result(board, action):

    if board[action[0]][action[1]] != EMPTY:
        raise ValueError("Invalid action")


    newBoard = []

    for row in board:
        newBoard.append(row.copy())

    newBoard [action[0]][action[1]] = player(board)

    return newBoard


def winner(board):
    
    for i in range(3):
        if board[i][0] is not EMPTY:
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            
    for i in range(3):
        if board[0][i] is not EMPTY:
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]
            
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def terminal(board):
    
    if winner(board) != None:
        return True
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
            

    return True


def utility(board):
    

    if winner(board) == X:
        return 1
    if winner(board) ==O:
        return -1
    
    return 0
    

def MAX_VALUE(board):
    if terminal(board):
        return utility(board)

    v = float("-inf")
    for action in actions(board):
        v = max(v, MIN_VALUE(result(board, action)))
    return v

def MIN_VALUE(board):
    if terminal(board): return utility(board)

    v = float("inf")
    for action in actions(board):
        v = min(v, MAX_VALUE(result(board, action)))
    return v

def minimax(board):
    
    if terminal(board):
        return None
    
    if player(board) == X:
        best_value = float("-inf")
        best_action = None

        for action in actions(board):
            value = MIN_VALUE(result(board, action))
            if value > best_value:
                best_value = value
                best_action = action

        return best_action
    
    else:

        best_value = float("inf")
        best_action = None

        for action in actions(board):
            value = MAX_VALUE(result(board, action))
            if value < best_value:
                best_value = value
                best_action = action

        return best_action