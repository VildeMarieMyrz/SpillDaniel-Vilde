import pygame

class Player:
    def __init__(self, screenSize, charSize):
        img = pygame.image.load("game_assets/character.png")

        self.img = pygame.transform.scale(img, (charSize))

        # Movement
            # position
        self.x = screenSize[0]/2 - charSize[0]/2
        self.y = screenSize[1] - charSize[1]
        self.pos = (self.x,self.y)
            # speed
        self.xSpeed = 0
        self.ySpeed = 0

    def walk(self,speed):
        self.xSpeed += speed

    def jump(self,speed):
        self.ySpeed = -speed

    def fall(self, gravity):
        self.ySpeed += gravity

    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed
        self.pos = (self.x,self.y)