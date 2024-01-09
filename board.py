# author: Curran Advani
# date: March 16th, 2023
# file: board.py creates and operates the board for the game of tic tac toe
# input: code for the encode text and decode data
# output: displays the encoded binary and decoded text messages in a string

class Board:
    def __init__(self):
        self.board = [[' ',' ',' '],[' ', ' ', ' '],[' ', ' ', ' ']]
        # board is a list of cells that are represented
        # by strings (" ", "O", and "X")
        # initially it is made of empty cells represented
        # by " " strings
        self.sign = " "
        self.size = 3
        # the winner's sign O or X
        self.winner = ""


    def get_size(self):
        return self.size
    # optional, return the board size (an instance size)
    def get_winner(self):
        return self.winner


    # return the winner's sign O or X (an instance winner)
    def set(self, cell, sign):
        #i = cell[0] is the letter --> ascii - 41
        #j = cell[1] is the number --> -1
        i = ord(cell[0])-65
        j = int(cell[1])-1
        self.board[i][j] = sign

    # mark the cell on the board with the sign X or O
    # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
    # you can use a tuple ("A1", "B1",...) to obtain indexes
    # this implementation is up to you
    def isempty(self, cell):
        i = ord(cell[0]) - 65
        j = int(cell[1]) - 1
        if self.board[i][j] == ' ':
            return True
        else:
            return False
    # return True if board isn't empty
    # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
    # return True if the cell is empty (not marked with X or O)
    def isdone(self):
        done = False
        self.winner = ''
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                if self.board[i][0]=='X':
                    done = True
                    self.winner = 'X'
                elif self.board[i][0]=='O':
                    done = True
                    self.winner = 'O'
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i]=='X':
                    done = True
                    self.winner = 'X'
                elif self.board[0][i]=='O':
                    done = True
                    self.winner = 'O'
        if self.board[0][0]==self.board[1][1]==self.board[2][2]:
            if self.board[0][0] == 'X':
                done = True
                self.winner = 'X'
            elif self.board[0][0] == 'O':
                done = True
                self.winner = 'O'
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] =='X':
                done = True
                self.winner = 'X'
            elif self.board[0][2] == 'O':
                done = True
                self.winner = 'O'

        if done:
            return done

        done = True
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if (self.board[i][j] == ' '):
                    done = False
        if done:
            self.winner = ' '
        # check all game terminating conditions, if one of them is present, assign the var done to True
        # depending on conditions assign the instance var winner to O or X
        return done

    def show(self):
        print(f'    1   2   3\n'
              f'  +---+---+---+\n'
              f'A | {self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]} |\n'
              f'  +---+---+---+\n'
              f'B | {self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]} |\n'
              f'  +---+---+---+\n'
              f'C | {self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]} |\n'
              f'  +---+---+---+\n')
# draw the board