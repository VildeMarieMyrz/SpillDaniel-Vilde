import pygame
from blocks import Block
from systemDataFile import System
from playerFile import Player


# System Setup
pygame.init()
sys = System()

# Game Setup

FPS = 60
gravity = 1
player_size = (80,80)
block_size = 80

screen = pygame.display.set_mode((sys.screen_size[0],sys.screen_size[1]))
pygame.display.set_caption('Spill')
player = Player(sys.screen_size,player_size)
clock = pygame.time.Clock()

# temp blocks
blocks = []
blocks.append(Block(sys.screen_size,block_size,sys.screen_size[0]/2,sys.screen_size[1]-block_size))
blocks.append(Block(sys.screen_size,block_size,sys.screen_size[0]/2-block_size,sys.screen_size[1]-block_size))
blocks.append(Block(sys.screen_size,block_size,sys.screen_size[0]/2+block_size,sys.screen_size[1]-block_size))
blocks.append(Block(sys.screen_size,block_size,sys.screen_size[0]/2+2*block_size,sys.screen_size[1]-2*block_size))
blocks.append(Block(sys.screen_size,block_size,sys.screen_size[0]/2-2*block_size,sys.screen_size[1]-2*block_size))
blocks.append(Block(sys.screen_size,block_size,sys.screen_size[0]/2,sys.screen_size[1]-5*block_size))
blocks.append(Block(sys.screen_size,block_size,sys.screen_size[0]/2+block_size,sys.screen_size[1]-5*block_size))

rects = []
for block in blocks:
    rects.append(block.img.get_rect(topleft=block.pos))

# Colors    
background_colour = (234, 212, 252)

running = True
while running:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.walk(10)
            if event.key == pygame.K_LEFT:
                player.walk(-10)
            if event.key == pygame.K_UP:
                player.jump(18)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.walk(-10)
            if event.key == pygame.K_LEFT:
                player.walk(10)

    
    # Movement
    player.move(rects)

    # Physics
    player.fall(gravity)

        # Collisions

    # Display
    screen.fill(background_colour)

    screen.blit(player.img,(player.rect.x,player.rect.y))

    for block in blocks:
        screen.blit(block.img,block.pos)

    pygame.display.update()
    clock.tick(FPS)