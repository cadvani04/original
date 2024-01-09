# author: Curran Advani
# date: Mar 17, 2023
# file: fifteen.py
# input: users specific moves for the games
# output: the puzzle game, fifteen
import numpy as np
class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4):
        self.size = size
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        for i in range(self.size):
            print("+---" * self.size + "+")
            for j in range(self.size):
                if self.tiles[i * self.size + j] == 0:
                    print("|   ", end="")
                else:
                    print("|{:2d} ".format(self.tiles[i * self.size + j]), end="")
            print("|")
        print("+---" * self.size + "+")

    # return a string representation of the vector of tiles as a 2d array
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    # 13 14 15
    def __str__(self):
        output = ''
        i = 0
        while i < self.size:
            j = 0
            while j < self.size:
                tile = self.tiles[(i * self.size) + j]
                if tile == 0:
                    output += '   '
                elif len(str(tile)) == 2:
                    output += f'{tile} '
                else:
                    output += f' {tile} '
                j += 1
            output += '\n'
            i += 1
        return output

    # exchange i-tile with j-tile
    # tiles are numbered 1-15, the last tile is 0 (empty space)
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor
    def is_valid_move(self, move):
        zero_pos = np.where(self.tiles == 0)[0][0]
        move_pos = np.where(self.tiles == move)[0][0]

        # check if move is adjacent to zero
        if zero_pos == move_pos - 1 and move_pos % self.size != 0:  # left
            return True
        elif zero_pos == move_pos + 1 and zero_pos % self.size != 0:  # right
            return True
        elif zero_pos == move_pos - self.size:  # up
            return True
        elif zero_pos == move_pos + self.size:  # down
            return True
        else:
            return False

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose
    def update(self, move):
        zero_pos = np.where(self.tiles == 0)[0][0]
        move_pos = np.where(self.tiles == move)[0][0]

        if self.is_valid_move(move):
            self.transpose(zero_pos, move_pos)
            return self.tiles
        else:
            print("Invalid move.")

    # shuffle tiles
    def shuffle(self, moves=100):
        np.random.shuffle(self.tiles)

    # verify if the puzzle is solved
    def is_solved(self):
        if str(self) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n':
            return True
        else:
            return False

    # verify if the puzzle is solvable (optional)
    def is_solvable(self):
        pass

    # solve the puzzle (optional)
    def solve(self):
        pass


if __name__ == '__main__':
    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False
'''You should be able to play the game if you uncomment the code below'''


game = Fifteen()
game.shuffle()
game.draw()
while True:
    move = input('Enter your move or q to quit: ')
    if move == 'q':
        break
    elif not move.isdigit():
        continue
    game.update(int(move))
    game.draw()
    if game.is_solved():
        break
print('Game over!')
