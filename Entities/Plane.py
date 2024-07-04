import pygame
from entities.AmmoBox import AmmoBox
from entities.Bomb import Bomb


class Plane(pygame.sprite.Sprite):
    def __init__(self, ammo_group,bomb_group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 50))
        self.image.fill((192, 192, 192))
        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.x = 1
        self.rect.y = 100
        self.drop_counter = 0
        self.ammo_group = ammo_group
        self.bomb_group = bomb_group

    def drop(self, drop_counter):
        self.drop_counter = drop_counter
        if self.drop_counter % 360 == 0:
            ammo_drop = AmmoBox(self.rect.x, self.rect.y)
            self.drop_counter += 1
            self.ammo_group.add(ammo_drop)
        if self.drop_counter % 500 == 0:  # Adicione esta condição para dropar bombas
            bomb_drop = Bomb(self.rect.x, self.rect.y)
            self.bomb_group.add(bomb_drop)
        self.drop_counter += 1

    def patrol(self):
        self.rect.x += self.speed
        if self.rect.centerx >= 800 or self.rect.centerx <= 0:
            self.speed *= -1

    def update(self, *args):
        self.patrol()
        self.drop(self.drop_counter)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (192, 192, 192), self.rect.center)
