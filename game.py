import pygame, sys, pickle
from cameraClass import Camera
from planetClass import Planet
from systemDataFile import System
from playerClass import Player
from chunkLoaderClass import ChunkLoader


# System Setup
pygame.init()
system = System()
planet_name = "jorden"

# Game Setup
FPS = 60
gravity = 1
player_size = (80,80)
block_size = 80
chunk_size = 16


# Load images
images = {
    "dirt" : pygame.image.load("game_assets/block.png")
    }

screen = pygame.display.set_mode((system.screen_size[0],system.screen_size[1]))
pygame.display.set_caption('Lost in Space')
player = Player(system.screen_size,player_size)
clock = pygame.time.Clock()
cam = Camera(system.screen_width, system.screen_height, player_size)
planet = Planet(chunk_size, block_size, grid=pickle.load(open("planets/"+planet_name+".planet", "rb")))
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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
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