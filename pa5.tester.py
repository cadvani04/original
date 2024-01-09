import numpy as np

class Fifteen:

    def __init__(self, size=4):
        self.size = size
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])

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

    def __str__(self):
        '''l = ' '
        for i in range(1,len(self.tiles)):
            if i % 4==0:
                l+= str(i)
                l+='\n'
                l+=' '
            else:
                l+= str(i)
                l+=' '
        l+='\n'
        print(l)
        return(l)'''
        return (f' {game.tiles[0]} {game.tiles[1]} {game.tiles[2]} {game.tiles[3]} \n {game.tiles[4]} {game.tiles[5]} {game.tiles[6]} {game.tiles[7]} \n {game.tiles[8]} {game.tiles[9]} {game.tiles[10]} {game.tiles[11]} \n{game.tiles[12]} {game.tiles[13]} {game.tiles[14]} \n')







game = Fifteen()
print(game.tiles)
print(str(game))
for i in game.tiles:
    print(i)
assert str(game) == ' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n13 14 15 \n'

import numpy as np
size = 4
tiles = np.array([i for i in range(1, size ** 2)] + [0])
l = ' '
for i in range(1,len(tiles)):
    if i % 4==0:
        l+= str(i)
        l+='\n'
        l+=' '
    else:
        l+= str(i)
        l+=' '
l+='\n'
print(l)
print(' 1 2 3 4 \n 5 6 7 8 \n 9 10 11 12 \n13 14 15 \n')


