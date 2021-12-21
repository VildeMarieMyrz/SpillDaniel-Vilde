from airBlockClass import Air
from blockClass import Block
from dirtBlockClass import Dirt

class ChunkLoader:

    def __init__ (self, chunk_size, block_size, images):

        self.block_size = block_size
        self.chunk_size = chunk_size
        
        self.chunks = []
        self.loaded_chunks = []

        self.images = images

# adds chunk to self.chunks and self.loaded_chunks
    def load(self, chunk, chunk_pos):
        loaded_chunk = []
        for y in range(len(chunk)):
            row = []
            for x in range(len(chunk[y])):
                if chunk[x][y] == 0:
                    row.append(Air(self.block_size, x * self.block_size + self.chunk_size*chunk_pos*self.block_size, y * self.block_size))
                elif chunk[x][y] == 1:
                    row.append(Dirt(self.block_size, x * self.block_size + self.chunk_size*chunk_pos*self.block_size, y * self.block_size, self.images.get("dirt")))
            loaded_chunk.append(row)
        self.chunks.append(loaded_chunk)
        self.loaded_chunks.append(chunk_pos)

# removes chunk from  self.chunks and self.loaded_chunks
    def remove (self, chunk_pos):
        for e in range(len(self.loaded_chunks)):
            if self.loaded_chunks[e] == chunk_pos:
                self.loaded_chunks.pop(e)
                self.chunks.pop(e)
                break

# changes the type of a block in self.chunks
    def add_block(self, block, x , y):
        chunk_pos = (x//self.block_size)//self.chunk_size
        for e in range(len(self.loaded_chunks)):
            if self.loaded_chunks[e] == chunk_pos:
                if block == 0:
                    self.chunks[e][x//self.block_size-chunk_pos*self.chunk_size][y//self.block_size] = Air(self.block_size, (x - x % self.block_size), (y - y % self.block_size))
                elif block == 1:
                    self.chunks[e][x//self.block_size-chunk_pos*self.chunk_size][y//self.block_size] = Dirt(self.block_size, (x - x % self.block_size), (y - y % self.block_size), self.images.get("dirt"))
                break


