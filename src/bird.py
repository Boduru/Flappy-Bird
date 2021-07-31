import pygame

from globals import AUDIO, GRAVITY, JUMP_FORCE, MAX_VEL_Y, SCREEN_SIZE, SPRITES


class Bird:
    def __init__(self):
        # Physics
        self.x = 20
        self.y = 100
        self.vspeed = 0

        # Images controls
        self.images = []
        self.curr_img = 0
        self.img_time_count = 0
        self.img_time_change = 2
        self.img_anim_speed = 20

        self.load_images()

        # Collisions
        self.rect = self.images[0].get_rect()

        # Sound
        self.jump_sound = pygame.mixer.Sound(f"..//{AUDIO}wing.wav")
        self.jump_sound.set_volume(0.2)


    def load_images(self):
        """Load images"""

        for img in ["bluebird-downflap.png", "bluebird-midflap.png", "bluebird-upflap.png"]:
            self.images.append(pygame.image.load(f"..//{SPRITES}{img}"))


    def update(self, deltatime):
        """Update bird"""

        self.update_wings(deltatime)
        self.update_vspeed()
        self.move(deltatime)
        self.update_rect()


    def update_wings(self, deltatime):
        """"Update wings animation"""

        # Update timer
        self.img_time_count += self.img_anim_speed * deltatime

        if self.img_time_count > self.img_time_change:
            # Change image
            self.img_time_count = 0
            self.curr_img += 1
            
            if self.curr_img >= len(self.images):
                # Get the first image if len of list reached
                self.curr_img = 0


    def update_vspeed(self):
        """Update vertical speed (gravity)
        and cap it to max value"""

        self.vspeed += GRAVITY

        if self.vspeed > MAX_VEL_Y:
            self.vspeed = MAX_VEL_Y


    def update_rect(self):
        """Update rect"""

        self.rect.update(self.x, self.y, self.rect.width, self.rect.height)

    
    def jump(self):
        """Make the bird jump"""

        self.vspeed = JUMP_FORCE

        # Play wing/jump sound
        self.jump_sound.play()


    def move(self, deltatime):
        """Move bird"""

        self.y += self.vspeed * deltatime


    def draw(self, screen):
        """Draw bird"""

        screen.blit(self.images[self.curr_img], self.rect)