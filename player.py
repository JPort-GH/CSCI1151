"""
Program: Match Coins Game - Player Class
Author: Janet Portillo
Purpose: Represents a player with a name, wallet, and a coin to toss.
Starter Code: No starter code used.
Date: 06/28/2026
"""

from coin import Coin

class Player:
    """A class representing a player in the coin match game."""

    def __init__(self, name):
        """Initialize the player with a name, wallet, and coin."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Tell the player's coin to toss itself."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Subtract one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the player's wallet amount."""
        return self.__wallet

    def get_name(self):
        """Return the player's name."""
        return self.__name
