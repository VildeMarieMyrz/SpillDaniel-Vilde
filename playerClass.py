import pygame

class Player:
    def __init__(self, screen_size, char_size):
        img = pygame.image.load("game_assets/character.png")
        self.img = pygame.transform.scale(img, (char_size))
        self.rect = self.img.get_rect(center=(screen_size[0]/2,screen_size[1] * 0.8))

        # Movement
        self.x_speed = 0
        self.y_speed = 0
        self.can_jump = False


    def walk(self,speed):
        self.x_speed += speed

    def jump(self,speed):
        if self.can_jump:
            self.y_speed = -speed

    def fall(self, gravity):
        self.y_speed += gravity

    def move(self,rects):
        self.can_jump = False

        # X-movement and collisions
        self.rect.x += self.x_speed
        hit_list = self.collision_test(rects)   
        for rect in hit_list:
            if self.x_speed > 0:
                self.rect.right = rect.left
            elif self.x_speed < 0:   
                self.rect.left = rect.right

        # Y-movement and collisions
        self.rect.y += self.y_speed
        hit_list = self.collision_test(rects)
        for rect in hit_list:
            if self.y_speed > 0:
                self.rect.bottom = rect.top
                self.y_speed = 0
                self.can_jump = True

            elif self.y_speed < 0:   
                self.rect.top = rect.bottom
                self.y_speed = 0
                

    def collision_test(self, rects):
        hit_list = []
        for rect in rects:
            if self.rect.colliderect(rect):
                hit_list.append(rect)
        return hit_list