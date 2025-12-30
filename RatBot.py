import sys
import copy
import time
from config import *
from board import Board

class RatBot:
    def __init__(self, board):
        self.board = board
        self.nodes_expanded = 0
        self.depth = 1 ## set depth as you see fit and use it further for your works. 

    def get_best_move(self):
        legal_moves = self.board.get_legal_moves()

        if not legal_moves:
            return None

        best_score = -10**9
        best_moves = []

        for move in legal_moves:
            self.board.make_move(move)

        score = self.evaluate_board()
        
        self.board.undo_move()

        if score > best_score:
            best_score = score
            best_moves = [move]
        elif score == best_score:
            best_moves.append(move)

        return random.choice(best_moves)

    def evaluate_board(self):
        piece_values = { 
            'P': 20,
            'N': 70,
            'B': 70,
            'K': 1000
        }

        score = 0

for row in self.board.board:
    for piece in row:
        if piece == EMPTY_SQUARE:
            continue

        value = piece_values[piece[1]]

if piece[0] == 'w':
    score += value
else:
    score -= value

if self.board.is_in_check():
    score -= 2 if self.board.white_to_move else 2

return score
        

