import pygame

from globals import SCREEN_SIZE, SPRITES, VEL_X


class Floor:
    img = pygame.image.load(f"..//{SPRITES}base.png")

    def __init__(self, x=0):
        self.x = x
        self.y = Floor.img.get_height()
        self.image = Floor.img

        # Collisions
        self.rect = Floor.img.get_rect()


    def update(self, deltatime):
        self.x -= VEL_X * deltatime

        # Update rect
        self.rect.update(self.x, SCREEN_SIZE[1] - self.y, self.rect.width, self.rect.height)


    def draw(self, screen):
        screen.blit(self.image, self.rect)