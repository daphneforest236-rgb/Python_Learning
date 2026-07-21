import pygame
from pygame.sprite import Sprite

class AlienBomb(Sprite):
    def __init__(self, ai_game, alien):
        super().__init__()
        self.screen = ai_game.screen
        
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(0, 0, 5, 15)
        
        self.rect.midbottom = alien.rect.midbottom
        self.y = float(self.rect.y)
        
        self.speed = 0.5

    def update(self):
        self.y += self.speed
        self.rect.y = self.y

    def draw_bomb(self):
        pygame.draw.rect(self.screen, self.color, self.rect)