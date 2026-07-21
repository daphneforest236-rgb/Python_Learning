import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import time
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import random
from alien_bomb import AlienBomb
from floating_text import FloatingText

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星人入侵")

        self.bg_image = pygame.image.load('images/bg_image.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image, 
            (self.settings.screen_width, self.settings.screen_height)
        )

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien_bombs = pygame.sprite.Group()
        self.floating_texts = pygame.sprite.Group()
        self.firing = False
        self.last_shot_time = 0

        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self.play_button = Button(self, "Play")
        self.sb = Scoreboard(self)
        
        self._create_fleet()
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.2
        self.alien_points = 50
        self.score_scale = 1.5

        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        
        pygame.mixer.music.load('sounds/bg_music.ogg')
        self.laser_sound = pygame.mixer.Sound('sounds/laser.ogg')
        self.explosion_sound = pygame.mixer.Sound('sounds/explosion.ogg')
        
        pygame.mixer.music.set_volume(0.3)
        self.laser_sound.set_volume(0.4)
        self.explosion_sound.set_volume(0.5)

        pygame.mixer.music.play(-1)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                for a in self.aliens.sprites():
                    a.rect.y += self.fleet_drop_speed
                self.fleet_direction *= -1
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update(self.alien_speed, self.fleet_direction)
        
        if pygame.sprite.spritecollide(self.ship, self.aliens, True):
            self._ship_hit()
            
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.aliens.remove(alien)
                self._ship_hit()
                
        if self.aliens.sprites():
            if random.randint(1, 100) <= 3:
                frontline_aliens = {}
                for alien in self.aliens.sprites():
                    if alien.rect.x not in frontline_aliens or alien.rect.y > frontline_aliens[alien.rect.x].rect.y:
                        frontline_aliens[alien.rect.x] = alien
                
                if frontline_aliens:
                    random_alien = random.choice(list(frontline_aliens.values()))
                    new_bomb = AlienBomb(self, random_alien)
                    self.alien_bombs.add(new_bomb)

    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.floating_texts.empty()
            self.ship.speed = 3.0
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_bullets(self):
        self.bullets.update()
        
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.explosion_sound.play()
            for aliens_hit in collisions.values():
                self.stats.score += self.alien_points * len(aliens_hit)
            self.sb.prep_score()
            if collisions:
                for aliens_hit in collisions.values():
                    for alien in aliens_hit:
                        self.ship.speed += 0.1
                        
                        ft = FloatingText(self, "SPEED +10", alien.rect.center)
                        self.floating_texts.add(ft)
                        
                    self.stats.score += self.alien_points * len(aliens_hit)
                    self.sb.prep_score()
                    self.sb.check_high_score()
            
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.alien_speed *= self.speedup_scale
            self.alien_points = int(self.alien_points * self.score_scale)

    def _update_alien_bombs(self):
        self.alien_bombs.update()
        
        screen_rect = self.screen.get_rect()
        for bomb in self.alien_bombs.copy():
            if bomb.rect.top >= screen_rect.bottom:
                self.alien_bombs.remove(bomb)
                
        if pygame.sprite.spritecollide(self.ship, self.alien_bombs, True):
            self._ship_hit()

    def _create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        
        available_space_x = self.screen.get_rect().width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        ship_height = self.ship.rect.height
        available_space_y = self.screen.get_rect().height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)
        
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                new_alien = Alien(self)
                new_alien.x = float(alien_width + 2 * alien_width * alien_number)
                new_alien.rect.x = new_alien.x
                new_alien.rect.y = alien_height + 2 * alien_height * row_number
                
                self.aliens.add(new_alien)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True
                    elif event.key == pygame.K_SPACE:
                        self.firing = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = False
                    elif event.key == pygame.K_SPACE:
                        self.firing = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
                        self.stats.reset_stats()
                        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
                            self.stats.reset_stats()
                            self.stats.game_active = True
                            pygame.mouse.set_visible(False)
                        
                        self.alien_speed = 1.0
                        self.alien_points = 50
                        self.sb.prep_score()
                        self.sb.prep_ships()
                        self.stats.game_active = True
                        pygame.mouse.set_visible(False)
                        
                        self.bullets.empty()
                        self.aliens.empty()
                        self.alien_bombs.empty()
                        
                        self._create_fleet()
                        self.ship.rect.midbottom = self.screen.get_rect().midbottom

            if self.firing:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_shot_time > 200:
                    new_bullet = Bullet(self)
                    self.bullets.add(new_bullet)
                    self.last_shot_time = current_time
                    self.laser_sound.play()

            if self.stats.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_aliens()
                self._update_alien_bombs()

                self.floating_texts.update()
                for ft in self.floating_texts.copy():
                    if ft.timer <= 0:
                        self.floating_texts.remove(ft)
            
            self.screen.blit(self.bg_image, (0, 0))
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.aliens.draw(self.screen)
            for bomb in self.alien_bombs.sprites():
                bomb.draw_bomb()
            self.sb.show_score()

            if not self.stats.game_active:
                self.play_button.draw_button()


            self.ship.blitme()

            self.floating_texts.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(250)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()