from board import Board
from player import Player

playa = Player("Bob", "X")
bd = Board()
bd.show()
print("After setting A1")
bd.set("A2", "X")
bd.show()