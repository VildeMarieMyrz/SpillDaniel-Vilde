import pygame

class Planet:

    def __init__ (self, chunk_size, chunk_height, block_size, positive_chunks=[], negative_chunks=[]):
        self.chunk_height = chunk_height
        self.positive_chunks = positive_chunks
        self.negative_chunks = negative_chunks
        self.chunk_size = chunk_size
        self.block_size = block_size
        
    
    def add_block(self, block, x , y):
        chunk_pos = (x//self.block_size)/self.chunk_size

        if chunk_pos < 0:
            while chunk_pos > len(self.negative_chunks):
                self.positive_chunks.append(self.make_chunk)
            self.negative_chunks[(x*-1)//chunk_pos//self.block_size,y//self.block_size] = block
        else:
            while chunk_pos >= len(self.positive_chunks):
                self.positive_chunks.append(self.make_chunk)
            self.positive_chunks[x//chunk_pos//self.block_size,y//self.block_size] = block

    def make_chunk(self):
        chunk = []
        for e in range(self.chunk_size):
            chunk_row = []
            for i in range(self.chunk_size):
                chunk_row.append(0)
            chunk.append(chunk_row)
        return chunk