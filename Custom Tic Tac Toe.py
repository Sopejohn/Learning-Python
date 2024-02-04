"""
Created on Sun Feb  4 05:57:25 2024

@author: mosope
"""

import random

print("It's time for Tic Tac Toe!!!")
print("----------------------")

POSSIBLE_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ROWS = 3
COLUMNS = 3

def PrintBoard():
    for x in range(ROWS):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(COLUMNS):
            print("", board[x][y], end=" |")
    print("\n+---+---+---+")

def ModifyArray(number, turn):
    number -= 1
    if number == 0:
        board[0][0] = turn
    elif number == 1:
        board[0][1] = turn
    elif number == 2:
        board[0][2] = turn
    elif number == 3:
        board[1][0] = turn
    elif number == 4:
        board[1][1] = turn
    elif number == 5:
        board[1][2] = turn
    elif number == 6:
        board[2][0] = turn
    elif number == 7:
        board[2][1] = turn
    elif number == 8:
        board[2][2] = turn

# Function to check for the winner
def CheckWinner(board):
    # Horizontally
    if(board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
        print("O has won!")
        return "O"
    # Horizontally
    if(board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O'):
        print("O has won!")
        return "O"
    elif(board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O'):
        print("O has won!")
        return "O"
    elif(board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O'):
        print("O has won!")
        return "O"
      # Vertically
    if(board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O'):
        print("O has won!")
        return "O"
    elif(board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O'):
        print("O has won!")
        return "O"
    elif(board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O'):
        print("O has won!")
        return "O"
      # Diagonally
    elif(board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X'):
        print("X has won!")
        return "X"
    elif(board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O'):
        print("O has won!")  
        return "O"
    elif(board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'):
        print("X has won!")  
        return "X"
    elif(board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'):
        print("O has won!") 
        return "O" 
    else:
        return "N"

leave = False
turn_counter = 0

while not leave:
    # Determine current player
    current_player = 'X' if turn_counter % 2 == 0 else 'O'

    PrintBoard()
    
    while True:
        try:
            number_picked = int(input(f"\n{current_player}, choose a number [1-9]: "))
            if 1 <= number_picked <= 9 and number_picked in POSSIBLE_NUMBERS:
                break
            else:
                print("Invalid input. Select a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    ModifyArray(number_picked, current_player)
    POSSIBLE_NUMBERS.remove(number_picked)
    turn_counter += 1

    winner = CheckWinner(board)
    if winner != "N":
        PrintBoard()
        print(f"\n{current_player} has won! Congratulations!")
        break

    if turn_counter == 9:
        PrintBoard()
        print("\nIt's a tie! The game is a draw.")
        break
