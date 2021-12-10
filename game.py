import pygame
from systemDataFile import System
from playerFile import Player


# System Setup
pygame.init()
sys = System()

# Game Setup

FPS = 60
gravity = 1
player_size = (80,80)
wolrd_ground = sys.screenSize[1]

screen = pygame.display.set_mode((sys.screenSize[0],sys.screenSize[1]))
pygame.display.set_caption('Spill')
player = Player(sys.screenSize,player_size)
clock = pygame.time.Clock()

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
            if event.key == pygame.K_SPACE:
                player.jump(18)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.walk(-10)
            if event.key == pygame.K_LEFT:
                player.walk(10)

    
    # Movement
    player.move()

    # Physics
    player.fall(gravity)

        # Ground
    if player.y > wolrd_ground - player_size[1]:
        player.y =  wolrd_ground - player_size[1]
        player.ySpeed = 0

    # Display
    screen.fill(background_colour)

    screen.blit(player.img,(player.pos))

    pygame.display.update()
    clock.tick(FPS)