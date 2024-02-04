"""
Created on Sun Nov  12 03:52:58 2023

@author: Mosopefoluwa John
"""

import random

MIN_DICE_VALUE = 1
MAX_DICE_VALUE = 6
MAX_SCORE = 15

def roll():
    return random.randint(MIN_DICE_VALUE, MAX_DICE_VALUE)

def get_num_of_players():
    while True:
        num_of_players = input("Enter the number of players (Between 2 and 4): ")
        if num_of_players.isdigit():
            players = int(num_of_players)
            if 2 <= players <= 4:
                return players
            else:
                print("Number of players must be between 2 and 4.")
        else:
            print("Invalid input, try again.")

def player_turn(player_num, scores):
    print("\nPlayer number", player_num + 1, "turn has just started!")
    print("Your total score is:", scores[player_num], "\n")
    
    current_score = 0
    while True:
        turn = input("Would you like to roll (y/n)? ").lower()
        if turn == "n":
            print("You have passed your turn.")
            break
        elif turn == "y":
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    scores[player_num] += current_score
    print("Your total score is:", scores[player_num])

def main():
    players = get_num_of_players()
    player_scores = [0] * players

    while max(player_scores) < MAX_SCORE:
        for player_num in range(players):
            player_turn(player_num, player_scores)

    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)
    print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)

if __name__ == "__main__":
    main()
