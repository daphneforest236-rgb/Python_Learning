import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.midtop = ai_game.ship.rect.midtop
    
    def update(self):
        self.rect.y -= 2

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)