import pygame

from Button import Button
from gui_score import GUI_Score
from label import Label
from level import Level

from globals import AUDIO, BLACK, CAPTION, FPS, GREEN, SCREEN_SIZE, WHITE


class Main:
    def __init__(self):
        # Images config
        GUI_Score.load_numbers()

        # Pygame config
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        # Setting window
        pygame.display.set_caption(CAPTION)
        pygame.display.set_icon(pygame.image.load("..//favicon.ico"))

        # Setting fonts
        self.normal_font = pygame.font.Font("..//Flappy-Bird.ttf", 72)

        # Level
        self.level = Level()

        # Menu
        self.button_play = Button(SCREEN_SIZE[0] / 2 - SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] - SCREEN_SIZE[1] / 10, "Play", self.normal_font)
        self.button_quit = Button(SCREEN_SIZE[0] / 2 + SCREEN_SIZE[0] / 4, SCREEN_SIZE[1] - SCREEN_SIZE[1] / 10, "Quit", self.normal_font)
        self.gameover_label = Label(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2, "Game over", self.normal_font)
        self.best_score_label = Label(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2 + SCREEN_SIZE[1] / 10, "Best ", self.normal_font)
        self.gui_best_score = GUI_Score(SCREEN_SIZE[0] / 2 + 80, SCREEN_SIZE[1] / 2 + SCREEN_SIZE[1] / 10 - 20)

        # Sounds
        self.die_sound = pygame.mixer.Sound(f"..//{AUDIO}hit.wav")
        self.die_sound.set_volume(0.2)

        self.new_play = pygame.mixer.Sound(f"..//{AUDIO}swoosh.wav")
        self.new_play.set_volume(0.2)

        # Game logic variables
        self.running = True
        self.last_frame = 0
        self.deltatime = 0

        # state of the game -> run, end
        self.game_state = "run"


    def run(self):
        """Main game loop : 
        1. FPS calculation
        2. Game updates
        3. Game drawing"""

        # game loop
        while self.running:

            # FPS cap
            self.clock.tick(FPS)

            now = pygame.time.get_ticks()

             # deltatime in seconds
            self.deltatime = (now - self.last_frame) / 1000.0
            self.last_frame = now

            # for loop through the event queue  
            for event in pygame.event.get():

                # Check for QUIT event
                if event.type == pygame.QUIT:
                    self.quit()

                # Check for mouse click event
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if self.button_play.collide(pygame.mouse.get_pos()):
                            self.game_state = "run"
                            self.level = Level()
                            self.new_play.play()

                        elif self.button_quit.collide(pygame.mouse.get_pos()):
                            self.quit()

                # Check for Up event
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.level.bird.jump()

            self.manage_buttons_overlaps()

            self.update()
            self.draw()

            # Update the screen
            pygame.display.update()


    def update(self):
        """Update game components"""

        if self.game_state == "run":
            game_state = self.level.update(self.deltatime)

            if game_state:
                self.game_state = "end"
                
                # manage best score
                self.manage_score()
                # play collision sound
                self.die_sound.play()


    def manage_score(self):
        """Draw best score and save it"""

        self.level.score.save_best_score()


    def draw(self):
        """"Draw game components"""

        if self.game_state in ("run", "start"):
            self.level.draw(self.screen)

        elif self.game_state == "end":
            self.button_play.draw(self.screen)
            self.button_quit.draw(self.screen)
            self.gameover_label.draw(self.screen)
            self.best_score_label.draw(self.screen)
            self.gui_best_score.draw(self.screen, self.level.score.best_score)
        

    def manage_buttons_overlaps(self):
        """Change color if mouse overlaps buttons"""

        if self.game_state == "end":
            if self.button_play.collide(pygame.mouse.get_pos()):
                self.button_play.change_color(BLACK)
            else:
                self.button_play.change_color(WHITE)

            if self.button_quit.collide(pygame.mouse.get_pos()):
                self.button_quit.change_color(BLACK)
            else:
                self.button_quit.change_color(WHITE)


    def quit(self):
        """Quit game"""

        self.running = False
        pygame.quit()
        quit()


if __name__ == '__main__':
    # Initialize Pygame
    pygame.init()
    pygame.font.init()

    # Initialize and run game
    main = Main()
    main.run()