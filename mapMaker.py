from typing import Text
import pygame, sys, time
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
clock = pygame.time.Clock()

# Load images
images = {
    "dirt" : pygame.image.load("game_assets/block.png")
    }

screen = pygame.display.set_mode((system.screen_width,system.screen_height))
pygame.display.set_caption('Lost in Space')
cam = Camera()
planet = Planet(chunk_size, block_size)
chunks = ChunkLoader(chunk_size, block_size, images)


# Colors    
background_colour = (234, 212, 252)

while True:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
                save(planet, screen, system.screen_width, system.screen_height)
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

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
                chunks.add_block(1, pygame.mouse.get_pos()[0] - cam.x, pygame.mouse.get_pos()[1] - cam.y)
            if event.button == 3:
                planet.add_block(0, pygame.mouse.get_pos()[0] - cam.x, pygame.mouse.get_pos()[1] - cam.y)
                chunks.add_block(0, pygame.mouse.get_pos()[0] - cam.x, pygame.mouse.get_pos()[1] - cam.y)
    
    cam.move()

    # Rendering
    cam_x = int(-1*(cam.x - system.screen_width//2)//block_size//chunk_size)
    cam_y = int(-1*(cam.y - system.screen_height//2)//block_size//chunk_size)
    should_render = []
    for x in range(3):
        for y in range(3):
            should_render.append((cam_x + x-1, cam_y + y-1))

        # Generate chunks if missing
    for chunk in should_render:
        planet.make_chunk(chunk) # does not ad chunk if a chunk already exists in this position

        # Remove Chunks Not in Should Render
    for chunk in chunks.loaded_chunks:
        if chunk not in should_render:
            chunks.remove(chunk)

        # Load Chunks in Should Render
    for chunk in (should_render):
        if chunk not in chunks.loaded_chunks:
            if chunk[0] < 0:
                if chunk[1] < 0: 
                    chunks.load(planet.negative_chunks[chunk[0]*-2-1][chunk[1]*-1-1],chunk)
                else:
                    chunks.load(planet.negative_chunks[chunk[0]*-2-2][chunk[1]],chunk)
            else:
                if chunk[1] < 0: 
                    chunks.load(planet.positive_chunks[chunk[0]*2+1][chunk[1]*-1-1],chunk)
                else:
                    chunks.load(planet.positive_chunks[chunk[0]*2][chunk[1]],chunk)

    # Display
        # Background
    screen.fill(background_colour)

        # Blocks
    for chunk in chunks.chunks:
        for row in chunk:
            for block in row:
                if block.texture:
                    screen.blit(block.img, (block.x + cam.x, block.y + cam.y))

        # Text boxes

    pygame.display.update()
    clock.tick(FPS)