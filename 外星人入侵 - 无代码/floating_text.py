import pygame
from pygame.sprite import Sprite

class FloatingText(Sprite):
    def __init__(self, ai_game, msg, center_pos):
        super().__init__()
        self.screen = ai_game.screen
        
        self.color = (255, 215, 0)
        self.font = pygame.font.Font(None, 28)
        
        self.image = self.font.render(msg, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = center_pos
        
        self.y = float(self.rect.y)
        
        self.timer = 30

    def update(self):
        self.y -= 1.5
        self.rect.y = self.y
        self.timer -= 1