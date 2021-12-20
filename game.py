import pygame, sys, pickle
from cameraClass import Camera
from planetClass import Planet
from systemDataFile import System
from playerClass import Player
from chunkLoaderClass import ChunkLoader


# System Setup
pygame.init()
system = System()
planet_name = "level_1_test"

# Game Setup
FPS = 60
gravity = 1
player_size = (80,80)
block_size = 80
chunk_size = 16
chunk_height = 64


# Load images
images = {
    "dirt" : pygame.image.load("game_assets/block.png")
    }

screen = pygame.display.set_mode((system.screen_size[0],system.screen_size[1]))
pygame.display.set_caption('Lost in Space')
player = Player(system.screen_size,player_size)
clock = pygame.time.Clock()
cam = Camera()
planet = Planet(chunk_size, chunk_height, block_size, grid=pickle.load(open("planets/"+planet_name+".planet", "rb")))
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
        # Create rects
    rects = []

    for e in range(len(chunks.chunks)):
        for row in chunks.chunks[e]:
            for block in row:
                if block.texture:
                    rects.append(pygame.Rect(block.x, block.y,block.size,block.size))
           
        # Move
    player.move(rects)

        # Move Camera
    cam.scroll(player.rect.x, player.rect.y)

    # Rendering
    cam_centre = int((-1*(cam.x - system.screen_width//2)//block_size//chunk_size ))
    shloud_render = [cam_centre-1, cam_centre, cam_centre+1]

        # Generate chunks if missing
    for chunk in (shloud_render):
        if chunk < 0:
            if (chunk*-1) > len(planet.negative_chunks):
                planet.make_chunk(chunk)
        else:
            if chunk >= len(planet.positive_chunks):
                planet.make_chunk(chunk)

        # Remove Chunks Not in Should Render
    for chunk in chunks.loaded_chunks:
        if chunk not in shloud_render:
            chunks.remove(chunk)

        # Load Chunks in Should Render
    for chunk in (shloud_render):
        if chunk < 0:
            if chunk not in chunks.loaded_chunks:
                chunks.load(planet.negative_chunks[(chunk*-1)-1],(chunk))
        else:
            if chunk not in chunks.loaded_chunks:
                chunks.load(planet.positive_chunks[chunk],chunk)

    # Physics
    player.fall(gravity)

    # Display
        # Background
    screen.fill(background_colour)

        # Player
    screen.blit(player.img,(player.rect.x + cam.x ,player.rect.y + cam.y))

        # Blocks
    for chunk in chunks.chunks:
        for row in chunk:
            for block in row:
                if block.texture:
                    screen.blit(block.img, (block.x + cam.x, block.y + cam.y))

    pygame.display.update()
    clock.tick(FPS)