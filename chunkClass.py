import pygame
from dirtBlockClass import Dirt

class Chunk:

    def __init__ (self, pos, grid, chunk_size, screen_size, block_size):

        self.pos = pos
        self.size = chunk_size
        self.grid = []

        for x in range(16):
            block_row = []
            for y in range(16):
                if grid[x][y] == 1:
                    block_row.append(Dirt(screen_size, block_size, x*block_size, y*block_size))
            self.grid.append(block_row)