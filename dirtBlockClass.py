import pygame

from blockClass import Block

class Dirt(Block):
    def __init__(self, block_size, x, y):
        super().__init__(block_size, x, y)
        self.texture = True
        img = pygame.image.load("game_assets/block.png")
        self.img = pygame.transform.scale(img, (block_size, block_size))