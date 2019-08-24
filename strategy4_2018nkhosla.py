from core import *
from random import *

mmDict = dict()
def random(board, player):
    possibleMoves = actions(board)
    rIndex = randint(0, len(possibleMoves)-1)
    move = int(possibleMoves[rIndex])
    return move

def human(board, player):
    boxNum = input( "Where do you want to move(box 0-8)")
    return int(boxNum)

def minimax_strategy(max_depth):
    """ Takes a max_depth parameter and returns a new function/closure for strategy """
    def strategy(board, player):
        return minimax(board, player, max_depth)
    return strategy

def minimax(board, player, max_depth):
    """ Takes a current board and player and max_depth and returns a best move
     This is the top level mini-max function. Note depth is ignored. We
     always search to the end of the game."""
    if player == MAX:
        move = max_dfs(board, player, max_depth)[1]
    if player == MIN:
        move = min_dfs(board, player, max_depth)[1]
    return move


def max_dfs(board, player, max_depth):
    global mmDict
    if not terminal_test(board) == False:
        temp = terminal_test(board)
        if temp == TIE:
            return 0, None
        if temp == MAX:
            return 1, None
        if temp == MIN:
            return -1, None
    v = -10**9
    move = -1
    for m in actions(board):
        m = int(m)
        new_board = make_move(board,player, m)
 #       new_value = min_dfs(make_move(board,player, m), toggle(player), max_depth)[0]
        if(new_board, player) in mmDict:
            new_value = mmDict[(new_board, player)]
        else:
            new_value = min_dfs(new_board, toggle(player), max_depth)[0]
            mmDict[(new_board, player)] = new_value
        if new_value > v:
            v = new_value
            move = int(m)
            if v == 1:
                return v, int(move)
    return v, int(move)

def min_dfs(board, player, max_depth):
    global mmDict
    if not terminal_test(board) == False:
        temp = terminal_test(board)
        if temp == TIE:
            return 0, None
        if temp == MAX:
            return 1, None
        if temp == MIN:
            return -1, None
    v = 10**9
    move = -1
    for m in actions(board):
        m = int(m)
        new_board = make_move(board,player, m)
 #       new_value = min_dfs(make_move(board,player, m), toggle(player), max_depth)[0]
        if(new_board, player) in mmDict:
            new_value = mmDict[(new_board, player)]
        else:
            new_value = max_dfs(new_board, toggle(player), max_depth)[0]
            mmDict[(new_board, player)] = new_value
        if new_value < v:
            v = new_value
            move = int(m)
            if v == -1:
                return v, int(move)
    return v, int(move)
