#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 17:56:44 2018

@author: shin
"""

#!/usr/bin/python3

from enum import Enum

class BOARDVAL(Enum):
    EMPTY = '-'
    PLAYER1 = 'X'
    PLAYER2 = 'O'

def drawBoard(board):
    for r in board:
        out = ""
        for c in r:
            if c == BOARDVAL.EMPTY:
                out.join('- ')
            if c == BOARDVAL.PLAYER1:
                out.join('X ')
            if c == BOARDVAL.PLAYER2:
                out.join('O ')
        print(out)

#board = [[BOARDVAL.EMPTY for c in range(3)] for r in range(3)]

board = [[1] * 3] * 3

print(board)

print()

print(type(board), len(board), len(board[0]), print(type(board[0][0])), print(board[0]))
print('Board')
drawBoard(board)