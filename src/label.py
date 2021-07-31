from globals import ORANGE


class Label:
    def __init__(self, x, y, text, font):
        self.text = text
        self.font = font
        self.img = font.render(text, True, ORANGE)
        self.rect = self.img.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2
        

    def modify(self, text):
        """Customize label"""

        self.img = self.font.render(text, True, ORANGE)


    def update(deltatime):
        pass


    def draw(self, screen):
        """Draw button"""

        screen.blit(self.img, self.rect)