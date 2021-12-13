import pygame
from airClass import Air
from dirtBlockClass import Dirt

class Chunk:

    def __init__ (self, chunk_pos, chunk_size, block_size):

        self.block_size = block_size
        self.pos = chunk_pos
        self.size = chunk_size
        self.grid = []

        for x in range(self.size):
            chunk_row = []
            for y in range(self.size):
                chunk_row.append(Air(block_size, x*block_size, y*block_size))
            self.grid.append(chunk_row)

    def add(self,block, x ,y):
        if block == 0:
            self.grid[x][y] = (Air(self.block_size, x*self.block_size, y*self.block_size))
        if block == 1:
            self.grid[x][y] = (Dirt(self.block_size, x*self.block_size, y*self.block_size))