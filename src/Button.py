from globals import WHITE


class Button:
    def __init__(self, x, y, text, font):
        self.text = text
        self.font = font
        self.img = font.render(text, True, WHITE)
        self.rect = self.img.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        

    def collide(self, point):
        """Check if a point is inside the rectangle"""

        return self.rect.collidepoint(point)

    
    def change_color(self, color=WHITE):
        """Change color"""

        self.img = self.font.render(self.text, True, color)


    def update(deltatime):
        pass


    def draw(self, screen):
        """Draw button"""

        screen.blit(self.img, self.rect)
