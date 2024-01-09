# author: Curran Advani
# date: Mar 17, 2023
# file: game.py
# input: users specific moves for the games
# output: the puzzle game, fifteen in gui format

import numpy as np
import tkinter as tk

class FifteenGUI:

    def __init__(self, master, size=4): #The constructor method initializes the FifteenGUI object
        self.master = master
        self.size = size
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])
        self.empty_pos = size ** 2 - 1
        self.draw()

    def draw(self): #creates a tk.Frame object for the tiles, and then creates tk.Label objects for each tile
        self.tiles_frame = tk.Frame(self.master)
        self.tiles_frame.pack(side=tk.TOP, padx=10, pady=10)

        for i in range(self.size):
            for j in range(self.size):
                index = i * self.size + j
                if self.tiles[index] == 0:
                    label = tk.Label(self.tiles_frame, text='', width=3, height=2, bg='lightgrey')
                else:
                    label = tk.Label(self.tiles_frame, text=str(self.tiles[index]), width=3, height=2, bg='white')
                label.grid(row=i, column=j, padx=2, pady=2)
                label.bind('<Button-1>', lambda e, index=index: self.transpose(index))

        self.message = tk.StringVar() #update message and set
        self.message.set('Click a tile to move it')
        self.status_bar = tk.Label(self.master, textvariable=self.message, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        self.quit_button = tk.Button(self.master, text='Quit', command=self.master.quit)
        self.quit_button.pack(side=tk.RIGHT, padx=5, pady=5)

        self.shuffle_button = tk.Button(self.master, text='Shuffle', command=self.shuffle) #shuffle tiles basically connected to button
        self.shuffle_button.pack(side=tk.LEFT, padx=5, pady=5)

    def transpose(self, index): #takes the index of the clicked tile as an argument, and transposes the tile with the empty tile if they are adjacent
        pos = np.where(self.tiles == self.tiles[index])[0][0]
        if self.is_valid_move(pos):
            self.tiles[pos], self.tiles[self.empty_pos] = self.tiles[self.empty_pos], self.tiles[pos]
            self.empty_pos = pos
            self.update()
            self.update_status_bar()

            if self.is_solved():
                self.message.set('Congratulations! You solved the puzzle.')

    def is_valid_move(self, pos):
        empty_row = self.empty_pos // self.size
        empty_col = self.empty_pos % self.size
        row = pos // self.size
        col = pos % self.size
        if (empty_row == row and abs(empty_col - col) == 1) or (empty_col == col and abs(empty_row - row) == 1):
            return True
        else:
            return False

    def shuffle(self): #method shuffles the tiles randomly, updates the empty position and calls the update method to update the GUI
        np.random.shuffle(self.tiles)
        self.empty_pos = np.where(self.tiles == 0)[0][0]
        self.update()
        self.message.set('Click a tile to move it')

    def update(self): #method iterates through all the tiles and updates their text and background color based on their values
        for i in range(self.size):
            for j in range(self.size):
                index = i * self.size + j
                if self.tiles[index] == 0:
                    text = ''
                    bg = 'lightgrey'
                else:
                    text = str(self.tiles[index])
                    bg = 'white'
                self.tiles_frame.grid_slaves(row=i, column=j)[0].configure(text=text, bg=bg)

    def is_solved(self):
        x = 0
        while x < len(self.tiles):
            x += 1
            if self.tiles[x] < x or self.tiles[x] > x:
                return False
        return True

    def update_status_bar(self): #Updates the status bar with information about the current puzzle state.

        if self.is_solved():
            self.message.set('Congratulations! You solved the puzzle.')
        else:
            self.message.set('Click a tile to move it')
root = tk.Tk()
app = FifteenGUI(root)
root.mainloop()
