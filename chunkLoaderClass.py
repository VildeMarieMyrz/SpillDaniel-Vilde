from airBlockClass import Air
from dirtBlockClass import Dirt

class ChunkLoader:

    def __init__ (self, chunk_size, block_size):

        self.block_size = block_size
        self.chunk_size = chunk_size
        
        self.chunks = []
        self.loaded_chunks = []


    def load(self, chunk, chunk_pos):
        loaded_chunk = []
        for y in range(len(chunk)):
            row = []
            for x in len(chunk[y]):
                if chunk[x][y] == 0:
                    row.append(Air(self.block_size, x * self.block_size + self.chunk_size*chunk_pos, y * self.block_size))
                elif chunk[x][y] == 1:
                    row.append(Dirt(self.block_size, x * self.block_size + self.chunk_size*chunk_pos, y * self.block_size))
            loaded_chunk.append(row)
        self.chunks.append(loaded_chunk)
        self.loaded_chunks.append(chunk_pos)

    def remove (self):
        pass