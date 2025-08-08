"""
File dedicated for representing characters
"""

from move import Move

class Character:
    """
    test
    """
    def __init__(self,
                 normal_moves: dict[str, Move],
                 special_moves: dict[str, Move],
                 super_moves: dict[str, Move]):
        self.normal_moves = normal_moves
        self.special_moves = special_moves
        self.super_moves = super_moves
