import pygame

from blockClass import Block

class Dirt(Block):
    def __init__(self, block_size, x, y, image):
        super().__init__(block_size, x, y)
        self.texture = True
        img = image
        self.img = pygame.transform.scale(img, (block_size, block_size))