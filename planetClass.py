import pygame
from blockClass import Block

from chunkClass import Chunk

class Planet:

    def __init__ (self, chunk_size, chunk_height, block_size):
        self.chunk_height = chunk_height
        self.chunks = []
        self.chunk_size = chunk_size
        self.block_size = block_size
        
    
    def add_block(self, block, x , y):
        chunk_pos = (x//self.block_size)/self.chunk_size
        chunk_index = None

        for e in range(len(self.chunks)):
            if self.chunks[e].pos == chunk_pos:
                chunk_index = e

        if chunk_index == None:
            self.chunks.append(self.make_chunk(chunk_pos))
            chunk_index = len(self.chunks)-1
        self.chunks[chunk_index].add(block, int((x//self.block_size) - self.chunk_size * chunk_pos), y//self.block_size)


    def make_chunk(self, chunk_pos):
        chunk_grid = []
        for e in range(self.chunk_size):
            chunk_row = []
            for i in range(self.chunk_size):
                chunk_row.append(0)
            chunk_grid.append(chunk_row)
        return Chunk(chunk_pos, chunk_grid, self.chunk_size, self.block_size)