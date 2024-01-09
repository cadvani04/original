# author: Curran Advani
# date: March 16th, 2023
# file: player.py creates the class for player, ai, and minimax ai
# input: name, sign, and type of player
# output: choices for tic tac toe on board of board.py
import random

class Player:
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        return self.sign
    # return an instance sign
    def get_name(self):
        return self.name
    # return an instance name
    def choose(self, board):
        print(f'{self.name},{self.sign}: Enter a cell [A-C][1-3]:')
        valid_choices= ['A1','A2','A3','B1','B2','B3','C1', 'C2','C3']
        while True:
            user_choice = str(input())
            user_choice = user_choice.upper()
            if (user_choice in valid_choices) and board.isempty(user_choice):
                board.set(user_choice, self.sign)
                break
            else:
                print('You did not choose correctly.')


class AI(Player):
    def __init__(self, name, sign):
        self.name = name  # player's name
        self.sign = sign  # player's sign O or X

    def get_sign(self):
        return self.sign
        # return an instance sign

    def get_name(self):
        return self.name
    # return an instance name
    def choose(self, board):
        print(f'{self.name},{self.sign}: Enter a cell [A-C][1-3]:')
        while True:
            user_choice = random.choice(['A1','A2','A3','B1','B2','B3','C1', 'C2','C3'])
            if board.isempty(user_choice):
                board.set(user_choice, self.sign)
                break
            else:
                print('You did not choose correctly.')
                user_choice = random.choice(['A1','A2','A3','B1','B2','B3','C1', 'C2','C3'])







# prompt the user to choose a cell
# if the user enters a valid string and the cell on the board is empty, update the board
# otherwise print a message that the input is wrong and rewrite the prompt
# use the methods board.isempty(cell), and board.set(cell, sign)
class MiniMax(AI):
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.set(cell, self.sign)

    def minimax(self, board, self_player, start): #1. Check the base case: if the game is over, then return -1 if self lost, 0 if it is a tie, or 1 if self won.
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
        # is a tie
            elif board.get_winner() == ' ':
                return 0
        # self is a looser (opponent is a winner)
            else:
                return -1
# make a move (choose a cell) recursively
        maxscore = float('-inf') #2. Set the min score to infinity and max score to -infinity
        minscore = float('inf')
        move = ''
        correct_choices=['A1','A2','A3','B1','B2','B3','C1','C2','C3']
        for cell in correct_choices: #iterate through all available cells (9 cells) b. check if the cell is empty c. mark the cell with X or O (if self then mark it with its sign, otherwise mark it with another sign) d. get score by calling the minimax recursively (you need to alternate between self and opponent)
            if board.isempty(cell)==True:
                    if self_player:
                        board.set(cell, self.sign)
                        score = MiniMax.minimax(self, board, False, False)
                        if score>maxscore:
                            maxscore = score
                            move = cell
                    else:
                        if self.sign == 'X':
                            board.set(cell, 'O')
                        else:
                            board.set(cell,'X')
                        score = MiniMax.minimax(self, board, True, False)
                        if score<minscore:
                            minscore = score
                            move = cell
                    board.set(cell, ' ') #unmark the cell (make it a space again " ") and reset all other variables that were affected by the game play 4. If it is the start level (the last level to be executed completely and the last score to be returned) return the move.
        if start:
            return move
        elif self_player:
            return maxscore
        else:
            return minscore
'''Minimax:
1. Check the base case: if the game is over, then return -1 if self lost, 0 if it is a tie, or 1 if self won.
2. Set the min score to infinity and max score to -infinity
3. Choose a cell (or make a move): 
        a. iterate through all available cells (9 cells)
        b. check if the cell is empty
        c. mark the cell with X or O (if self then mark it with its sign, otherwise mark it with another sign)
        d. get score by calling the minimax recursively (you need to alternate between self and opponent)
        e. update score: if self then use the max score (compare it to the max score), otherwise use the min score (compare it to the min score)
        f. update move: update the cell index
        g. unmark the cell (make it a space again " ") and reset all other variables that were affected by the game play
4. If it is the start level (the last level to be executed completely and the last score to be returned) return the move. '''

    # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code

