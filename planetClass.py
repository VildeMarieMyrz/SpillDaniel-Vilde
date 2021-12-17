import pygame

class Planet:

    def __init__ (self, chunk_size, chunk_height, block_size, grid = None):
        self.chunk_height = chunk_height
        self.positive_chunks = []
        self.negative_chunks = []
        self.chunk_size = chunk_size
        self.block_size = block_size

        if grid != None:
            self.restore_world(grid)
        
    
    def add_block(self, block, x , y):
        chunk_pos = (x//self.block_size)//self.chunk_size

        if chunk_pos < 0:
            while chunk_pos > len(self.negative_chunks):
                self.make_chunk(chunk_pos)
            self.negative_chunks[chunk_pos*-1-1][(x*-1)//self.block_size+(chunk_pos+1)*self.chunk_size][y//self.block_size] = block
        else:
            while chunk_pos >= len(self.positive_chunks):
                self.make_chunk(chunk_pos)
            self.positive_chunks[chunk_pos][x//self.block_size-chunk_pos*self.chunk_size][y//self.block_size] = block

    def make_chunk(self, chunk_position):
        chunk = []
        for e in range(self.chunk_size):
            chunk_row = []
            for i in range(self.chunk_size):
                chunk_row.append(0)
            chunk.append(chunk_row)

        if chunk_position < 0:
            self.negative_chunks.append(chunk)
        else:
            self.positive_chunks.append(chunk)

    def restore_world(self, grid):
        for chunk in grid[0]:
            self.positive_chunks.append(chunk)
        for chunk in grid[1]:
            self.negative_chunks.append(chunk)