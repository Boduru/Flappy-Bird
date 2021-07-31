import pygame
import random

from bird import Bird
from gui_score import GUI_Score
from pipe import Pipe
from floor import Floor
from score import Score

from globals import AUDIO, PIPE_DISTANCE, SCREEN_SIZE, SPRITES


class Level:
    def __init__(self):
        self.background = pygame.image.load(f"..//{SPRITES}background-night.png")

        self.bird = Bird()
        self.floors = [Floor(0), Floor(SCREEN_SIZE[0])]
        self.pipes = [self.new_pipe()]

        self.score = Score()
        self.target = 0 # pipe target
        self.gui_score = GUI_Score(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 10)

        # Sound
        self.point_sound = pygame.mixer.Sound(f"..//{AUDIO}point.wav")
        self.point_sound.set_volume(0.2)


    def new_pipe(self, x=400):
        """Create random pipe from screen top"""

        return Pipe(x, random.randint(0, SCREEN_SIZE[1] / 2))


    def manage_pipes(self):
        """Create new pipes and delete out ones"""

        if self.pipes[0].x < -Pipe.top_img.get_width():
            # delete border pipes
            del self.pipes[0]
            # change target number
            self.target = 0

        while len(self.pipes) < 2:
            # add as many pipes as needed (1 each time)
            x = self.pipes[len(self.pipes)-1].x + PIPE_DISTANCE
            self.pipes.append(self.new_pipe(x))


    def manage_floors(self):
        """Create new floors and delete out ones"""

        if self.floors[0].x < -Floor.img.get_width():
            self.floors[0].x = SCREEN_SIZE[0] - 1
            # swap elements in list
            self.floors[0], self.floors[1] = self.floors[1], self.floors[0]


    def update(self, deltatime):
        """Update game components"""

        self.manage_pipes()
        self.manage_floors()

        for pipe in self.pipes:
            pipe.update(deltatime)

        for floor in self.floors:
            floor.update(deltatime)

        self.bird.update(deltatime)

        self.manage_score()

        return self.check_collisions()


    def manage_score(self):
        """Update score"""

        if self.bird.x + self.bird.rect.width / 2 >= self.pipes[0].x + self.pipes[0].rect_top.width / 2 and self.target == 0:
            self.score.update_score()
            self.target = 1

            # play score increasing sound
            self.point_sound.play()


    def check_collisions(self):
        """Collision detection"""

        for pipe in self.pipes:
            if self.bird.rect.colliderect(pipe.rect_top) or self.bird.rect.colliderect(pipe.rect_down):
                return True

        for floor in self.floors:
            if self.bird.rect.colliderect(floor.rect):
                return True

        return False


    def draw(self, screen):
        """"Draw game components"""

        screen.blit(self.background, (0, 0))
        
        for pipe in self.pipes:
            pipe.draw(screen)

        for floor in self.floors:
            floor.draw(screen)

        self.bird.draw(screen)

        self.gui_score.draw(screen, self.score.curr_score)