import pygame

class Planet:

    def __init__ (self, chunk_size, block_size, grid = None):
        self.positive_chunks = []
        self.negative_chunks = []
        self.chunk_size = chunk_size
        self.block_size = block_size

        if grid != None:
            self.restore_world(grid)
        
        # changes the block at pos x, y to the block input. If a chunk does not exist in pos x, y one is made.
    def add_block(self, block, x , y):
        chunk_pos = ((x//self.block_size)//self.chunk_size, (y//self.block_size)//self.chunk_size)
        self.make_chunk(chunk_pos)
        if chunk_pos[0] < 0:
            if chunk_pos[1] < 0:
                self.negative_chunks[chunk_pos[0]*-2-1][chunk_pos[1]*-1-1][(x*-1)//self.block_size+(chunk_pos[0]+1)*self.chunk_size][y*-1//self.block_size+(chunk_pos[1]+1)*self.chunk_size] = block
            else:
                self.negative_chunks[chunk_pos[0]*-2-2][chunk_pos[1]][(x*-1)//self.block_size+(chunk_pos[0]+1)*self.chunk_size][y//self.block_size-chunk_pos[1]*self.chunk_size] = block
        else:
            if chunk_pos[1] < 0:
                self.positive_chunks[chunk_pos[0]*2+1][chunk_pos[1]*-1-1][x//self.block_size-chunk_pos[0]*self.chunk_size][y*-1//self.block_size+chunk_pos[1]*self.chunk_size] = block
            else:
                self.positive_chunks[chunk_pos[0]*2][chunk_pos[1]][x//self.block_size-chunk_pos[0]*self.chunk_size][y//self.block_size-chunk_pos[1]*self.chunk_size] = block

    # generates a blank chunk
    def new_chunk(self):
        chunk = []
        for e in range(self.chunk_size):
            chunk_row = []
            for i in range(self.chunk_size):
                chunk_row.append(0)
            chunk.append(chunk_row)
        return chunk
    
    # make every chunk not already made between 0,0 and chunk position
    def make_chunk (self, chunk_position):
        if chunk_position[0] < 0:
            self.make_negative_chunk(chunk_position)
        elif chunk_position[0] >= 0:
            self.make_positive_chunk(chunk_position)

    # adds positive chunks on the x coordinate until chunk_pos[0] (x), then adds blank chunks until chunk_pos[1] (y) is reached
    def make_positive_chunk(self, chunk_position):
        while(len(self.positive_chunks)//2 <= chunk_position[0]):
            self.positive_chunks.append([])
        if chunk_position[1] < 0:
            self.make_chunk_northeast(chunk_position)
        elif chunk_position[1] >= 0:
            self.make_chunk_southeast(chunk_position)
    
    # adds positive chunks on the x coordinate until chunk_pos[0] (x), then adds blank chunks until chunk_pos[1] (y) is reached
    def make_negative_chunk(self, chunk_position):
        while(len(self.negative_chunks)//2 < chunk_position[0]*-1):
            self.negative_chunks.append([])
        if chunk_position[1] < 0:
            self.make_chunk_northwest(chunk_position)
        elif chunk_position[1] >= 0:
            self.make_chunk_southwest(chunk_position)
    
    # adds blank chunks until chunk_pos[1] is reached
    def make_chunk_southeast(self, chunk_position):
        while(len(self.positive_chunks[chunk_position[0]*2]) <= chunk_position[1]):
            self.positive_chunks[chunk_position[0]*2].append(self.new_chunk())

    # adds blank chunks until chunk_pos[1] is reached
    def make_chunk_northeast(self, chunk_position):
        while(len(self.positive_chunks[chunk_position[0]*2 + 1]) < chunk_position[1]*-1):
            self.positive_chunks[chunk_position[0]*2 + 1].append(self.new_chunk())

    # adds blank chunks until chunk_pos[1] is reached
    def make_chunk_southwest(self, chunk_position):
        while(len(self.negative_chunks[chunk_position[0]*-2-2]) <= chunk_position[1]):
            self.negative_chunks[chunk_position[0]*-2-2].append(self.new_chunk())

    # adds blank chunks until chunk_pos[1] is reached
    def make_chunk_northwest(self, chunk_position):
        while(len(self.negative_chunks[chunk_position[0]*-2-1]) < chunk_position[1]*-1):
            self.negative_chunks[chunk_position[0]*-2-1].append(self.new_chunk())

    # loades a saved world
    def restore_world(self, grid):
        for chunk in grid[0]:
            self.positive_chunks.append(chunk)
        for chunk in grid[1]:
            self.negative_chunks.append(chunk)