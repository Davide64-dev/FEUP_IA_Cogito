import random
import threading
import pygame
import copy

from sound import Sound

# General Bot class
class Bot:

    # Constructor - Receives the game the bot will operate in
    def __init__(self, game):
        self.game = game
        self.gamecopy = copy.copy(self.game)
    
    # Lists all possible moves to do given the game's board
    def valid_moves(self):
        valid_moves = set()
        for i in range (0, 11):
            for j in range (0, 11):
                gamecopy = self.game.deep_copy_game()
                if gamecopy.isArrowClick(i, j):
                    gamecopy.make_move(i,j)

                    print(f"({i},{j})")
                    valid_moves.add(gamecopy)
        return valid_moves

    # Check if a tile is a right side arrow
    def isRightSideArrow(self, row, col):
        return col == 10 and 1 <= row <= 9

    # Check if a tile is a Top side arrow
    def isTopSideArrow(self, row, col):
        return row == 0 and 1 <= col <= 9

    # Check is a tile is a Bottom side arrow
    def isBottomSideArrow(self, row, col):
        return row == 10 and 1 <= col <= 9

