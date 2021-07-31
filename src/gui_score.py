import pygame

from globals import SCREEN_SIZE, SPRITES


class GUI_Score:
    numbers = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = GUI_Score.numbers[0].get_width()


    @classmethod
    def load_numbers(cls):
        """Load numbers as pygame images"""

        GUI_Score.numbers = [pygame.image.load(f"..//{SPRITES}{n}.png") for n in range(0, 10)]


    def draw(self, screen, n=0):
        """Draw numbers"""

        l = [0, n] if n < 10 else [int(e) for e in list(str(n))]

        for i, e in enumerate(l):
            screen.blit(GUI_Score.numbers[e], (self.x - self.width * (len(l) - i) + self.width, self.y))