from typing import Text
import pygame, sys
from cameraClass import Camera
from chunkLoaderClass import ChunkLoader
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

screen = pygame.display.set_mode((system.screen_width,system.screen_height))
pygame.display.set_caption('Lost in Space')
cam = Camera()
planet = Planet(chunk_size, chunk_height, block_size)
chunks = ChunkLoader(chunk_size, block_size)


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

    # Rendering
    cam_centre = (cam.x//block_size//chunk_size + system.screen_width//2)
    shloud_render = [cam_centre-1, cam_centre, cam_centre+1]

        # Remove Chunks
    for chunk in chunks.loaded_chunks:
        if chunk not in shloud_render:
            chunks.remove(chunk)

        # Load Chunks
    for chunk in (shloud_render):
        if chunk < 0:
            if chunk not in chunks.loaded_chunks:
                chunks.load(planet.negative_chunks[(chunk*-1)-1],(chunk*-1))
        else:
            if chunk not in chunks.loaded_chunks:
                chunks.load(planet.positive_chunks[chunk],chunk)

    # Display
        # Background
    screen.fill(background_colour)

        # Blocks
    for chunk in chunks.chunks:
        for row in chunk:
            for block in row:
                if block.texture:
                    screen.blit(block.img, (block.x + cam.x, block.y + cam.y))

    pygame.display.update()
    clock.tick(FPS)