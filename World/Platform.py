import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height,speedp):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((139, 69, 19))  # Cor marrom para a plataforma
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speedp


    def update(self):

        self.rect.x += self.speed
        if self.rect.centerx >= 800 or self.rect.centerx <= 0:
              self.speed *= -1
