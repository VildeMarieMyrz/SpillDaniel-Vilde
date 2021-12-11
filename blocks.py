import pygame

class Block:
    def __init__(self, screen_size, size, x, y):
        img = pygame.image.load("game_assets/block.png")

        self.img = pygame.transform.scale(img, (size,size))

        self.x = x
        self.y = y
        self.pos = (self.x, self.y)