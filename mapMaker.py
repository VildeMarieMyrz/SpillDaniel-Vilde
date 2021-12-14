from typing import Text
import pygame, sys
from cameraClass import Camera
from planetClass import Planet
from systemDataFile import System
from savePlanet import save


# System Setup
pygame.init()
system = System()
FPS = 60

# Game Setup
gravity = 1
player_size = (80,80)
block_size = 80
chunk_size = 16
chunk_height = 64
clock = pygame.time.Clock()

screen = pygame.display.set_mode((system.screen_size[0],system.screen_size[1]))
pygame.display.set_caption('Lost in Space')
cam = Camera()
planet = Planet(chunk_size, chunk_height, block_size)


# Colors    
background_colour = (234, 212, 252)

while True:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            system.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                cam.move_right(True)
            if event.key == pygame.K_LEFT:
                cam.move_left(True)
            if event.key == pygame.K_UP:
                cam.move_up(True)
            if event.key == pygame.K_DOWN:
                cam.move_down(True)
            if event.key == pygame.K_s:
                save(planet)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                cam.move_right(False)
            if event.key == pygame.K_LEFT:
                cam.move_left(False)
            if event.key == pygame.K_UP:
                cam.move_up(False)
            if event.key == pygame.K_DOWN:
                cam.move_down(False)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                planet.add_block(1, pygame.mouse.get_pos()[0] - cam.x, pygame.mouse.get_pos()[1] - cam.y)
            if event.button == 3:
                planet.add_block(0, pygame.mouse.get_pos()[0] - cam.x, pygame.mouse.get_pos()[1] - cam.y)
    cam.move()

    # Display
        # Background
    screen.fill(background_colour)

        # Blocks
    for chunk in planet.chunks:
        for row in chunk.grid:
            for block in row:
                if block.texture:
                    screen.blit(block.img, (block.x + chunk.size * block_size * chunk.pos + cam.x, block.y + cam.y))

    pygame.display.update()
    clock.tick(FPS)