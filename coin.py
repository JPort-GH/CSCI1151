"""
Program: Match Coins Game - Coin Class
Author: Janet Portillo
Purpose: Represents a single coin that can be tossed.
Starter Code: No starter code used.
Date: 06/28/2026
"""

import random

class Coin:
    """A class representing a single tossable coin."""

    def __init__(self):
        """Initialize the coin with a default side."""
        self.__sideup = "Heads"

    def toss(self):
        """Randomly set the coin to Heads or Tails."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side of the coin."""
        return self.__sideup
