import pygame

class Dirt:
    def __init__(self, screen_size, block_size, x, y):
        img = pygame.image.load("game_assets/block.png")
        self.img = pygame.transform.scale(img, (block_size, block_size))
        self.x = x
        self.y = y
        self.size = block_size