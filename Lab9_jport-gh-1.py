"""
Program: Match Coins Game - Main Game File
Author: Janet Portillo
Purpose: Runs the Match Coins game using Player and Coin classes.
Starter Code: No starter code used.
Date: 06/28/2026
"""

from player import Player

def main():
    print("\n--- Coin Match Game ---")

    # Create two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.\n")

    choice = input("Do you want to toss the coins? (y/n): ")

    while choice.lower() == "y":

        print("\nTossing...")

        # Toss coins
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        # Determine winner
        if side1 == side2:
            print("...It's a Match! Player 1 wins a coin.\n")
            player1.win_coin()
            player2.lose_coin()
        else:
            print
