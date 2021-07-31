import pygame

from globals import PIPE_SPACING, SPRITES, VEL_X


class Pipe:
    # Images of pipes
    down_img = pygame.image.load(f"..//{SPRITES}pipe-red.png")
    top_img = pygame.transform.rotate(down_img, 180)

    def __init__(self, x, y):
        self.x = x
        self.y = y # random y top pipe

        # Collisions
        self.rect_top = Pipe.top_img.get_rect()
        self.rect_down = Pipe.down_img.get_rect()


    def update(self, deltatime):
        self.x -= VEL_X * deltatime

        # Update rects
        self.rect_top.update(self.x, self.y - self.rect_top.height, self.rect_top.width, self.rect_top.height)
        self.rect_down.update(self.x, self.y + PIPE_SPACING, self.rect_down.width, self.rect_down.height)


    def draw(self, screen):
        """Draw two pipes"""

        screen.blit(Pipe.top_img, self.rect_top)
        screen.blit(Pipe.down_img, self.rect_down)