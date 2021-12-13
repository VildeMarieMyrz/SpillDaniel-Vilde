import pygame
from airClass import Air
from dirtBlockClass import Dirt

class Chunk:

    def __init__ (self, pos, grid, chunk_size, block_size):

        self.pos = pos
        self.size = chunk_size
        self.grid = []

        for x in range(self.size):
            block_row = []
            for y in range(self.size):
                if grid[x][y] == 0:
                    block_row.append(Air(block_size, x*block_size, y*block_size))
                elif grid[x][y] == 1:
                    block_row.append(Dirt(block_size, x*block_size, y*block_size))
            self.grid.append(block_row)

    def add(self,block, x ,y):
        print(x, y)
        self.grid[x][y] = block