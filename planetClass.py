import pygame

from chunkClass import Chunk

class Planet:

    # Må få inn grid med et antall rows som går opp i 16.
    # Alle rader må være like lange
    # Flipper gridet 90 grader

    def __init__ (self, grid, chunk_size, screen_size, block_size):
        
        self.chunks = []

        for chunk_pos in range(len(grid[0])//16):
            chunk_grid = []
            for e in range(16):
                chunk_row = []
                for block in grid[e + chunk_pos * chunk_size]:
                    chunk_row.append(block)
                chunk_grid.append(chunk_row)
            self.chunks.append(Chunk(chunk_pos, chunk_grid, chunk_size, screen_size, block_size))